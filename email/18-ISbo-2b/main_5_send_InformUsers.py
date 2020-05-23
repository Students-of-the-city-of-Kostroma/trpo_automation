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
    smtp_obj = smtp_login() # Создание SMTP объекта
    SendLetters(smtp_obj, answersForUsers) # Отправка ответов пользователям
    quit_email_smtp(smtp_obj) # Закрытие SMTP объекта

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
        send_mes(smtp_obj, i) # Отправка ответа по экземпляру списка ответов

    with open(cfg.filename, "a") as file:
        file.write("Ответы отправлены!")

def send_mes(smtp_obj, message):
    try:
        mes = EmailMessage() # Создание экземпляра класса Email Message
        mes['From'] = "ТРПО ИАСТ" # Заполнение поля отправителя
        mes['To'] = message.Who # Заполнение поля получателя
        mes['Subject'] = message.Theme # Заполнение темы письма
        mes.set_content(message.Body) # Заполнение тела письма
        smtp_obj.send_message(mes) # отправка SMTP пакета
        with open(cfg.filename, "a") as file:
            file.write("\nОтвет отправлен!")
    except:
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