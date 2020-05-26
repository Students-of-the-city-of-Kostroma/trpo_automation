import unittest
import main_4_moderate_FormAnswers
import global_User
import global_LetterResult
import global_AnswersForUsers
import moderate_PatternsOfLetter


class test_MakeAnswersForUsers(unittest.TestCase):

    def test_S_7_t1(self):
        """В входных данных пустой список LettersResult"""

        # Создание входных данных
        LetterResult = []

        # Создание ожидаемого результата
        answers = []

        my_result = main_4_moderate_FormAnswers.MakeAnswersForUsers(LetterResult)

        self.assertEqual(my_result, answers)

    def test_S_7_t2(self):
        """Список LetterResult с кодами: ""00"", ""01"", ""02"", ""03"", ""04"", ""03"", ""04"",
""05"", ""06"", ""07"", ""08"", ""10"", ""30""."""

        # Создание входных данных
        us = global_User.User("Ельцов Андрей", "18-ИСбо-2б", "andreq64AhA@mail.ru", True)
        Letters = []
        let0 = global_LetterResult.LetterResult(us, True, '1', '1')
        let0.CodeStatus = '00'
        Letters.append(let0)
        let1 = global_LetterResult.LetterResult(us, True, '1', '1')
        let1.CodeStatus = '01'
        Letters.append(let1)
        let2 = global_LetterResult.LetterResult(us, True, '1', '1')
        let2.CodeStatus = '02'
        Letters.append(let2)
        let3 = global_LetterResult.LetterResult(us, True, '1', '1')
        let3.CodeStatus = '03'
        Letters.append(let3)
        let4 = global_LetterResult.LetterResult(us, True, '1', '1')
        let4.CodeStatus = '04'
        Letters.append(let4)
        let5 = global_LetterResult.LetterResult(us, True, '1', '1')
        let5.CodeStatus = '05'
        Letters.append(let5)
        let6 = global_LetterResult.LetterResult(us, True, '1', '1')
        let6.CodeStatus = '06'
        Letters.append(let6)
        let7 = global_LetterResult.LetterResult(us, True, '1', '1')
        let7.CodeStatus = '07'
        Letters.append(let7)
        let8 = global_LetterResult.LetterResult(us, True, '1', '1')
        let8.CodeStatus = '08'
        Letters.append(let8)
        let9 = global_LetterResult.LetterResult(us, True, '1', '1')
        let9.CodeStatus = '10'
        Letters.append(let9)
        let10 = global_LetterResult.LetterResult(us, True, '1', '1')
        let10.CodeStatus = '30'
        Letters.append(let10)

        # Создание ожидаемого результата
        answers = []
        pattern = moderate_PatternsOfLetter.UnknownUser()
        an0 = global_AnswersForUsers.AnswersForUsers("andreq64AhA@mail.ru", pattern.return_theme(),
                                                     pattern.return_body())
        answers.append(an0)
        pattern = moderate_PatternsOfLetter.UncorrectedTheme()
        an1 = global_AnswersForUsers.AnswersForUsers("andreq64AhA@mail.ru", pattern.return_theme(),
                                                     pattern.return_body())
        answers.append(an1)
        pattern = moderate_PatternsOfLetter.UncorrectedStructure()
        an2 = global_AnswersForUsers.AnswersForUsers("andreq64AhA@mail.ru", pattern.return_theme(),
                                                     pattern.return_body())
        answers.append(an2)
        pattern = moderate_PatternsOfLetter.UncorrectedVariant()
        an3 = global_AnswersForUsers.AnswersForUsers("andreq64AhA@mail.ru", pattern.return_theme(),
                                                     pattern.return_body())
        answers.append(an3)
        pattern = moderate_PatternsOfLetter.LostLinks()
        an4 = global_AnswersForUsers.AnswersForUsers("andreq64AhA@mail.ru", pattern.return_theme(),
                                                     pattern.return_body())
        answers.append(an4)
        pattern = moderate_PatternsOfLetter.HaveAttachments()
        an5 = global_AnswersForUsers.AnswersForUsers("andreq64AhA@mail.ru", pattern.return_theme(),
                                                     pattern.return_body())
        answers.append(an5)
        pattern = moderate_PatternsOfLetter.SystemFailure()
        an6 = global_AnswersForUsers.AnswersForUsers("andreq64AhA@mail.ru", pattern.return_theme(),
                                                     pattern.return_body())
        answers.append(an6)
        pattern = moderate_PatternsOfLetter.SystemFailure()
        an7 = global_AnswersForUsers.AnswersForUsers("andreq64AhA@mail.ru", pattern.return_theme(),
                                                     pattern.return_body())
        answers.append(an7)
        pattern = moderate_PatternsOfLetter.UncorrectedLink()
        an8 = global_AnswersForUsers.AnswersForUsers("andreq64AhA@mail.ru", pattern.return_theme(),
                                                     pattern.return_body())
        answers.append(an8)
        pattern = moderate_PatternsOfLetter.WorkCompleted()
        an9 = global_AnswersForUsers.AnswersForUsers("andreq64AhA@mail.ru", pattern.return_theme(),
                                                     pattern.return_body())
        answers.append(an9)
        pattern = moderate_PatternsOfLetter.WorkVerified(True)
        an10 = global_AnswersForUsers.AnswersForUsers("andreq64AhA@mail.ru", pattern.return_theme(),
                                                      pattern.return_body())
        answers.append(an10)
        par = ("Ельцов Андрей", '1', '1')
        forteacher = moderate_PatternsOfLetter.ForTeacher()
        forteacher.add(par)
        an11 = global_AnswersForUsers.AnswersForUsers("trpo.help@gmail.com", forteacher.return_theme(),
                                                      forteacher.return_body())
        answers.append(an11)

        my_result = main_4_moderate_FormAnswers.MakeAnswersForUsers(Letters)

        # Заполненый массив answers содержащие ответы, сответствующие своим кодам
        for i in range(len(answers)):
            self.assertEqual(my_result[i].Body, answers[i].Body)
            self.assertEqual(my_result[i].Theme, answers[i].Theme)  
            self.assertEqual(my_result[i].Who, answers[i].Who)

    def test_S_7_t3(self):
        """Список LettersResult с 1 пустым экземпляром"""

        # Создание входных данных
        us = global_User.User("Ельцов Андрей", "18-ИСбо-2б", "andreq64AhA@mail.ru", True)
        Letters = []
        let0 = global_LetterResult.LetterResult(us, True, '1', '1')
        let0.CodeStatus = '00'
        Letters.append(let0)
        let1 = global_LetterResult.LetterResult(us, True, '1', '1')
        let1.CodeStatus = '01'
        Letters.append(let1)
        let2 = global_LetterResult.LetterResult()
        Letters.append(let2)

        # Создание ожидаемого результата
        answers = []
        pattern = moderate_PatternsOfLetter.UnknownUser()
        an0 = global_AnswersForUsers.AnswersForUsers("andreq64AhA@mail.ru", pattern.return_theme(),
                                                     pattern.return_body())
        answers.append(an0)
        pattern = moderate_PatternsOfLetter.UncorrectedTheme()
        an1 = global_AnswersForUsers.AnswersForUsers("andreq64AhA@mail.ru", pattern.return_theme(),
                                                     pattern.return_body())
        answers.append(an1)

        my_result = main_4_moderate_FormAnswers.MakeAnswersForUsers(Letters)

        # Заполненый массив answers содержащие ответы сответствующие своим кода и меньше на 1 элемент чем LetterResult
        self.assertEqual(len(my_result), len(answers) - 1)

    def test_S_7_t4(self):
        """В списке LetterResult в поле IsOk, Student, NumberOfLab, VariantOfLab не заполнены"""

        # Создание входных данных
        Letters = []
        let0 = global_LetterResult.LetterResult()
        let0.CodeStatus = '00'
        Letters.append(let0)

        # Создание ожидаемого результата
        answers = []

        my_result = main_4_moderate_FormAnswers.MakeAnswersForUsers(Letters)

        # Пустой массив answers
        self.assertEqual(my_result, answers)


if __name__ == '__main__':
    unittest.main()