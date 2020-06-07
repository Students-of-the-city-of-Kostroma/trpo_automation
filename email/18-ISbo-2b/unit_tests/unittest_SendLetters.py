import unittest
import main_5_send_InformUsers as InformUsers
import global_AnswersForUsers as AnswersForUsers
import work_EmailLibrary as EmailLibrary


class test_SendLetters(unittest.TestCase):
    def test_S_9_t1(self):
        answers = []
        answers.append(AnswersForUsers.AnswersForUsers("trpo.help@gmail.com", "Test", "Hello"))
        smtp_obj = EmailLibrary.smtp_login()
        InformUsers.SendLetters(smtp_obj, answers)
        EmailLibrary.quit_email_smtp(smtp_obj)
        element = answers[0]
        result = element.Success
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
