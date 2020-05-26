# coding=utf-8
from work_Loger import Logs
from email.message import EmailMessage
import config_Project as cfg
import config_Mail

import smtplib
import email
from datetime import datetime
import inspect


def InformUsers(answersForUsers):
    """
    Разослать письма пользователям
    """

    # Создание SMTP объекта
    smtp_obj = smtp_login()

    # Отправка ответов пользователям
    # Глобальная функция 9
    SendLetters(smtp_obj, answersForUsers)

    # Закрытие SMTP объекта
    quit_email_smtp(smtp_obj)

    # Формирование нового имени файла логов
    FormFilename()


def SendLetters(smtp_obj, answersForUsers):
    """
     Функционал:
    - Разослать письма пользователям
    На входе:
    - Сформированный список экземпляров класса AnswersForUsers, где в поле Who находится email пользователя,
    в поле Theme - тема письма, а в поле Body - тело письма
    На выходе:
    - None
    Что предусмотреть:
    - None
    Участвующие внешние типы переменных
    - None
    """
    # logs = Logs()
    # name = inspect.currentframe().f_code.co_name
    # logs.Infor(name, answersForUsers)

    for i in answersForUsers:
        # Отправка ответа по экземпляру списка ответов
        send_mes(smtp_obj, i)


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


def FormFilename():
    """
    Формирование имени файла логов
    """

    name = datetime.strftime(datetime.now(), "%Y.%m.%d")

    if name != cfg.last_date:
        cfg.last_date = name
        cfg.gen_num_for_filename = cfg.num_for_filename()

    cfg.filename = cfg.path_to_logs + "log_" + name + "_" + str(next(cfg.gen_num_for_filename)) + ".txt"

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
