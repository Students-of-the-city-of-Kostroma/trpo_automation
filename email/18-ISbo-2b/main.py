#!/usr/bin/python3
# coding=utf-8
from main_1_CheckEmail import CheckEmail
from main_2_WorkWithLetters import WorkWithLetters
from main_3_SetResults import SetResults
from main_4_FormAnswers import FormAnswers
from main_5_InformUsers import InformUsers
import config_Project as cfg
from work_Loger import Logs

import inspect
# from datetime import datetime


def main():
    # logs = Logs()
    # name = inspect.currentframe().f_code.co_name
    # logs.Infor(name)

    # # Формирование имени файла лога
    # cfg.filename = cfg.path_to_logs + "log_" + datetime.strftime(datetime.now(), "%Y.%m.%d") + "_" + str(
    #     next(cfg.gen_num_for_filename)) + ".txt"

    # Запуск работы
    while True:
        print(next(cfg.gen_num_for_filename))

        # main_1
        letters = CheckEmail()

        # Тестирование
        print(len(letters))
        print(letters)

        # main_2
        letterResults = WorkWithLetters(letters)

        # Тестирование
        print(letterResults)

        # main_3
        letterResults = SetResults(letterResults)

        # Тестирование
        print(letterResults)

        # main_4
        answers = FormAnswers(letterResults)

        # Тестирование
        print(answers)

        # main_5
        InformUsers(answers)


# Вызов начальной функции
if __name__ == '__main__':
    main()
