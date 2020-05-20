#!/usr/bin/python3
# coding=utf-8
from time import sleep
from datetime import datetime
from threading import Timer

from main_1_google_CheckEmail import CheckEmail
from main_2_base_WorkWithLetters import WorkWithLetters
from main_3_send_SetResults import SetResults
from main_4_moderate_FormAnswers import FormAnswers
from main_5_send_InformUsers import InformUsers
import config_Project as cfg
from reserve_Reserve import Reserve

import inspect
from Loger import Logs
logs = Logs()
name = None


def Main():
        name = inspect.currentframe().f_code.co_name
        logs.Infor(name)
    # try:
        # Создание объекта резервных данных
        cfg.reserve_dates = Reserve()

        # Формирование имени файла лога
        cfg.filename = cfg.path_to_logs + "log_" + datetime.strftime(datetime.now(), "%Y.%m.%d") + "_" + str(next(cfg.gen_num_for_filename)) + ".txt"

        # Запись в лог о начале работы
        with open(cfg.filename, "a") as file:
            file.write("Начало работы... ")

        # Запуск работы
        # while True:
            # Установка таймаута ожидания

        letters = CheckEmail()                          # main_1
        letterResults = WorkWithLetters(letters)        # main_2
        letterResults = SetResults(letterResults)       # main_3
        answers = FormAnswers(letterResults)            # main_4
        InformUsers(answers)                            # main_5


        # start_function = Timer(cfg.timeout, CheckEmail)
        #
        # # Запуск таймера до начала работы
        # start_function.start()

    # except Exception as err:
    #
    #     # Запись в лог о ошибке
    #     with open(cfg.filename, "a") as file:
    #         file.write("Извините, у вас возникла ошибка, " + str(err) + " перезапускаю...")
    #
    #     # Перезапуск
    #     Main()

# Вызов начальной функции
if __name__ == '__main__':
    Main()
