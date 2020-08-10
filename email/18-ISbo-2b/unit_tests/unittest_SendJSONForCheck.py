import unittest
import global_User as User
import global_Letter as Letter
import global_LetterResult as LetterResult
import json

import config_Project
import global_Logging

config_Project.logger = global_Logging.Logger()
i = config_Project.logger
config_Project.logger.createlogfile()

import main_2_WorkWithLetters


class TestSendJSONForCheck(unittest.TestCase):

    def test_S_5_t1(self):
        """Код статус не равен 20"""

        # Создание студента
        student = User.User("Максим Расторгуев", "18-ИСбо-2", None, None)

        # Создание письма
        letter = Letter.Letter(student, "ЛР01", "Max", 1, 1)

        # Заполнение полей письма
        letter.CodeStatus = "02"
        letter.CodeStatusComment = ""

        # Список готовых к проверке писем
        letters = []
        letters.append(letter)

        # Создание JSON-объекта
        json1 = {
            "messageType": 1,
            "lab": 1,
            "variant": 1,
            "link": None,
            "code": "Max"
        }

        mystr = json.dumps(json1)
        jsonDates = []
        jsonDates.append(mystr)

        # Список ожидаемых писем
        letters_expectation = main_2_WorkWithLetters.SendJSONForCheck(jsonDates, letters)

        # Ожидаемое письмо
        letterRes = LetterResult.LetterResult(student)

        # Заполнение ожидаемого письма
        letterRes.IsOK = False
        letterRes.VariantOfLab = 1
        letterRes.NumberOfLab = 1
        letterRes.CodeStatus = "02"
        letterRes.CodeStatusComment = ""

        # Проверка писем на значение поля IsOK
        self.assertEqual(letters_expectation[0].IsOK, letterRes.IsOK)

    def test_S_5_t2(self):
        """Сервер для проверки работы не доступен"""

        # Создание студента
        student = User.User("Максим Расторгуев", "18-ИСбо-2", None, None)

        # Создание письма
        letter = Letter.Letter(student, "ЛР01", "Max", 1, 2)

        # Заполнение полей письма
        letter.CodeStatus = "20"
        letter.CodeStatusComment = ""

        # Список готовых к проверке писем
        letters = []
        letters.append(letter)

        # Создание JSON-объекта
        json1 = {
            "messageType": 1,
            "lab": 1,
            "variant": 1,
            "link": None,
            "code": "Max"
        }

        mystr = json.dumps(json1)
        jsonDates = []
        jsonDates.append(mystr)

        # Список ожидаемых писем
        letters_expectation = main_2_WorkWithLetters.SendJSONForCheck(jsonDates, letters)

        # Ожидаемое письмо
        letterRes = LetterResult.LetterResult(student)

        # Заполнение ожидаемого письма
        letterRes.IsOK = False
        letterRes.VariantOfLab = 1
        letterRes.NumberOfLab = 2
        letterRes.CodeStatus = "06"
        letterRes.CodeStatusComment = ""

        # Проверка писем на значение поля CodeStatus
        self.assertEqual(letters_expectation[0].CodeStatus, letterRes.CodeStatus)

    def test_S_5_t3(self):
        """Сервер не отвечает в течение 10 секунд"""

        # Создание студента
        student = User.User("Максим Расторгуев", "18-ИСбо-2", None, None)

        # Создание письма
        letter = Letter.Letter(student, "ЛР01", "Max", 1, 3)

        # Заполнение полей письма
        letter.CodeStatus = "20"
        letter.CodeStatusComment = ""

        # Список готовых к проверке писем
        letters = []
        letters.append(letter)

        # Создание JSON-объекта
        json1 = {
            "messageType": 1,
            "lab": 1,
            "variant": 1,
            "link": None,
            "code": "Max"
        }

        mystr = json.dumps(json1)
        jsonDates = []
        jsonDates.append(mystr)

        # Список ожидаемых писем
        letters_expectation = main_2_WorkWithLetters.SendJSONForCheck(jsonDates, letters)

        # Ожидаемое письмо
        letterRes = LetterResult.LetterResult(student)

        # Заполнение ожидаемого письма
        letterRes.IsOK = False
        letterRes.VariantOfLab = 1
        letterRes.NumberOfLab = 3
        letterRes.CodeStatus = "06"
        letterRes.CodeStatusComment = ""

        # Проверка писем на значение поля CodeStatus
        self.assertEqual(letters_expectation[0].CodeStatus, letterRes.CodeStatus)

    def test_S_5_t4(self):
        """Ответ от сервера messageType == 2, grade == 1"""

        # Создание студента
        student = User.User("Максим Расторгуев", "18-ИСбо-2", None, None)

        # Создание письма
        letter = Letter.Letter(student, "ЛР01", "Max", 1, 1)

        # Заполнение полей письма
        letter.CodeStatus = "20"
        letter.CodeStatusComment = ""

        # Список готовых к проверке писем
        letters = []
        letters.append(letter)

        # Создание JSON-объекта
        json1 = {
            "messageType": 1,
            "lab": 1,
            "variant": 1,
            "link": None,
            "code": "Max"
        }

        mystr = json.dumps(json1)
        jsonDates = []
        jsonDates.append(mystr)

        # Список ожидаемых писем
        letters_expectation = main_2_WorkWithLetters.SendJSONForCheck(jsonDates, letters)

        # Ожидаемое письмо
        letterRes = LetterResult.LetterResult(student)

        # Заполнение ожидаемого письма
        letterRes.IsOK = True
        letterRes.VariantOfLab = 1
        letterRes.NumberOfLab = 1
        letterRes.CodeStatus = "30"
        letterRes.CodeStatusComment = ""

        # Проверка писем на значение поля IsOK
        self.assertEqual(letters_expectation[0].IsOK, letterRes.IsOK)

    def test_S_5_t5(self):
        """Ответ от сервера messageType == 2, grade == 0"""

        # Создание студента
        student = User.User("Максим Расторгуев", "18-ИСбо-2", None, None)

        # Создание письма
        letter = Letter.Letter(student, "ЛР01", "Max", 1, 3)

        # Заполнение полей письма
        letter.CodeStatus = "20"
        letter.CodeStatusComment = ""

        # Список готовых к проверке писем
        letters = []
        letters.append(letter)

        # Создание JSON-объекта
        json1 = {
            "messageType": 1,
            "lab": 1,
            "variant": 1,
            "link": None,
            "code": "Max"
        }

        mystr = json.dumps(json1)
        jsonDates = []
        jsonDates.append(mystr)

        # Список ожидаемых писем
        letters_expectation = main_2_WorkWithLetters.SendJSONForCheck(jsonDates, letters)

        # Ожидаемое письмо
        letterRes = LetterResult.LetterResult(student)

        # Заполнение ожидаемого письма
        letterRes.IsOK = False
        letterRes.VariantOfLab = 1
        letterRes.NumberOfLab = 1
        letterRes.CodeStatus = "30"
        letterRes.CodeStatusComment = ""

        # Проверка писем на значение поля IsOK
        self.assertEqual(letters_expectation[0].IsOK, letterRes.IsOK)

    def test_S_5_t6(self):
        """Ответ от сервера messageType == 3"""

        # Создание студента
        student = User.User("Максим Расторгуев", "18-ИСбо-2", None, None)

        # Создание письма
        letter = Letter.Letter(student, "ЛР01", "Max", 1, 4)

        # Заполнение полей письма
        letter.CodeStatus = "20"
        letter.CodeStatusComment = ""

        # Список готовых к проверке писем
        letters = []
        letters.append(letter)

        # Создание JSON-объекта
        json1 = {
            "messageType": 1,
            "lab": 1,
            "variant": 1,
            "link": None,
            "code": "Max"
        }

        mystr = json.dumps(json1)
        jsonDates = []
        jsonDates.append(mystr)

        # Список ожидаемых писем
        letters_expectation = main_2_WorkWithLetters.SendJSONForCheck(jsonDates, letters)

        # Ожидаемое письмо
        letterRes = LetterResult.LetterResult(student)

        # Заполнение ожидаемого письма
        letterRes.IsOK = False
        letterRes.VariantOfLab = 1
        letterRes.NumberOfLab = 1
        letterRes.CodeStatus = "07"
        letterRes.CodeStatusComment = ""

        # Проверка писем на значение поля CodeStatus
        self.assertEqual(letters_expectation[0].CodeStatus, letterRes.CodeStatus)

    def test_S_5_t7(self):
        """Ответ от сервера messageType == 4"""

        # Создание студента
        student = User.User("Максим Расторгуев", "18-ИСбо-2", None, None)

        # Создание письма
        letter = Letter.Letter(student, "ЛР01", "Max", 1, 5)

        # Заполнение полей письма
        letter.CodeStatus = "20"
        letter.CodeStatusComment = ""

        # Список готовых к проверке писем
        letters = []
        letters.append(letter)

        # Создание JSON-объекта
        json1 = {
            "messageType": 1,
            "lab": 1,
            "variant": 1,
            "link": None,
            "code": "Max"
        }

        mystr = json.dumps(json1)
        jsonDates = []
        jsonDates.append(mystr)

        # Список ожидаемых писем
        letters_expectation = main_2_WorkWithLetters.SendJSONForCheck(jsonDates, letters)

        # Ожидаемое письмо
        letterRes = LetterResult.LetterResult(student)

        # Заполнение ожидаемого письма
        letterRes.IsOK = False
        letterRes.VariantOfLab = 1
        letterRes.NumberOfLab = 1
        letterRes.CodeStatus = "06"
        letterRes.CodeStatusComment = ""

        # Проверка писем на значение поля CodeStatus
        self.assertEqual(letters_expectation[0].CodeStatus, letterRes.CodeStatus)

if __name__ == "__main__":
    unittest.main()
    config_Project.logger.closelogfile()
