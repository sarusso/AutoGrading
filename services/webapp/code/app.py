import logging
from flask import Flask, render_template, request
import uuid

# Set up logging
logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def menu():
    return render_template("menu.html")


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["file"]
        f.save("tmp/" + str(uuid.uuid4()) + ".py")
        return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)
