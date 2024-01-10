FROM ubuntu:20.04
MAINTAINER Stefano Alberto Russo <stefano.russo@gmail.com>

# Always start with an apt-get update when extending base images,
# otherwise apt repositories might get outdated (404 not found)
# and building without cache does not re-build base images.
RUN apt-get update

# Utilities: Curl, Nano and sudo
RUN apt-get install curl sudo -y

# Add ubuntu group and user
RUN groupadd -g 1000 ubuntu
RUN useradd ubuntu -d /home/ubuntu -u 1000 -g 1000 -m -s /bin/bash

# Add ubuntu user to sudoers
RUN adduser ubuntu sudo
    
# No pass sudo
COPY sudoers /etc/sudoers

#------------------------------
# Apt requirements
#------------------------------

# Download get-pip script
RUN curl -O https://bootstrap.pypa.io/get-pip.py

# Install Python3 and Pip3 (python3-distutils required for pip3)
RUN apt-get install python3 python3-distutils -y 
RUN python3 get-pip.py 'pip==21.0.1'

# Python 3 dev (for pycrypto)
RUN apt-get install python3-dev -y

# Install Docker client
RUN apt-get install docker.io -y

# Build essential for uWSGI
RUN apt-get -y install build-essential

#------------------------------
# Python requirements
#------------------------------

# Install Flask etc.
RUN pip install flask==2.0.2 requests==2.28.1 uwsgi==2.0.21 Werkzeug==2.2.2

#------------------------------
# Install Flask project
#------------------------------

# Prepare dir
RUN mkdir -p /opt/webapp/code

# Copy over code
COPY code /opt/webapp/code

# Fix permissions
RUN chown -R ubuntu:ubuntu /opt/webapp


#------------------------------
# Entrypoint
#------------------------------

# Run script
COPY run.sh /
RUN chmod 755 /run.sh

# Entrypoint
COPY entrypoint.sh /
RUN chmod 755 /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]





