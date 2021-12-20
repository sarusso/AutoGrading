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
    # render opening menu page
    return render_template("menu.html")


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["file"]
        # save user file with unique id
        f.save("/tmp/" + str(uuid.uuid4()) + ".py")
        # render
        return render_template("upload.html")


@app.route("/upload", methods=["GET", "POST"])
def grade():
    if request.method == "POST":
        # Initialize page data
        data = {}
    
        # Create the docker run command.
        # TODO: let's start by just executing the Python script uploaded by the user
        command = "sudo docker run -it -v shared/uuid_dir:/data python:3.8 /data/tester.py"  # 'sudo docker run hello-world'
    
        # Log the shell command going to be execute
        logger.debug('Shell executing command: "%s"', command)
    
        # Execute the command and capture the output
        out = os_shell(command, capture=True)
    
        # Log the output
        logger.debug('Shell output: "%s"', out)
    
        # Set the output in the page data
        data['shell_out'] = out

        # Render
        return render_template("grade.html", data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
