# coding=utf-8
from work_Loger import Logs
from email.message import EmailMessage
import work_EmailLibrary as EmailLibrary
import config_Project as cfg
import config_Mail

from datetime import datetime
import inspect


def InformUsers(answersForUsers):
    """
    Разослать письма пользователям
    """

    # Создание SMTP объекта
    smtp_obj = EmailLibrary.smtp_login()

    # Отправка ответов пользователям
    # Глобальная функция 9
    SendLetters(smtp_obj, answersForUsers)

    # Закрытие SMTP объекта
    EmailLibrary.quit_email_smtp(smtp_obj)

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
        EmailLibrary.send_mes(smtp_obj, i)

def FormFilename():
    """
    Формирование имени файла логов
    """

    name = datetime.strftime(datetime.now(), "%Y.%m.%d")

    if name != cfg.last_date:
        cfg.last_date = name
        cfg.gen_num_for_filename = cfg.num_for_filename()

    cfg.filename = cfg.path_to_logs + "log_" + name + "_" + str(next(cfg.gen_num_for_filename)) + ".txt"
