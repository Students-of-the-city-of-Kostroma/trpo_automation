from main_3_send_SetResults import SetMarks
from global_User import User
from global_LetterResult import LetterResult
import google_Sheet
import unittest


class test_SetMarks(unittest.TestCase):


    def test_S_7_t1(self):
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


    def test_S_7_t2(self):

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


    def test_S_7_t3(self):

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

        # Создание ожидаемого результата
        letters = []
        let = LetterResult()
        let.CodeStatus = '05'
        letters.append(let)

        SetMarks(letters)

        self.assertEqual(letters[0].CodeStatus, '05')


if __name__ == '__main__':
    unittest.main()