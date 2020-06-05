#!/bin/bash

# Run dowload script and create testSuites.xml file with test cases
cd LR/07/tests/getTestSuites
sudo python3 -m venv env
sudo pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
sudo pip3 install openpyxl
sudo python3 googleDrive.py