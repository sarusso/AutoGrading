# Auto Grading

_An automatic Python assignment grading project using unit-testing_




## Quickstart

Requirements:
    
    Bash, Git and Docker. Runs on Linux, Mac or Windows*.

*Windows not fully supported in development mode due to lack of support for symbolic links.


Build

    $ autograding/build

Run

	$ autograding/run

Play

    Open a browser to http://localhost:5000


Clean

	$ autograding/clean



### Extras

Check running services

    $ autograding/ps
    

Check webapp service logs

    $ autograding/logs webapp



### Building errors

It is common for the build process to fail with a "404 not found" error on an apt-get instrucions, as apt repositories often change their IP addresses. In such case, try:

    $ autograding/build nocache


### Development mode

Flask development server is running on port 5000 of the "webapp" service.

To enable live code changes, uncomment the following line in the docker-compose.yaml file, under the "volumes" section of the "webapp" service:

    - ./services/webapp/code:/opt/webapp/code
    
This will mount the code from the services/webapp/code directory as a volume inside the webapp container itself allowing to make codebase changes immediately effective.