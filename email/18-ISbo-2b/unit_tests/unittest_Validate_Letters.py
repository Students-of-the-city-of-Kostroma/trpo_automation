import unittest
import main_1_CheckEmail
import global_Letter
import  global_User

class test_Validate_Letters(unittest.TestCase):
    def test_S_2_t1(self):
        """Проверка корректного письма"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", None, None)

        # Создание письма
        letter = global_Letter.Letter(student, "ЛР03",
                                      """Здравствуйте
Выполнил работу. Прошу проверить. Ссылка на репозиторий https://github.com/Students-of-the-city-of-Kostroma/trpo_automation
--
Артём Гусев, 18-ИСбо-2б
""", None, None)
        letter.ThemeOfLetter = "ТРПО ЛР03 ВАР1"

        letters = []
        letters.append(letter)

        letter_Res =  global_Letter.Letter(student, "ЛР03", "https://github.com/Students-of-the-city-of-Kostroma/trpo_automation", None, None)
        letter_Res.CodeStatus = "20"
        letter_Res.CodeStatusComment = "Работа отправлена на проверку"
        letter_Res.NumberOfLab = 3
        letter_Res.VariantOfLab = 1

        main_1_CheckEmail.ValidateLetters(letters)

        self.assertEqual(letters[0].NumberOfLab, letter_Res.NumberOfLab)

    def test_S_2_t2(self):
        """В теме отсутствует шифр дисциплины"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", None, None)

        # Создание письма
        letter = global_Letter.Letter(student, "ЛР03",
                                      """Здравствуйте
Выполнил работу. Прошу проверить. Ссылка на репозиторий https://github.com/Students-of-the-city-of-Kostroma/trpo_automation
--
Артём Гусев, 18-ИСбо-2б
""", None, None)
        letter.ThemeOfLetter = "ЛР03 ВАР1"

        letters = []
        letters.append(letter)

        letter_Res = global_Letter.Letter(student, "ЛР03",
                                          "https://github.com/Students-of-the-city-of-Kostroma/trpo_automation", None,
                                          None)
        letter_Res.CodeStatus = "01"
        letter_Res.CodeStatusComment = "Тема письма не соответствует требованиям к теме"
        letter_Res.NumberOfLab = 3
        letter_Res.VariantOfLab = 1

        main_1_CheckEmail.ValidateLetters(letters)

        self.assertEqual(letters[0].CodeStatusComment, letter_Res.CodeStatusComment)

    def test_S_2_t3(self):
        """В теме отсутствует шифр ЛР """

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", None, None)

        # Создание письма
        letter = global_Letter.Letter(student, "ЛР03",
                                      """Здравствуйте
Выполнил работу. Прошу проверить. Ссылка на репозиторий https://github.com/Students-of-the-city-of-Kostroma/trpo_automation
--
Артём Гусев, 18-ИСбо-2б
""", None, None)
        letter.ThemeOfLetter = "ТРПО 03 ВАР1"

        letters = []
        letters.append(letter)

        letter_Res = global_Letter.Letter(student, "ЛР03",
                                          "https://github.com/Students-of-the-city-of-Kostroma/trpo_automation", None,
                                          None)
        letter_Res.CodeStatus = "01"
        letter_Res.CodeStatusComment = "Тема письма не соответствует требованиям к теме"
        letter_Res.NumberOfLab = 3
        letter_Res.VariantOfLab = 1

        main_1_CheckEmail.ValidateLetters(letters)

        self.assertEqual(letters[0].CodeStatusComment, letter_Res.CodeStatusComment)

    def test_S_2_t4(self):
        """В теме отсутствует шифр ВАР"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", None, None)

        # Создание письма
        letter = global_Letter.Letter(student, "ЛР03",
                                      """Здравствуйте
Выполнил работу. Прошу проверить. Ссылка на репозиторий https://github.com/Students-of-the-city-of-Kostroma/trpo_automation
--
Артём Гусев, 18-ИСбо-2б
""", None, None)
        letter.ThemeOfLetter = "ТРПО ЛР03"

        letters = []
        letters.append(letter)

        letter_Res = global_Letter.Letter(student, "ЛР03",
                                          "https://github.com/Students-of-the-city-of-Kostroma/trpo_automation", None,
                                          None)
        letter_Res.CodeStatus = "01"
        letter_Res.CodeStatusComment = "Тема письма не соответствует требованиям к теме"
        letter_Res.NumberOfLab = 3
        letter_Res.VariantOfLab = 1

        main_1_CheckEmail.ValidateLetters(letters)

        self.assertEqual(letters[0].CodeStatusComment, letter_Res.CodeStatusComment)

    def test_S_2_t5(self):
        """В теме не указан номер лабораторной работы"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", None, None)

        # Создание письма
        letter = global_Letter.Letter(student, "ЛР03",
                                      """Здравствуйте
Выполнил работу. Прошу проверить. Ссылка на репозиторий https://github.com/Students-of-the-city-of-Kostroma/trpo_automation
--
Артём Гусев, 18-ИСбо-2б
""", None, None)
        letter.ThemeOfLetter = "ТРПО ЛР ВАР3"

        letters = []
        letters.append(letter)

        letter_Res =  global_Letter.Letter(student, "ЛР03", "https://github.com/Students-of-the-city-of-Kostroma/trpo_automation", None, None)
        letter_Res.CodeStatus = "03"
        letter_Res.CodeStatusComment = "Неверно указан номер работы или варианта"
        letter_Res.NumberOfLab = 3
        letter_Res.VariantOfLab = 1

        main_1_CheckEmail.ValidateLetters(letters)

        self.assertEqual(letters[0].CodeStatusComment, letter_Res.CodeStatusComment)

    def test_S_2_t6(self):
        """В теме не указан вариант лабораторной работы"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", None, None)

        # Создание письма
        letter = global_Letter.Letter(student, "ЛР03",
                                      """Здравствуйте
Выполнил работу. Прошу проверить. Ссылка на репозиторий https://github.com/Students-of-the-city-of-Kostroma/trpo_automation
--
Артём Гусев, 18-ИСбо-2б
""", None, None)
        letter.ThemeOfLetter = "ТРПО ЛР03 ВАР"

        letters = []
        letters.append(letter)

        letter_Res =  global_Letter.Letter(student, "ЛР03", "https://github.com/Students-of-the-city-of-Kostroma/trpo_automation", None, None)
        letter_Res.CodeStatus = "03"
        letter_Res.CodeStatusComment = "Неверно указан номер работы или варианта"
        letter_Res.NumberOfLab = 3
        letter_Res.VariantOfLab = 1

        main_1_CheckEmail.ValidateLetters(letters)

        self.assertEqual(letters[0].CodeStatusComment, letter_Res.CodeStatusComment)

    def test_S_2_t7(self):
        """Номер лабораторной: |x| > 15 или |x| < 1"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", None, None)

        # Создание письма
        letter = global_Letter.Letter(student, "ЛР03",
                                      """Здравствуйте
Выполнил работу. Прошу проверить. Ссылка на репозиторий https://github.com/Students-of-the-city-of-Kostroma/trpo_automation
--
Артём Гусев, 18-ИСбо-2б
""", None, None)
        letter.ThemeOfLetter = "ТРПО ЛР15 ВАР01"

        letters = []
        letters.append(letter)

        letter_Res =  global_Letter.Letter(student, "ЛР03", "https://github.com/Students-of-the-city-of-Kostroma/trpo_automation", None, None)
        letter_Res.CodeStatus = "03"
        letter_Res.CodeStatusComment = "Неверно указан номер работы или варианта"
        letter_Res.NumberOfLab = 3
        letter_Res.VariantOfLab = 1

        main_1_CheckEmail.ValidateLetters(letters)

        self.assertEqual(letters[0].CodeStatusComment, letter_Res.CodeStatusComment)

    def test_S_2_t8(self):
        """Номер варианта: |x| > 15 или |x| < 1"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", None, None)

        # Создание письма
        letter = global_Letter.Letter(student, "ЛР03",
                                      """Здравствуйте
Выполнил работу. Прошу проверить. Ссылка на репозиторий https://github.com/Students-of-the-city-of-Kostroma/trpo_automation
--
Артём Гусев, 18-ИСбо-2б
""", None, None)
        letter.ThemeOfLetter = "ТРПО ЛР03 ВАР99"

        letters = []
        letters.append(letter)

        letter_Res =  global_Letter.Letter(student, "ЛР03", "https://github.com/Students-of-the-city-of-Kostroma/trpo_automation", None, None)
        letter_Res.CodeStatus = "03"
        letter_Res.CodeStatusComment = "Неверно указан номер работы или варианта"
        letter_Res.NumberOfLab = 3
        letter_Res.VariantOfLab = 1

        main_1_CheckEmail.ValidateLetters(letters)

        self.assertEqual(letters[0].CodeStatusComment, letter_Res.CodeStatusComment)

    def test_S_2_t9(self):
        """В теле отсутсвует приветствие"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", None, None)

        # Создание письма
        letter = global_Letter.Letter(student, "ЛР03",
                                      """
Выполнил работу. Прошу проверить. Ссылка на репозиторий https://github.com/Students-of-the-city-of-Kostroma/trpo_automation
--
Артём Гусев, 18-ИСбо-2б
""", None, None)
        letter.ThemeOfLetter = "ТРПО ЛР03 ВАР1"

        letters = []
        letters.append(letter)

        letter_Res =  global_Letter.Letter(student, "ЛР03", "https://github.com/Students-of-the-city-of-Kostroma/trpo_automation", None, None)
        letter_Res.CodeStatus = "02"
        letter_Res.CodeStatusComment = "Структура письма не соответствует требованиям к оформлению"
        letter_Res.NumberOfLab = 3
        letter_Res.VariantOfLab = 1

        main_1_CheckEmail.ValidateLetters(letters)

        self.assertEqual(letters[0].CodeStatusComment, letter_Res.CodeStatusComment)

    def test_S_2_t10(self):
        """Приветствие в теле не по форме"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", None, None)

        # Создание письма
        letter = global_Letter.Letter(student, "ЛР03",
                                      """Здарова бот
Выполнил работу. Прошу проверить. Ссылка на репозиторий https://github.com/Students-of-the-city-of-Kostroma/trpo_automation
--
Артём Гусев, 18-ИСбо-2б
""", None, None)
        letter.ThemeOfLetter = "ТРПО ЛР03 ВАР1"

        letters = []
        letters.append(letter)

        letter_Res =  global_Letter.Letter(student, "ЛР03", "https://github.com/Students-of-the-city-of-Kostroma/trpo_automation", None, None)
        letter_Res.CodeStatus = "02"
        letter_Res.CodeStatusComment = "Структура письма не соответствует требованиям к оформлению"
        letter_Res.NumberOfLab = 3
        letter_Res.VariantOfLab = 1

        main_1_CheckEmail.ValidateLetters(letters)

        self.assertEqual(letters[0].CodeStatusComment, letter_Res.CodeStatusComment)

    def test_S_2_t11(self):
        """В теле нет ссылки"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", None, None)

        # Создание письма
        letter = global_Letter.Letter(student, "ЛР03",
                                      """Здравствуйте
Выполнил работу. Прошу проверить. Ссылка на репозиторий 
--
Артём Гусев, 18-ИСбо-2б
""", None, None)
        letter.ThemeOfLetter = "ТРПО ЛР03 ВАР1"

        letters = []
        letters.append(letter)

        letter_Res =  global_Letter.Letter(student, "ЛР03", "", None, None)
        letter_Res.CodeStatus = "04"
        letter_Res.CodeStatusComment = "Письмо не содержит необходимых ссылок на ресурсы."
        letter_Res.NumberOfLab = 3
        letter_Res.VariantOfLab = 1

        main_1_CheckEmail.ValidateLetters(letters)

        self.assertEqual(letters[0].CodeStatusComment, letter_Res.CodeStatusComment)

    def test_S_2_t12(self):
        """В теле нет ссылки"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", None, None)

        # Создание письма
        letter = global_Letter.Letter(student, "ЛР03",
                                      """Здравствуйте
Выполнил работу. Прошу проверить. Ссылка на репозиторий 
--
Артём Гусев, 18-ИСбо-2б
""", None, None)
        letter.ThemeOfLetter = "ТРПО ЛР03 ВАР1"

        letters = []
        letters.append(letter)

        letter_Res =  global_Letter.Letter(student, "ЛР03", "", None, None)
        letter_Res.CodeStatus = "04"
        letter_Res.CodeStatusComment = "Письмо не содержит необходимых ссылок на ресурсы."
        letter_Res.NumberOfLab = 3
        letter_Res.VariantOfLab = 1

        main_1_CheckEmail.ValidateLetters(letters)

        self.assertEqual(letters[0].CodeStatusComment, letter_Res.CodeStatusComment)

    def test_S_2_t13(self):
        """В теле отсутствет подпись"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", None, None)

        # Создание письма
        letter = global_Letter.Letter(student, "ЛР03",
                                      """Здравствуйте
Выполнил работу. Прошу проверить. Ссылка на репозиторий https://github.com/Students-of-the-city-of-Kostroma/trpo_automation
--
Артём
""", None, None)
        letter.ThemeOfLetter = "ТРПО ЛР03 ВАР1"

        letters = []
        letters.append(letter)

        letter_Res =  global_Letter.Letter(student, "ЛР03", "https://github.com/Students-of-the-city-of-Kostroma/trpo_automation", None, None)
        letter_Res.CodeStatus = "02"
        letter_Res.CodeStatusComment = "Структура письма не соответствует требованиям к оформлению"
        letter_Res.NumberOfLab = 3
        letter_Res.VariantOfLab = 1

        main_1_CheckEmail.ValidateLetters(letters)

        self.assertEqual(letters[0].CodeStatusComment, letter_Res.CodeStatusComment)

    def test_S_2_t14(self):
        """Подпись не соответствует указанной в полях User.Name \ User.Group"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", None, None)

        # Создание письма
        letter = global_Letter.Letter(student, "ЛР03",
                                      """Здравствуйте
Выполнил работу. Прошу проверить. Ссылка на репозиторий https://github.com/Students-of-the-city-of-Kostroma/trpo_automation
--
Артём Гусев, 18-ИСбо-2а
""", None, None)
        letter.ThemeOfLetter = "ТРПО ЛР03 ВАР1"

        letters = []
        letters.append(letter)

        letter_Res =  global_Letter.Letter(student, "ЛР03", "https://github.com/Students-of-the-city-of-Kostroma/trpo_automation", None, None)
        letter_Res.CodeStatus = "02"
        letter_Res.CodeStatusComment = "Подпись не соответствует заявленной при регистрации"
        letter_Res.NumberOfLab = 3
        letter_Res.VariantOfLab = 1

        main_1_CheckEmail.ValidateLetters(letters)

        self.assertEqual(letters[0].CodeStatusComment, letter_Res.CodeStatusComment)

if __name__ == '__main__':
    unittest.main()
