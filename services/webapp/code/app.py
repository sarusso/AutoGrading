import os
import uuid
import logging
import requests

from flask import Flask, render_template, request
from utils import os_shell

# Set up logging
logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def menu():
    # Render opening menu page
    return render_template("menu.html")


@app.route("/upload", methods=["POST"])
def upload_file_and_exam():

    # Generate a grading session uuid
    uuid_str = str(uuid.uuid4())
        
    # Set the grading directory folder with the grading session uuid
    destination_folder = "/shared/{}".format(uuid_str)

    # Set destination dir
    try:
        os.makedirs(destination_folder)
    except PermissionError:
        os_shell("sudo chmod 777 /shared")
        os.makedirs(destination_folder)

    # Set the destination exam file
    exam_file = destination_folder + "/esame.py"
    
    # Get and save uploaded exam file or from URL
    try:
        url = request.form["url"]
        if not url:
            raise KeyError
        logger.debug('Getting file from "{}"'.format(url))
        r = requests.get(url, allow_redirects=True)
        with open(exam_file, 'wb') as f:
            f.write(r.content)
    except KeyError:
        f = request.files["file"]
        f.save(exam_file)
        logger.debug('Uploaded file')

    
    logger.debug("Saved exam file to '%s'", exam_file)

    # Set exam tests file
    exam_tests_file = "test_" + request.form["esami"] + ".py"
    logger.debug("Set exam tests file to '%s'", exam_tests_file)

    # Save exam tests file in the grading directory as well
    source_exam_file = "/opt/webapp/code/tests/" + exam_tests_file
    os_shell(" ".join(["cp", source_exam_file, destination_folder]))
    logger.debug("Copied tests file to '%s'", source_exam_file)

    # Grade and return
    return grade(uuid_str)


def grade(uuid_str):
    
    # Initialize page data
    data = {}
    
    # Create the docker run command.
    # To restrict RAM: --memory=\"256m\"
    command = "sudo docker run --cpus=\"0.1\" -v /tmp/autograding_shared/:/shared autograding/evaluator /bin/bash -c 'cd /shared/" + uuid_str + " && python3 -m unittest discover'"
    
    # Log the shell command going to be execute
    logger.debug("Shell executing command: \"%s\"", command)
    
    # Execute the command and capture the output
    out = os_shell(command, capture=True)
    
    # Log the output
    logger.debug("Shell output: \"%s\"", out)
    
    # Set the output in the page data
    data["shell_out"] = out

    # Render
    return render_template("grade.html", data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
