#!/bin/bash
sudo python -m venv env
sudo pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
sudo pip install openpyxl
sudo python googleDrive.py