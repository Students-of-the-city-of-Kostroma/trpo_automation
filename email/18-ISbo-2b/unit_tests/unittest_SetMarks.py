from main_3_SetResults import SetMarks
from global_User import User
from global_LetterResult import LetterResult
import unittest


class test_SetMarks(unittest.TestCase):
    """Перед запуском теста нужно стереть оценку за 10 лабораторную у Калининой Екатерины
    в журнале https://docs.google.com/spreadsheets/d/1MPkVTspH5MCtCvUXNTduhgQl90N3LIjzLjqfjYTDPdc/edit#gid=867705603"""

    def test_S_7_t1(self):
        """В журнал выставляется ноль"""

        # Создание ожидаемого результата
        Student = User()
        Student.NameOfStudent = 'Калинина Екатерина Алексеевна'
        Student.GroupOfStudent = '18-ИСбо-2б'
        Student.IsRegistered = True
        letters = []
        let = LetterResult()
        let.Student = Student
        let.IsOK = False
        let.CodeStatus = '30'
        let.NumberOfLab = 10
        letters.append(let)

        SetMarks(letters)

        self.assertEqual(letters[0].CodeStatus, '30')

    def test_S_7_t4(self):
        """Данные не изменяются в результате выполнения функции"""
        # Создание ожидаемого результата
        letters = []
        let = LetterResult()
        let.CodeStatus = '05'
        letters.append(let)

        SetMarks(letters)

        self.assertEqual(letters[0].CodeStatus, '05')

    def test_S_7_t2(self):
        """В журнал выставляется единица"""

        # Создание ожидаемого результата
        Student = User()
        Student.NameOfStudent = 'Калинина Екатерина Алексеевна'
        Student.GroupOfStudent = '18-ИСбо-2б'
        Student.IsRegistered = True
        letters = []
        let = LetterResult()
        let.Student = Student
        let.IsOK = True
        let.CodeStatus = '30'
        let.NumberOfLab = 10
        letters.append(let)

        SetMarks(letters)

        # Метод ничего не возвращает, но отрабатывает верно
        self.assertEqual(letters[0].CodeStatus, '30')

    def test_S_7_t3(self):
        """Оценка в журнале не обновляется, т.к. работа была сдана ранее"""

        # Создание ожидаемого результата
        Student = User()
        Student.NameOfStudent = 'Калинина Екатерина Алексеевна'
        Student.GroupOfStudent = '18-ИСбо-2б'
        Student.IsRegistered = True
        letters = []
        let = LetterResult()
        let.Student = Student
        let.IsOK = True
        let.CodeStatus = '30'
        let.NumberOfLab = 10
        letters.append(let)

        SetMarks(letters)

        self.assertEqual(letters[0].CodeStatus, '10')


if __name__ == '__main__':
    unittest.main()
