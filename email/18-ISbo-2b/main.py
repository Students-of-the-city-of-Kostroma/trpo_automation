#!/usr/bin/python3
# coding=utf-8
from main_1_CheckEmail import CheckEmail
from main_2_WorkWithLetters import WorkWithLetters
from main_3_SetResults import SetResults
from main_4_FormAnswers import FormAnswers
from main_5_InformUsers import InformUsers
import config_Project as cfg
from global_Logging import Logger

import inspect
from cryptography.fernet import Fernet
cipher = ""


def main():

    # Запуск работы
    while True:
        print(next(cfg.gen_num_for_filename))

        cfg.logger.createlogfile()
        i = cfg.logger
        print("ok")
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

        cfg.logger.closelogfile()

# Вызов начальной функции
if __name__ == '__main__':
    with open("c_config2", "r") as file3:
        key = file3.read()
        key = key[:len(key) // 2]
        cipher = Fernet(key)

    with open("c_token", "rb") as file:
        token = cipher.decrypt(file.read())
        with open("token.pickle", "wb") as file2:
            file2.write(token)

    with open("c_json", "rb") as file:
        json = cipher.decrypt(file.read())
        with open("trpo-bot-1eb977889b18.json", "wb") as file2:
            file2.write(json)

    with open("c_config", "rb") as file:
        config = cipher.decrypt(file.read())
        with open("config_Mail.py", "wb") as file2:
            file2.write(config)

    import config_Mail

    cfg.logger = Logger()

    main()
