#!/bin/bash

# Upgrade Python to 3.7
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.7
sudo apt install python3-pip
sudo update-alternatives — install /usr/bin/python3 python3 /usr/bin/python3.7 2

# Run dowload script and create testSuites.xml file with test cases
cd LR/07/tests/getTestSuites
sudo python -m venv env
sudo pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
sudo pip install openpyxl
sudo python googleDrive.py