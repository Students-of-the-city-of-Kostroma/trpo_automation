import unittest
import global_User
import global_Letter
import json
import config_Project
import global_Logging

config_Project.logger = global_Logging.Logger()
i = config_Project.logger
config_Project.logger.createlogfile()

import main_2_WorkWithLetters



class MyTestCase(unittest.TestCase):
    def test_S_5_t1(self):
        """Лабораторная работа с номером из списка [2, 3, 11]"""

        # Создание студента
        student3 = global_User.User("Артём Гусев", "18-ИСбо-2", None, None)

        # Список писем
        letters = []

        # Создание письма в соответствии со сценарием
        letter = global_Letter.Letter(student3, "ЛР01", None, 1, 3)
        letter.Body = "Artyom_Gusev"
        letter.CodeStatus = "20"

        letters.append(letter)

        # Формирование JSON
        jsonDates_received = main_2_WorkWithLetters.FormJSONDates(letters)

        # Формирование ожидаемого JSON
        json3_expected = {
            "messageType": 1,
            "lab": 3,
            "variant": 1,
            "link": "Artyom_Gusev",
            "code": None
        }

        jsonDates_expected = [json.dumps(json3_expected)]

        self.assertEqual(jsonDates_received, jsonDates_expected)
    def test_S_5_t2(self):
        """Лабораторная работа с номером из списка [4, 5, 6, 7, 8, 9, 10, 12]"""

        # Создание студента
        student3 = global_User.User("Артём Гусев", "18-ИСбо-2", None, None)

        # Список писем
        letters = []

        # Создание письма в соответствии со сценарием
        letter = global_Letter.Letter(student3, "ЛР01", None, 1, 7)
        letter.Body = "Artyom_Gusev"
        letter.CodeStatus = "20"

        letters.append(letter)

        # Формирование JSON
        jsonDates_received = main_2_WorkWithLetters.FormJSONDates(letters)

        # Формирование ожидаемого JSON
        json3_expected = {
            "messageType": 1,
            "lab": 7,
            "variant": 1,
            "link": None,
            "code": "Artyom_Gusev"
        }

        jsonDates_expected = [json.dumps(json3_expected)]

        self.assertEqual(jsonDates_received, jsonDates_expected)

    def test_S_5_t3(self):
        """Код статус не равен 20"""

        # Создание студента
        student3 = global_User.User("Артём Гусев", "18-ИСбо-2", None, None)

        # Список писем
        letters = []

        # Создание письма в соответствии со сценарием
        letter = global_Letter.Letter(student3, "ЛР01", None, 1, 3)
        letter.Body = "Artyom_Gusev"
        letter.CodeStatus = "02"

        letters.append(letter)

        jsonDates_received = main_2_WorkWithLetters.FormJSONDates(letters)

        self.assertEqual(jsonDates_received, [])

if __name__ == '__main__':
    unittest.main()
    config_Project.logger.closelogfile()
