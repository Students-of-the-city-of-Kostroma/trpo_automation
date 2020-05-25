# coding=utf-8
from time import sleep
from datetime import datetime
from email.message import EmailMessage

import config_Project as cfg
import config_Mail
import smtplib
import email

import inspect
from Loger import Logs
logs = Logs()
name = None

def InformUsers(answersForUsers):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name,answersForUsers)
    """
    Разослать письма пользователям, внести пользователей в список, заархивировать письма, дождаться таймера
    """
    # Отправление писем пользователям
    # Создание SMTP объекта
    smtp_obj = smtp_login()
    # Отправка ответов пользователям
    SendLetters(smtp_obj, answersForUsers)
    # Закрытие SMTP объекта
    quit_email_smtp(smtp_obj)

    print(answersForUsers)

    # Добавление пользователей (функция пока не реализована)
    AddUsers()

    # Формирование нового имени файла логов
    FormFilename()


def SendLetters(smtp_obj, answersForUsers):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name,smtp_obj, answersForUsers)
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

    with open(cfg.filename, "a") as file:
        file.write("\nОтправление ответов пользователю... ")

    for i in answersForUsers:
        # Отправка ответа по экземпляру списка ответов
        send_mes(smtp_obj, i)

    with open(cfg.filename, "a") as file:
        file.write("Ответы отправлены!")

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
        with open(cfg.filename, "a") as file:
            file.write("\nОтвет отправлен!")
    except:
        message.Success = False
        with open(cfg.filename, "a") as file:
            file.write("\nОшибка при отправке ответа!")

def AddUsers():
    """
    Функционал:
    - Добавить в журнал тех пользователей, которые заполнили форму регистрации
    На входе:
    - None
    На выходе:
    - None
    Что предусмотреть:
    - Внести в список только тех, кто заполняет форму регистрации с момента последнего добавления
    Возможно, предусмотреть удаление записей из временного списка после добавления в основной журнал
    Участвующие внешние типы переменных
    - None
    """
    with open(cfg.filename, "a") as file:
        file.write("\nДобавление пользователей... ")

    with open(cfg.filename, "a") as file:
        file.write("Пользователи добавлены!")

def FormFilename():
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name)
    """
    Формирование имени файла логов
    """
    name = datetime.strftime(datetime.now(), "%Y.%m.%d")
    if name != cfg.last_date:
        cfg.last_date = name
        cfg.gen_num_for_filename = cfg.num_for_filename()

    cfg.filename = cfg.path_to_logs + "log_" + name + "_" + str(next(cfg.gen_num_for_filename)) + ".txt"

def smtp_login():
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name)
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
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name, smtpObj)
    """
    Закрытие SMTP объекта.
    Функция должна быть вызвана после завершения рыботы с SMTP объектом.
    :param smtpObj:
    :return:
    """
    smtpObj.close()
