# coding=utf-8
import inspect
from Loger import Logs 
logs = Logs()
name = None

from email import *
from global_Letter import Letter
from global_User import User
from main_2_base_WorkWithLetters import WorkWithLetters
from google_ValidateRules import ValidationMail as Val
import config_Project as cfg
import re
from email.message import EmailMessage
import config_Mail
import imaplib
import email
import base64
from google_Sheet import Sheet


def CheckEmail():
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name)
    
    """
    Точка входа в работу модуля.
    Чтение писем, их парсинг и валидация.
    """

    # Получение писем с почты
    imap_obj = imap_login()
    raw_letters = GetLetters(imap_obj)
    quit_email_imap(imap_obj)
    letters = []
    for item in raw_letters:
        letters.append(FormListWithLetters(item))

    # Получение резервных данных (функция пока не реализована)
    cfg.reserve_dates.GetReserveDate()

    # Проверка пользователей на существование в системе
    CheckUsers(letters)

    # Валидация писем
    ValidateLetters(letters)

    # Вызов следующей функции
    WorkWithLetters(letters)


def GetLetters(mail):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name,mail)
    """
   Функционал:
   - Прочитать письма на почте
   - Пометить прочитанные письма метками
   На входе:
   - None
   На выходе:
   - letters - объект, содержащий письма
   Что предусмотреть:
   - None
   Участвующие внешние типы переменных
   - None
   """
    with open(cfg.filename, "a") as file:
        file.write("\nПолучение писем... ")

    count = count_unseen_mess(mail)
    letters = []

    if count > 0:
        result, data = mail.uid('search', None, "unseen")  # Выполняет поиск и возвращает UID писем.
        print(count)
        for i in range(count):
            latest_email_uid = data[0].split()[i]
            result, date = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = date[0][1]
            letters.append(raw_email)


        with open(cfg.filename, "a") as file:
            file.write("Письма получены!")

    else:
        with open(cfg.filename, "a") as file:
            file.write("Новых сообщений нет!")
        # raise Exception("Letters is empty")

    return letters


def FormListWithLetters(mails):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name,mails)
    """
    Функционал:
    - Сформировать список экземпляров класса Letter на основе сырых данных по письмам
    На входе:
    - Объект с сырыми данными по письмам
    На выходе:
    - Список экземпляров класса Letter
    Что предусмотреть:
    - Парсинг сырых данных
    - Декодирование сырых данных
    - Заполнение всех полей в Letter на основе обработанной информации кроме 'Code' и 'CodeComment'
    - Поля 'Code' и 'CodeComment' заполняются только в случае существующего приложения к письму (что противоречит
    правилам отправки писем)
    - Заполнение поля User - вытаскивание всех данных о конкретном пользователе (кроме поля isRegistered)
    Участвующие внешние типы переменных
    - User (from import)
    - Letter (from import)
    """
    with open(cfg.filename, "a") as file:
        file.write("\nФормировка списка писем... ")

    try:
        try:
            email_message = email.message_from_string(mails)
        except TypeError:
            email_message = email.message_from_bytes(mails)
        error_code = ""
        from_mes = get_from(email_message)
        subject_mes = get_subject(email_message)
        user_email = from_parse(from_mes)
        name = name_parse(from_mes)
        body_str = get_body(email_message)
        body = body_parse(body_str)
        if body == "UNKNOWN":
            error_code = "05"

        user = User(name, None, user_email, None)
        letter_item = Letter(user, subject_mes, body, None, None)
        letter_item.CodeStatus = error_code

        with open(cfg.filename, "a") as file:
            file.write("Письма сформированы!")

        return letter_item
    except:
        user = User("UNKNOWN", None, "UNKNOWN", None)
        letter = Letter.Letter(user, "UNKNOWN", "UNKNOWN", None, None)
        letter.CodeStatus = "07"
        return letter


def CheckUsers(letters):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name,letters)
    """
    Функционал:
    - Проверить зарегистрированность каждого пользователя в системе по email
    На входе:
    - Список писем
    На выходе:
    - Расставленное поле 'isRegistered' в каждом письме в поле 'User'
    Что предусмотреть:
    - None
    Участвующие внешние типы переменных
    - None
    """
    with open(cfg.filename, "a") as file:
        file.write("\nПроверка пользователей... ")

    for i in letters:
        if i.CodeStatus == "0":
            result = Sheet.check_email(i.Student.Email)

            if not result:
                i.CodeStatus = "00"
                i.CodeStatusComment = "Пользователь не зарегистрирован"
            else:
                i.Student.IsRegistered = True
                i.Student.NameOfStudent = '{} {} {}'.format(result[0][0], result[0][1], result[0][2])
                i.Student.GroupOfStudent = '{}'.format(result[0][3])


    with open(cfg.filename, "a") as file:
        file.write("Пользователи проверены!")


def ValidateLetters(letters):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name,letters)
    """
    Функционал:
    - Провалидировать каждое письмо по правилам валидации
    На входе:
    - Список писем
    На выходе:
    - Расставленные поля 'Code' и 'CodeComment' в каждом письме
    Что предусмотреть:
    - Просле проверки вытащить ссылки на ресурсы и поместить их в поле 'Body' каждого письма
    - Проверку выполнять только если поле 'Code' ещё не заполнено
    - Поле 'CodeComment' заполнять сокращённой информацией по результатам проверки как угодно.
    Участвующие внешние типы переменных
    - None
    """
    with open(cfg.filename, "a") as file:
        file.write("\nВалидация писем... ")

    for let in letters:
        if let.CodeStatus == None or let.CodeStatus == "0":
            val = Val(let.ThemeOfLetter, let.Body)
            let.CodeStatus = val.validation(val.subject, val.body)
            if let.CodeStatus == '02':
                let.CodeStatusComment = 'Структура письма не соответствует требованиям к оформлению'
            elif let.CodeStatus == '03':
                let.CodeStatusComment = 'Номер варианта меньше 1 или больше 15 или не число'
            else:
                num, var = val.get_num_and_var(val.subject)
                if int(num) < 1 or int(num) > 15 or int(var) == 0:
                    let.CodeStatus = '03'
                    let.CodeStatusComment = 'Номер лабораторной не существует'
                else:
                    let.Number = var
                    let.Variant = num
            if let.CodeStatus == '20':
                let.Body = re.findall(r'http[^ \n]*', let.Body)
                let.CodeStatusComment = 'Работа отправлена на проверку'

    with open(cfg.filename, "a") as file:
        file.write("Письма провалидированы!")


def imap_login():
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name)
    """
    Авторизация в Gmail аккаунте.
    Функция возвращает SMTP объект.
    :return:
    """
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(config_Mail.EMAIL_ADDRESS, config_Mail.EMAIL_PASSWORD)
    imap.select('inbox')
    return imap

def quit_email_imap(imapObj):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name)
    """
    Закрытие SMTP объекта.
    Функция должна быть вызвана после завершения рыботы с SMTP объектом.
    :param smtpObj:
    :return:
    """
    imapObj.close()

def count_unseen_mess(mail):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name,mail)
    """
    Возвращает кол-во непрочитанных сообщений
    :param mail:
    :return:
    """
    result, data = mail.uid('search', None, "unseen")
    return len(data[0].split())


def get_from(email_message):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name,email_message)
    try:
        from_mes = str(email.header.make_header(email.header.decode_header(email_message['From'])))
        return from_mes
    except:
        return "UNKNOWN"


def get_subject(email_message):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name,email_message)
    try:
        subject_mes = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))
        return subject_mes
    except:
        return "UNKNOWN"


def from_parse(from_mes):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name,from_mes)
    try:
        user_email = from_mes[from_mes.find("<", 0, len(from_mes))+1:from_mes.find(">", 0, len(from_mes))]
        return user_email
    except:
        return "UNKNOWN"


def name_parse(from_mes):
    try:
        name = from_mes[0:from_mes.find("<", 0, len(from_mes))-1]
        return name
    except:
        return "UNKNOWN"

def name_parse(from_mes):
    try:
        name = from_mes[0:from_mes.find("<", 0, len(from_mes))-1]
        return name
    except:
        return "UNKNOWN"


def get_body(email_message):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name,email_message)
    try:
        str_body = ""
        if email_message.is_multipart():
            for payload in email_message.get_payload():
                str_body += payload.get_payload()
        else:
            str_body += email_message.get_payload()
        body_str = base64.b64decode(str_body).decode('utf8')
        return body_str
    except:
        return "UNKNOWN"


def body_parse(body_str):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name,body_str)
    if body_str.find("<div"):
        body_str = body_str.split("<div")[0]
        return body_str
    else:
        return body_str
