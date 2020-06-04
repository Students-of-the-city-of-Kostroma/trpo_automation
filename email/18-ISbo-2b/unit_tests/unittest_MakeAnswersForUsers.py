import unittest
import global_LetterResult
import  global_User
import main_4_FormAnswers
import global_AnswersForUsers

class MyTestCase(unittest.TestCase):
    def test_S_8_t1(self):
        """Пользователь отсутствует в журнале"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", "test@yandex.ru", None)

        # Создание письма
        letterResult = global_LetterResult.LetterResult(student, False, None, None)
        letterResult.CodeStatus = "00"

        # Список писем
        letter = []
        letter.append(letterResult)

        # Список писем для отправки на почту
        answer = main_4_FormAnswers.MakeAnswersForUsers(letter)

        # Ожидаемое письмо
        answer_Res = global_AnswersForUsers.AnswersForUsers()
        answer_Res.Who = student.Email
        answer_Res.Theme = "Пользователь не найден."
        answer_Res.Body = "Ваше письмо было получено, но вас нет в журнале учащихся. Пожалуйста, заполните форму\n" \
               "для вашей регистрации в журнале учащихся и отправьте письмо повторно.\n" \
               "Без этого вы не сможете сдать свои работы дистанционно.\n\n" \
               "Форма: ссылка на форму регистрации .\n"

        self.assertEqual(answer[0].Theme, answer_Res.Theme)

    def test_S_8_t2(self):
        """Неправильная тема письма"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", "artemgusev200071@yandex.ru", None)

        # Создание письма
        letterResult = global_LetterResult.LetterResult(student, False, None, None)
        letterResult.CodeStatus = "01"

        # Список писем
        letter = []
        letter.append(letterResult)

        # Список писем для отправки на почту
        answer = main_4_FormAnswers.MakeAnswersForUsers(letter)

        # Ожидаемое письмо
        answer_Res = global_AnswersForUsers.AnswersForUsers()
        answer_Res.Who = student.Email
        answer_Res.Theme = "Задание с таким названием не существует."
        answer_Res.Body = "Ваше письмо было получено, но вы неверно указали тему. Возможно, это случилось из-за того, что вы \n" \
               "неверно указали номер или название. Поэтому пожалуйста, убедитесь, что номер задания соответствует \n" \
               "заданию и вы правильно указали название задание. После можете отправить письмо повторно.\n"

        self.assertEqual(answer[0].Theme, answer_Res.Theme)

    def test_S_8_t3(self):
        """Письмо не соответствует требованиям к оформлению письма."""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", "artemgusev200071@yandex.ru", None)

        # Создание письма
        letterResult = global_LetterResult.LetterResult(student, False, None, None)
        letterResult.CodeStatus = "02"

        # Список писем
        letter = []
        letter.append(letterResult)

        # Список писем для отправки на почту
        answer = main_4_FormAnswers.MakeAnswersForUsers(letter)

        # Ожидаемое письмо
        answer_Res = global_AnswersForUsers.AnswersForUsers()
        answer_Res.Who = student.Email
        answer_Res.Theme =  "Ваше письмо не соответствует требованиям к оформлению письма."
        answer_Res.Body = "Ваше письмо было получено, но письмо не соответствует требованиям. Возможно, это случилось из-за \n" \
               "того, что вы пользуетесь нашей системой впервые и не были ознакомлены с требованиями к оформлению \n" \
               "писем. Пожалуйста, прочитайте правила оформления писем и проверьте, что вы могли забыть\n" \
               "при написании письма.\n"

        self.assertEqual(answer[0].Theme, answer_Res.Theme)

    def test_S_8_t4(self):
        """В письме неверно указан вариант работы."""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", "artemgusev200071@yandex.ru", None)

        # Создание письма
        letterResult = global_LetterResult.LetterResult(student, False, None, None)
        letterResult.CodeStatus = "03"

        # Список писем
        letter = []
        letter.append(letterResult)

        # Список писем для отправки на почту
        answer = main_4_FormAnswers.MakeAnswersForUsers(letter)

        # Ожидаемое письмо
        answer_Res = global_AnswersForUsers.AnswersForUsers()
        answer_Res.Who = student.Email
        answer_Res.Theme = "В письме неверно указан вариант работы."
        answer_Res.Body = "Ваше письмо было получено, но в письме неверно указан номер варианта. Проверьте, что вы верно \n" \
               "указали свой вариант. Вариант должен входить в диапазон от 1 до 15 и содержит только цифры. \n"

        self.assertEqual(answer[0].Theme, answer_Res.Theme)

    def test_S_8_t5(self):
        """В письме отстуствует необходимая ссылка"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", "artemgusev200071@yandex.ru", None)

        # Создание письма
        letterResult = global_LetterResult.LetterResult(student, False, None, None)
        letterResult.CodeStatus = "04"

        # Список писем
        letter = []
        letter.append(letterResult)

        # Список писем для отправки на почту
        answer = main_4_FormAnswers.MakeAnswersForUsers(letter)

        # Ожидаемое письмо
        answer_Res = global_AnswersForUsers.AnswersForUsers()
        answer_Res.Who = student.Email
        answer_Res.Theme =  "В письме нет необходимых ссылок."
        answer_Res.Body = "Ваше письмо было получено, но в письме не хватает требуемых ссылок. \n" \
               "Проверьте, добавили все необходимые ссылки, и отправьте письмо повторно.\n"

        self.assertEqual(answer[0].Theme, answer_Res.Theme)

    def test_S_8_t6(self):
        """В письме есть вложения(картинки и иные файлы)"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", "artemgusev200071@yandex.ru", None)

        # Создание письма
        letterResult = global_LetterResult.LetterResult(student, False, None, None)
        letterResult.CodeStatus = "05"

        # Список писем
        letter = []
        letter.append(letterResult)

        # Список писем для отправки на почту
        answer = main_4_FormAnswers.MakeAnswersForUsers(letter)

        # Ожидаемое письмо
        answer_Res = global_AnswersForUsers.AnswersForUsers()
        answer_Res.Who = student.Email
        answer_Res.Theme = "В письме есть вложения."
        answer_Res.Body = "Ваше письмо было получено, но в письме есть вложений. Проверьте, что удалили все вложения, \n" \
               "заменив их на ссылки, и отправьте письмо повторно.\n"

        self.assertEqual(answer[0].Theme, answer_Res.Theme)

    def test_S_8_t7(self):
        """Модуль проверки писем отрабатывает некорректно"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", "artemgusev200071@yandex.ru", None)

        # Создание письма
        letterResult = global_LetterResult.LetterResult(student, False, None, None)
        letterResult.CodeStatus = "06"

        # Список писем
        letter = []
        letter.append(letterResult)

        # Список писем для отправки на почту
        answer = main_4_FormAnswers.MakeAnswersForUsers(letter)

        # Ожидаемое письмо
        answer_Res = global_AnswersForUsers.AnswersForUsers()
        answer_Res.Who = student.Email
        answer_Res.Theme =  "Система временно недоступна."
        answer_Res.Body = "Извините, но в данный момент система не может проверить вашу работу. Поэтому, пожалуйста, немного \n" \
               "подождите и отправьте письмо повторно.\n"

        self.assertEqual(answer[0].Theme, answer_Res.Theme)

    def test_S_8_t8(self):
        """Модуль приёма писем отрабатывает некорректно"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", "artemgusev200071@yandex.ru", None)

        # Создание письма
        letterResult = global_LetterResult.LetterResult(student, False, None, None)
        letterResult.CodeStatus = "07"

        # Список писем
        letter = []
        letter.append(letterResult)

        # Список писем для отправки на почту
        answer = main_4_FormAnswers.MakeAnswersForUsers(letter)

        # Ожидаемое письмо
        answer_Res = global_AnswersForUsers.AnswersForUsers()
        answer_Res.Who = student.Email
        answer_Res.Theme = "Система временно недоступна."
        answer_Res.Body = "Извините, но в данный момент система не может проверить вашу работу. Поэтому, пожалуйста, немного \n" \
               "подождите и отправьте письмо повторно.\n"

        self.assertEqual(answer[0].Theme, answer_Res.Theme)

    def test_S_8_t9(self):
        """В письме нерабочая ссылка, отсутствует файл или имеет неправильное имя"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", "artemgusev200071@yandex.ru", None)

        # Создание письма
        letterResult = global_LetterResult.LetterResult(student, False, None, None)
        letterResult.CodeStatus = "08"

        # Список писем
        letter = []
        letter.append(letterResult)

        # Список писем для отправки на почту
        answer = main_4_FormAnswers.MakeAnswersForUsers(letter)

        # Ожидаемое письмо
        answer_Res = global_AnswersForUsers.AnswersForUsers()
        answer_Res.Who = student.Email
        answer_Res.Theme = "В письме нерабочая ссылка."
        answer_Res.Body = "Ваше письмо было получено, но ссылка на ресурсы в письме нерабочая. Проверьте, что вы верно \n" \
                "указали ссылку. Возможно, была допущена ошибка или ссылка уже не действительна.\n"

        self.assertEqual(answer[0].Theme, answer_Res.Theme)

    def test_S_8_t10(self):
        """Модуль приёма писем отрабатывает некорректно"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", "artemgusev200071@yandex.ru", None)

        # Создание письма
        letterResult = global_LetterResult.LetterResult(student, False, None, None)
        letterResult.CodeStatus = "10"

        # Список писем
        letter = []
        letter.append(letterResult)

        # Список писем для отправки на почту
        answer = main_4_FormAnswers.MakeAnswersForUsers(letter)

        # Ожидаемое письмо
        answer_Res = global_AnswersForUsers.AnswersForUsers()
        answer_Res.Who = student.Email
        answer_Res.Theme = "Ваша работа уже была проверена."
        answer_Res.Body ="Ваша работа уже прошла проверку и зачтена, поэтому вам не надо больше отправлять на проверку.\n"

        self.assertEqual(answer[0].Theme, answer_Res.Theme)

    def test_S_8_t11(self):
        """Работа проверена и зачтена"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", "artemgusev200071@yandex.ru", None)

        # Создание письма
        letterResult = global_LetterResult.LetterResult(student, True, None, None)
        letterResult.CodeStatus = "30"
        letterResult.CodeStatusComment = ""
        # Список писем
        letter = []
        letter.append(letterResult)

        # Список писем для отправки на почту
        answer = main_4_FormAnswers.MakeAnswersForUsers(letter)

        # Ожидаемое письмо
        answer_Res1 = global_AnswersForUsers.AnswersForUsers()
        answer_Res1.Who = student.Email
        answer_Res1.Theme = "Ваша работа проверена."
        answer_Res1.Body = "Ваша работа проверена, оценка: зачтено. Если ваша работа \n" \
               "не зачтена, вы можете отправить работу на проверку повторно, после исправлений ошибок. \n"

        answer_Res2 = global_AnswersForUsers.AnswersForUsers()
        answer_Res2.Who = "trpo.help@gmail.com"
        answer_Res2.Theme = "Данные в журнале были изменены."
        answer_Res2.Body = "Артём Гусев сдал Работу номер 1 2"

        self.assertEqual(answer[0].Theme, answer_Res1.Theme)
        self.assertEqual(answer[1].Theme, answer_Res2.Theme)

    def test_S_8_t12(self):
        """Работа проверена и не зачтена"""

        # Создание студента
        student = global_User.User("Артём Гусев", "18-ИСбо-2б", "artemgusev200071@yandex.ru", None)

        # Создание письма
        letterResult = global_LetterResult.LetterResult(student, False, None, None)
        letterResult.CodeStatus = "30"
        letterResult.CodeStatusComment = ""
        # Список писем
        letter = []
        letter.append(letterResult)

        # Список писем для отправки на почту
        answer = main_4_FormAnswers.MakeAnswersForUsers(letter)

        # Ожидаемое письмо
        answer_Res1 = global_AnswersForUsers.AnswersForUsers()
        answer_Res1.Who = student.Email
        answer_Res1.Theme = "Ваша работа проверена."
        answer_Res1.Body = "Ваша работа проверена, оценка: не зачтено. Ответ от проверяющего модуля был таким: \n " \
                            + "" + "\n" \
                            "Если ваша работа не зачтена, вы можете отправить работу на проверку повторно, после исправлений ошибок. \n"

        answer_Res2 = global_AnswersForUsers.AnswersForUsers()
        answer_Res2.Who = "trpo.help@gmail.com"
        answer_Res2.Theme = "Данные в журнале были изменены."
        answer_Res2.Body = "Артём Гусев сдал Работу номер 1 2"

        self.assertEqual(answer[0].Theme, answer_Res1.Theme)
if __name__ == '__main__':
    unittest.main()
