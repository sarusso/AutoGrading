import logging
from flask import Flask
from utils import os_shell

# Set up logging
logging.basicConfig(format="[%(levelname)s] %(asctime)s %(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/")
def hello():
    
    # Run the hello world docker container from the OS shell
    #logger.debug(os_shell('sudo docker run hello-world', capture=True)

    # Get who am I from the OS shell
    whoami = os_shell('whoami', capture=True).stdout
    
    return 'Hello, World! I am running as "{}".'.format(whoami)