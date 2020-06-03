# coding=utf-8
import unittest
import global_User as User
import global_Letter as Letter
from main_2_base_WorkWithLetters import LettersConvertToString


class MyTestCase(unittest.TestCase):
    def test_S_4_t1(self):
        """Тест на ситуацию: Код статус не равен 20"""

        # Входные данные
        student = User.User("Валерий Бублин", "18-ИСбо-2", None, None)
        letters = []
        letter = Letter.Letter(student, "ЛР01", "https://github.com/Students-of-the-city-of-Kostroma/TasksOfStudents"
                                                "/tree/master/18-%D0%98%D0%A1%D0%B1%D0%BE-2/%D0%9B%D0%A001", None, 4)
        letter.CodeStatus = "08"
        letters.append(letter)
        letters = LettersConvertToString(letters)

        # Правильные данные
        student_true = User.User("Валерий Бублин", "18-ИСбо-2", None, None)
        letter_true = Letter.Letter(student_true, "ЛР01", "https://github.com/Students-of-the-city-of-Kostroma"
                                                          "/TasksOfStudents/tree/master/18-%D0%98%D0%A1%D0%B1%D0%BE-2"
                                                          "/%D0%9B%D0%A001", None, 4)
        letters_true = [letter_true]
        self.assertEqual(letters[0].Body, letters_true[0].Body)

    def test_S_4_t2(self):
        """Тест на ситуацию: Письмо с номером лабораторной, не требующей вытаскивание кода"""

        # Входные данные
        student = User.User("Валерий Бублин", "18-ИСбо-2", None, None)
        letters = []
        letter = Letter.Letter(student, "ЛР01",
                               "https://github.com/Students-of-the-city-of-Kostroma/TasksOfStudents/tree/master/18"
                               "-%D0%98%D0%A1%D0%B1%D0%BE-2/%D0%9B%D0%A001",
                               None, 1)
        letters.append(letter)
        letters = LettersConvertToString(letters)

        # Правильные данные
        student_true = User.User("Валерий Бублин", "18-ИСбо-2", None, None)
        letter_true = Letter.Letter(student_true, "ЛР01",
                                    "https://github.com/Students-of-the-city-of-Kostroma/TasksOfStudents/tree/master"
                                    "/18-%D0%98%D0%A1%D0%B1%D0%BE-2/%D0%9B%D0%A001",
                                    None, 1)
        letters_true = [letter_true]
        self.assertEqual(letters[0].Body, letters_true[0].Body)

    def test_S_4_t3(self):
        """Тест на ситуацию: Проверка корректного письма"""

        # Входные данные
        student = User.User("Валерий Бублин", "18-ИСбо-2", None, None)
        letters = []
        letter = Letter.Letter(student, "ЛР01", "https://github.com/Students-of-the-city-of-Kostroma/TasksOfStudents"
                                                "/tree/master/18-%D0%98%D0%A1%D0%B1%D0%BE-2/%D0%9B%D0%A001", None, 4)
        letter.CodeStatus = "20"
        letters.append(letter)
        letters = LettersConvertToString(letters)

        # Правильные данные
        student_true = User.User("Валерий Бублин", "18-ИСбо-2", None, None)
        letter_true = Letter.Letter(student_true, "ЛР01", "https://github.com/Students-of-the-city-of-Kostroma"
                                                          "/TasksOfStudents/tree/master/18-%D0%98%D0%A1%D0%B1%D0%BE-2"
                                                          "/%D0%9B%D0%A001",
                                    None, 4)
        letter_true.Body = "Всем привет от Бубли"
        letters_true = [letter_true]
        self.assertEqual(letters[0].Body, letters_true[0].Body)

    def test_S_4_t4(self):
        """Тест на ситуацию: Проверка письма с ссылкой не на ту папку( с другой лабораторной)"""

        # Входные данные
        student = User.User("Валерий Бублин", "18-ИСбо-2", None, None)
        letters = []
        letter = Letter.Letter(student, "ЛР01",
                               "https://github.com/Students-of-the-city-of-Kostroma/TasksOfStudents/tree/master/18"
                               "-%D0%98%D0%A1%D0%B1%D0%BE-2/%D0%9B%D0%A002",
                               None, 4)
        letter.CodeStatus = "20"
        letters.append(letter)
        letters = LettersConvertToString(letters)

        # Правильные данные
        student_true = User.User("Валерий Бублин", "18-ИСбо-2", None, None)
        letter_true = Letter.Letter(student_true, "ЛР01",
                                    "https://github.com/Students-of-the-city-of-Kostroma/TasksOfStudents/tree/master"
                                    "/18-%D0%98%D0%A1%D0%B1%D0%BE-2/%D0%9B%D0%A002",
                                    None, 4)
        letter_true.Body = "https://github.com/Students-of-the-city-of-Kostroma/TasksOfStudents/tree/master/18-%D0%98" \
                           "%D0%A1%D0%B1%D0%BE-2/%D0%9B%D0%A002 "
        letters_true = [letter_true]
        self.assertEqual(letters[0].Body, letters_true[0].Body)

    def test_S_4_t5(self):
        """Тест на ситуацию: Проверка письма в Body ссылка некорректна"""

        # Входные данные
        student = User.User("Валерий Бублин", "18-ИСбо-2", None, None)
        letters = []
        letter = Letter.Letter(student, "ЛР01", "https://www.youtube.com/watch?v=b5hM5nydmXU&t=2566s", None, 4)
        letter.CodeStatus = "20"
        letters.append(letter)
        letters = LettersConvertToString(letters)

        # Правильные данные
        student_true = User.User("Валерий Бублин", "18-ИСбо-2", None, None)
        letter_true = Letter.Letter(student_true, "ЛР01", "https://www.youtube.com/watch?v=b5hM5nydmXU&t=2566s", None,
                                    4)
        letter_true.Body = ""
        letter_true.CodeStatus = "08"
        letters_true = [letter_true]
        self.assertEqual(letters[0].CodeStatus, letters_true[0].CodeStatus)

    def test_S_4_t6(self):
        """Тест на ситуацию: Проверка письма с пустым полем Body"""

        # Входные данные
        student = User.User("Валерий Бублин", "18-ИСбо-2", None, None)
        letters = []
        letter = Letter.Letter(student, "ЛР01", "", None, 4)
        letter.CodeStatus = "20"
        letters.append(letter)
        letters = LettersConvertToString(letters)

        # Правильные данные
        student_true = User.User("Валерий Бублин", "18-ИСбо-2", None, None)
        letter_true = Letter.Letter(student_true, "ЛР01", "", None, 4)
        letter_true.Body = ""
        letter_true.CodeStatus = "08"
        letters_true = [letter_true]
        self.assertEqual(letters[0].CodeStatus, letters_true[0].CodeStatus)


if __name__ == '__main__':
    unittest.main()
