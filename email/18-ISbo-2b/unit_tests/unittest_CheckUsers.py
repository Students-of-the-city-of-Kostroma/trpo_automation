import unittest
import global_User
import global_Letter
import main_1_google_CheckEmail

class MyTestCase(unittest.TestCase):
    def test_S_6_t1(self):
        """Данные о пользователе содержатся в таблице регистрации"""
        # Создание студента
        student = global_User.User(None, None, "modern.kostroma@gmail.com", None)

        # Создание письма
        letter = global_Letter.Letter(student, "ЛР03",
                                      """Здравствуйте
Выполнил работу. Прошу проверить. Ссылка на репозиторий https://github.com/Students-of-the-city-of-Kostroma/trpo_automation
--
Екатерина Калинина, 18-ИСбо-2б
""", None, None)

        # Добавление темы письма
        letter.ThemeOfLetter = "ТРПО ЛР03 ВАР1"

        # На вход приходит пустой CodeStatus
        letter.CodeStatus = ""

        letters = []
        letters.append(letter)
        main_1_google_CheckEmail.CheckUsers(letters)

        # Ожидаемые данные:
        student_expectation = global_User.User
        student_expectation.IsRegistered = True
        student_expectation.NameOfStudent = 'Калинина Екатерина Алексеевна'
        student_expectation.GroupOfStudent = '18-ИСбо-2б'

        self.assertEqual(letters[0].Student.NameOfStudent, student_expectation.NameOfStudent)

    def test_S_6_t2(self):
        """Данные о пользователе отсутствуют в таблице регистрации"""
        # Создание студента
        student = global_User.User(None, None, "test@gmail.com", None)

        # Создание письма
        letter = global_Letter.Letter(student, "ЛР03",
                                      """Здравствуйте
Выполнил работу. Прошу проверить. Ссылка на репозиторий https://github.com/Students-of-the-city-of-Kostroma/trpo_automation
--
Екатерина Калинина, 18-ИСбо-2б
""", None, None)

        # Добавление темы письма
        letter.ThemeOfLetter = "ТРПО ЛР03 ВАР1"

        # На вход приходит пустой CodeStatus
        letter.CodeStatus = ""

        letters = []
        letters.append(letter)
        main_1_google_CheckEmail.CheckUsers(letters)

        # Ожидаемые данные:
        letter_expectation = global_Letter.Letter(student, "ЛР03",
                                      """Здравствуйте
Выполнил работу. Прошу проверить. Ссылка на репозиторий https://github.com/Students-of-the-city-of-Kostroma/trpo_automation
--
Екатерина Калинина, 18-ИСбо-2б
""", None, None)
        letter_expectation.CodeStatus = "00"
        letter_expectation.CodeStatusComment = "Пользователь не зарегистрирован"

        self.assertEqual(letters[0].CodeStatusComment, letter_expectation.CodeStatusComment)

    def test_S_6_t3(self):
        """Данные не изменяются в результате выполнения функции"""
        # Создание студента
        student = global_User.User(None, None, "modern.kostroma@gmail.com", None)

        # Создание письма
        letter = global_Letter.Letter(student, "ЛР03",
                                      """Здравствуйте
Выполнил работу. Прошу проверить. Ссылка на репозиторий https://github.com/Students-of-the-city-of-Kostroma/trpo_automation
--
Екатерина Калинина, 18-ИСбо-2б
""", None, None)

        # Добавление темы письма
        letter.ThemeOfLetter = "ТРПО ЛР03 ВАР1"

        # На вход приходит пустой CodeStatus
        letter.CodeStatus = "05"

        letters = []
        letters.append(letter)
        main_1_google_CheckEmail.CheckUsers(letters)

        # Ожидаемые данные:
        letter_expectation = global_Letter.Letter(student, "ЛР03",
                                                  """Здравствуйте
            Выполнил работу. Прошу проверить. Ссылка на репозиторий https://github.com/Students-of-the-city-of-Kostroma/trpo_automation
            --
            Екатерина Калинина, 18-ИСбо-2б
            """, None, None)
        letter_expectation.CodeStatus = "05"
        letter_expectation.CodeStatusComment = ""

        self.assertEqual(letters[0].CodeStatus, letter_expectation.CodeStatus)

if __name__ == '__main__':
    unittest.main()
