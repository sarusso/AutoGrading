import os
import uuid
import logging

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

    f = request.files["file"]
    exam_file = "test_" + request.form["esami"].replace(" ", "_") + ".py"
    uuid_str = str(uuid.uuid4())
        
    # Save user file with unique id
    destination_folder = "/shared/{}".format(uuid_str)
    destination_file = destination_folder + "/esame.py"
    try:
        os.makedirs(destination_folder)
    except PermissionError:
        os_shell("sudo chmod 777 /shared")
        os.makedirs(destination_folder)
            
    f.save(destination_file)
    logger.debug("Saved file to '%s'", destination_file)

    # Save exam file in the same dir
    source_exam_file = "/opt/webapp/code/tests/" + exam_file

    os_shell(" ".join(["cp", source_exam_file, destination_folder]))
    logger.debug("Copied file to '%s'", source_exam_file)

    return grade(uuid_str, exam_file)


def grade(user_id, exam):
    # Initialize page data
    data = {}
    # Create the docker run command.
    command = "sudo docker run --memory=\"256m\" --cpus=\"0.1\" -v /tmp/autograding_shared/:/shared python:3.8 /bin/bash -c 'cd /shared/" + user_id + " && python -m unittest discover'"
    
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
