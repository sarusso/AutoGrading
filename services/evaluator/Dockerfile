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
    
#------------------------------
# Apt requirements
#------------------------------

# Download get-pip script
RUN curl -O https://bootstrap.pypa.io/get-pip.py

# Install Python3 and Pip3 (python3-distutils required for pip3)
RUN apt-get install python3 python3-distutils -y 
RUN python3 get-pip.py 'pip==21.0.1'

#------------------------------
# Python requirements
#------------------------------

RUN pip3 install python-dateutil==2.8.2 numpy
