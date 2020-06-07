import config_Mail
import imaplib
from email.message import EmailMessage
import base64
import smtplib
import email

def imap_login():
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
    """
    Закрытие SMTP объекта.
    Функция должна быть вызвана после завершения рыботы с SMTP объектом.
    :param smtpObj:
    :return:
    """
    imapObj.close()


def count_unseen_mess(mail):
    """
    Возвращает кол-во непрочитанных сообщений
    :param mail:
    :return:
    """
    result, data = mail.uid('search', None, "unseen")
    return len(data[0].split())


def get_from(email_message):
    try:
        from_mes = str(email.header.make_header(email.header.decode_header(email_message['From'])))
        return from_mes
    except:
        return "UNKNOWN"


def get_subject(email_message):
    try:
        subject_mes = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))
        return subject_mes
    except:
        return "UNKNOWN"


def from_parse(from_mes):
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


def get_body(email_message_instance):
    try:
        maintype = email_message_instance.get_content_maintype()
        if maintype == 'multipart':
            for part in email_message_instance.get_payload():
                if part.get_content_maintype() == 'text':
                    return part.get_payload()
        elif maintype == 'text':
            return email_message_instance.get_payload()
    except:
        return "UNKNOWN"


def body_parse(mail):
    text = mail
    try:
        result = base64.b64decode(text).decode('utf8')
        if result.find("*") >= 0:
            result = result.replace("*", "")
        return result
    except:
        return mail

def send_mes(smtp_obj, message):
    try:
        # Создание экземпляра класса Email Message
        mes = EmailMessage()

        # Заполнение поля отправителя
        mes['From'] = "ТРПО ИАСТ"

        # Заполнение поля получателя
        mes['To'] = message.Who

        # Заполнение темы письма
        mes['Subject'] = message.Theme

        # Заполнение тела письма
        mes.set_content(message.Body)

        # отправка SMTP пакета
        smtp_obj.send_message(mes)

        message.Success = True

    except:
        message.Success = False

def smtp_login():
    """
    Авторизация в Gmail аккаунте.
    Функция возвращает SMTP объект.
    :return:
    """

    smtpObj = smtplib.SMTP('smtp.gmail.com:587')
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.ehlo()
    smtpObj.login(config_Mail.EMAIL_ADDRESS, config_Mail.EMAIL_PASSWORD)

    return smtpObj

def quit_email_smtp(smtpObj):
    """
    Закрытие SMTP объекта.
    Функция должна быть вызвана после завершения рыботы с SMTP объектом.
    :param smtpObj:
    :return:
    """

    smtpObj.close()

def check_attachments(mail):
    """
    Проверка на наличие вложений
    :param mail:
    :return:
    """
    if mail.is_multipart():
        for part in mail.walk():
            filename = part.get_filename()
            if filename:
                return True
    else:
        return False
