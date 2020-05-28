#coding: utf-8
import pickle
import os.path
import httplib2
import apiclient.discovery
import re
import email
import base64
import log_method
from oauth2client.service_account import ServiceAccountCredentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.multipart import MIMEMultipart
from googleapiclient.discovery import build
from email.mime.text import MIMEText
from datetime import datetime
from pprint import pprint
from config import (
    SPREAD_SHEET_ID,
    CREDENTIALS_FILE,
    SPREAD_SHEET_ID_INIT,
    CREDENTIALS_FILE_SERVICE,
)
from pattern import *

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 
          'https://www.googleapis.com/auth/gmail.send',
          'https://www.googleapis.com/auth/gmail.labels',
          'https://www.googleapis.com/auth/gmail.modify']

@log_method.log_method_info
def get_service():
    """
    Описание: Подключение к почте.
    """
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
            	CREDENTIALS_FILE_SERVICE,
                SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service

#Костыль для работы c gmailAPI.
#service = get_service()
#user_id = 'me'


@log_method.log_method_info
def add_str_in_table(table: str, cell: str, mark: str):
    """
    Добавление символа\предложения в таблице.

    :param table: Название таблицы.
    :param cell: Ячейка.
    :param mark: Символ\предложение.
    """
    log_method.logger.debug(f'add_mark_in_table: table - {table}, \
                            cell - {cell}, mark - {mark}')
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
                    CREDENTIALS_FILE,
                    [
                        'https://www.googleapis.com/auth/spreadsheets',
                        'https://www.googleapis.com/auth/drive'
                    ]
    )
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http = httpAuth) 
    rangeTab = f"(ТРПО) {table}!{cell}"
    service.spreadsheets().values().batchUpdate(spreadsheetId=SPREAD_SHEET_ID, 
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {
                    "range": rangeTab,
                    "majorDimension": "ROWS",     
                    "values": [ [mark] ]
                }
        ]
    }).execute()

        
@log_method.log_method_info
def cleaning_email(email_id: str):
    """
    Метод для выделения почты из передаваемой строки email.
    Name Surname <1234@gmail.com> ← пример email который мне передают
    1234@gmail.com это будет запоминаться после метода очистки

    :param email: Передаваемая строка с почтой
    :return: email без спец.знаков
    """
    comp = re.compile(r'<(\S*?)>')
    y = comp.search(email_id)
    q = y.group(0)
    z = q.replace('<', '').replace('>', '')
    return z


@log_method.log_method_info
def name_surname(email_id: str):
    """ 
    Метод для выделения и передачи имени и фамилии.
    :param email_id: Строка по типу <Иван Иванович>
    :return: Возвращает строку по типу "Иван Иванович"
    """
    comp = re.compile('(\S*?) '+'(\S*?) ')
    y = comp.search(email_id)
    return y.group(0)


@log_method.log_method_info
def search_email(email_id: str, spreadsheetid: str = SPREAD_SHEET_ID_INIT):
    """
    Метод поиска электронной почты в таблице.

    :param email_id: электронная почта
    :param spreadsheetid: таблица для поиска
    :return: возвращает электронную почту/None
    """
    mail_str = cleaning_email(email_id)
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
                CREDENTIALS_FILE,
                [
                    'https://www.googleapis.com/auth/spreadsheets',
                    'https://www.googleapis.com/auth/drive'
                ]
            )
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
    range_name = 'List1!B1:B1000'
    table = service.spreadsheets().values().get(
          spreadsheetId=spreadsheetid,
          range=range_name).execute()
    if re.search(mail_str, str(table)):
        return mail_str
    else:
        return None


@log_method.log_method_info
def get_message(service, user_id):
    """ 
    Метод получения полезной информации из письма студента.

    :params service: подключенный хук
    :params user_id: id подключаемого(может быть 'me')
    :return: { 'id_of_msg', 'email_id', 'head_of_msg', 'body_of_msg', 'date_of_msg' }
    """
    search_id = service.users().messages().list(
        userId=user_id,
        labelIds=['UNREAD']
    ).execute()
    message_id = search_id['messages']
    alone_msg = message_id[0]
    id_of_msg = alone_msg['id']
    change_label = {'removeLabelIds':['UNREAD'], 'addLabelIds':[]}
    change_msg_label = service.users().messages().modify(userId=user_id,
                                                         id=id_of_msg,
                                                         body=change_label
                                                        ).execute()
    message_list = service.users().messages().get(userId=user_id, 
                                                  id=id_of_msg,
                                                  format='full').execute()
    info_of_msg = message_list.get('payload')['headers']
    email_id = ''
    head_of_msg = ''
    body_of_msg = ''
    date_of_msg = ''
    for head in info_of_msg :
        if head['name'] == 'From' :
            email_id = head['value']
        if head['name'] == 'Subject' :
            head_of_msg = head['value']
        if head['name'] == 'Date' :
            date_of_msg = head['value']
    body_of_msg = message_list['snippet']

    message_info = {'id_of_msg':id_of_msg,
                    'email_id':email_id,
                    'head_of_msg':head_of_msg,
                    'body_of_msg':body_of_msg,
                    'date_of_msg': date_of_msg}
    return message_info


@log_method.log_method_info
def email_archiving(service, user_id, message_info):
    """
    Архивация сообщения.
    
    service: авторизация через мыло.  
    user_id: наше мыло или спец слово 'me'.  
    message_info: словарь с данными письма.
    """
    msg_labels = {'removeLabelIds': ['UNREAD', 'INBOX'],
                  'addLabelIds': []
                  }

    message = service.users().messages().modify(userId=user_id,
                                                id=message_info['id_of_msg'],
                                                body=msg_labels).execute()


@log_method.log_method_info
def send_message(service, user_id, email_of_student, name_of_student,
                 number_of_templates, validation_dictionary, 
                 error_dictionary, message_info):
    """
    Метод по отправке сообщения студенту.  
    
    :param service: авторизация через мыло.
    :param user_id: наше мыло или спец слово 'me'.
    :param email_of_student: мыло студента.
    :param name_of_student: имя и фамилия студента.
    :param validation_dictionary: словарь с валидации письма,
    в котором есть ('Numder')номер работы и ('URL')ссылка на работу.  
    :param error_dictionary: словарь с ошибками в коде студента.
    :param number_of_templates: номер используемого для заполнения письма шаблона.
    """

    str_of_val_er = ""
    str_of_er = "" 
    if number_of_templates == 1:
        str_of_val_er = error_in_work(validation_dictionary)
    elif number_of_templates == 2:
        str_of_er = error_in_work(error_dictionary)

    message_templates = funcSt(str_of_val_er, str_of_er)

    sending_msg = {}
    hello_student = funcHello(name_of_student)
    sending_msg['from'] = GMAIL_OF_TRPO
    our_msg = message_templates[number_of_templates]['our_msg']
    title = message_templates[number_of_templates]['title']
    date_of_msg = message_info['date_of_msg']
    return_body = message_info['body_of_msg']
    return_head = message_info['head_of_msg']

    sending_msg = MIMEMultipart('alternative')
    return_text = funcReturnMsg(hello_student, our_msg, SIGNATURE,
                                date_of_msg, return_body,
                                return_head)
    sending_msg = MIMEText(return_text)
    sending_msg['To'] = email_of_student
    sending_msg['Subject'] = title

    raw = base64.urlsafe_b64encode(sending_msg.as_bytes())
    raw = raw.decode()
    body = {'raw': raw}

    send_msg = service.users().messages().send(userId=user_id, 
                                               body=body).execute()
    

@log_method.log_method_info
def send_message_to_techsub(service, user_id, email_of_student, 
                            name_of_student, validation_dictionary, 
                            error_dictionary, number_of_templates):
    """
    Рассылка писем ТП.
    Вызывается преподавателю, если у студента есть ошибки в работе
    или ТП, если упал один из модулей
    :param service: авторизация через мыло
    :param user_id: наше мыло или спец слово 'me'
    :param email_of_student: мыло студента
    :param name_of_student: имя и фамилия студента
    :param validation_dictionary: словарь с валидации письма,
    в котором есть ('Numder')номер работы и ('URL')ссылка на работу
    :param error_dictionary: словарь с ошибками в коде студента
    :param number_of_templates: номер используемого для заполнения письма шаблона
    """

    if number_of_templates == 0:
        str_of_er = error_in_work(error_dictionary)
    else:
        str_of_er = ""

    message_templates = funcTs(name_of_student, validation_dictionary, str_of_er)
    sending_msg = {}

    sending_msg['From'] = GMAIL_OF_TRPO

    sending_msg = MIMEMultipart('alternative')
    sending_msg = MIMEText(message_templates[number_of_templates]['hello'] + 
                           message_templates[number_of_templates]['our_msg'] + 
                           SIGNATURE)
    sending_msg['Subject'] = message_templates[number_of_templates]['title']
    # Косяк!!!
    if number_of_templates == 0:
        for i in MAS_OF_TO:
            sending_msg['To'] = i

            raw = base64.urlsafe_b64encode(sending_msg.as_bytes())
            raw = raw.decode()
            body = {'raw': raw}
    else:
        sending_msg['To'] = EMAIL_OF_TEACHER

        raw = base64.urlsafe_b64encode(sending_msg.as_bytes())
        raw = raw.decode()
        body = {'raw': raw}

    send_msg = service.users().messages().send(userId=user_id, body=body).execute()
    

@log_method.log_method_info
def error_in_work(some_errors: dict):
    """
    Метод преобразования массива с ошибками в строку
    Метод используется для валидации и ошибок кода студента
    :param some_errors: Словарь из валидации
    """
    error = ""
    mas_of_er = some_errors["errorDescription"]
    i = 0
    while i < len(mas_of_er):
        error += "- " + mas_of_er[i] + "\n"
        i += 1
    return error


@log_method.log_method_info
def search_group(email_id):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
                CREDENTIALS_FILE,
                ['https://www.googleapis.com/auth/spreadsheets',
                 'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
    spreadsheetId = SPREAD_SHEET_ID_INIT
    range_name = 'List1!B1:B1000'
    table = service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId,
            range=range_name).execute()
    c = 1
    for val in table.get('values'):
        if val[0] != email_id:
            c += 1
        else:
            break
    if c == len(table.get('values'))+1:
        return None
    else:
        nomer = f'List1!F{c}:G{c}'
        table1 = service.spreadsheets().values().get(
               spreadsheetId=spreadsheetId, range=nomer).execute()
        values_finish = table1.get('values')[0]
        return tuple(values_finish)


@log_method.log_method_info
def search_tablic(group, laba, surname):
    group = f'(ТРПО) {group}'
    c = 2
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
                CREDENTIALS_FILE,
                ['https://www.googleapis.com/auth/spreadsheets',
                 'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
    spreadsheetId = SPREAD_SHEET_ID
    range_name = f'{group}!D2:D1000'
    table = service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId, range=range_name).execute()
    count = ord('J') + int(laba)-1
    nomer_stolbca = chr(count)
    try:
        for name in table.get('values'):
            if name[0] != surname:
                c = c+1
            else:
                break
        position = str(chr(count)) + str(c)
    except:
        return None
    else:
        return position

    
def search_dolgi(group, position):
    """
    Метод для поиска долгов 
    :param group: (ТРПО) название группы
    :param position: 'J7' позиция студента в таблице
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
    )
    http_auth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=http_auth)
    dolg=[]
    number_laboratorn=-1
    range_name = f'{group}!D{position[1]}:P{position[1]}'
    table = service.spreadsheets().values().get(spreadsheetId=SPREAD_SHEET_ID, range=range_name).execute()
    for p in table.get('values')[0]:
        number_laboratorn=number_laboratorn+1 
        try:
            if p[0] == '0':
                dolg.append(number_laboratorn)
        except:
            dolg.append(number_laboratorn)
    if len(dolg) == 0:
        return None
    if len(dolg) > 0:
        return dolg


def add_table(group, name):
    """
    Метод для добавления студента
    :param group: (ТРПО) название группы
    :param name: ФИО студента
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
                CREDENTIALS_FILE,
                [
                    'https://www.googleapis.com/auth/spreadsheets',
                    'https://www.googleapis.com/auth/drive'
                ]
    )
    http_auth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=http_auth)
    range_name=f'{group}!A1:A100'
    table = service.spreadsheets().values().get(
                spreadsheetId=SPREAD_SHEET_ID,
                range=range_name).execute()
    column = 1
    for i in table.get('values'):
        if(i[0] == name):
            status=('available',)
            count=0
            break
        else:
            column =column  + 1
            range_name = f'{group}!A{column}:A{column}'
            count = 1
            
    if count == 1:
        try:
            service.spreadsheets().values().batchUpdate(spreadsheetId=SPREAD_SHEET_ID, body={
                        "valueInputOption": "USER_ENTERED",
                        "data": [
                                {
                                    "range":range_name ,
                                    "majorDimension": "ROWS",
                                    "values": [
                                        [name]
                                    ]
                                }
                        ]
                }).execute()
            status = ('accepted',)
        except:
            status = ('error',)
    return status


def get_log():
    from collections import deque
    try:
        file_name = 'product_logs.log'
        with open(file_name) as f:
            date = list(deque(f, 5))
        return date
    except:
        return "We have problems with file logs. Please help us"
