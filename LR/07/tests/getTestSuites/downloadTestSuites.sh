#!/bin/bash

sudo apt-get install python3
sudo pip install --upgrade pip

# Run dowload script and create testSuites.xml file with test cases
cd LR/07/tests/getTestSuites
sudo python3 -m venv env
sudo pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
sudo pip install openpyxl
ls -la
sudo python3 googleDrive.py