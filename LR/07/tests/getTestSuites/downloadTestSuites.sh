#!/bin/bash

# Run dowload script and create testSuites.xml file with test cases
cd LR/07/tests/getTestSuites
python -m pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib --user
python googleDrive.py