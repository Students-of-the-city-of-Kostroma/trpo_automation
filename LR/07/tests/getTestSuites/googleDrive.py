# -*- coding: utf-8 -*-
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from xml.etree.ElementTree import Element, SubElement, ElementTree

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    SAMPLE_SPREADSHEET_ID = '1d4DwpPxyc5DkmKFavszVM5prBqGhY7CCWIz_CnZOHEs'
    sheet = service.spreadsheets()
    SAMPLE_RANGE_NAME = 'test_suites!A3:J1000'
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
    allCases = result.get('values', [])

    testCases = Element('testCases')
    for testCase in allCases:
        if len(testCase) > 6 and testCase[6] in ['Y', 'A']:
            case = SubElement(testCases, 'case', { 'id': testCase[0] })
            input = SubElement(case, 'input', { 'text': testCase[2] })
            description = SubElement(case, 'description', { 'text': testCase[1] })
            expected = SubElement(case, 'expected', { 'text': testCase[5] })

    tree = ElementTree(testCases)
    tree.write("../../src/config/testSuites.xml")



if __name__ == '__main__':
    main()