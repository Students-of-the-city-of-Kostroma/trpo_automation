#!/bin/bash
python -m venv env
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install openpyxl
python googleDrive.py