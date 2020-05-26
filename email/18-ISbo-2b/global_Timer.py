# coding=utf-8
from threading import Timer

import config_Project as cfg

from email import *
from main_1_google_CheckEmail import CheckEmail

class Timer:

    timer = None

    def __init__(self):
        pass

    def SetTimer(self):
        """
        Функционал:
        - Поставить таймер на необходимое время,
	Таймер устанавливается на один час - 3600 секунд
        На входе:
        - None
        На выходе:
        - None
        Что предусмотреть:
        Функция CheckEmail должна содержать вызов функции SetTimer
        Участвующие внешние типы переменных
        - None
        """
        with open(cfg.filename, "a") as file: file.write("\nSetting timer...")

        t = Timer(3600, CheckEmail)
        t.start()

        with open(cfg.filename, "a") as file: file.write("Timer sets!")


    
