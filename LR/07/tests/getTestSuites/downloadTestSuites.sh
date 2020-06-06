#!/bin/bash
# Run dowload script and create testSuites.xml file with test cases
#pip install virtualenv
cd LR/07/tests/getTestSuites
#virtualenv env
python -m pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
python googleDrive.py