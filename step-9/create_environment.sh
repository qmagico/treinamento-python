#!/bin/bash

# installing pip
sudo apt-get install -y python-setuptools
sudo easy_install pip

#installing virtualenvwrapper
sudo pip install virtualenv

# create virtualenv
virtualenv unifesp

# activate virtualenv
. ./unifesp/bin/activate

pip install -r requirements.txt
