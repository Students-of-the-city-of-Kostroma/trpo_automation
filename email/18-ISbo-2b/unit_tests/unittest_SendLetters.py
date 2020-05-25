import unittest
import main_5_send_InformUsers as InformUsers
import global_AnswersForUsers as AnswersForUsers


class test_SendLetters(unittest.TestCase):
    def test_S_9_t1(self):
        answers = []
        answers.append(AnswersForUsers.AnswersForUsers("trpo.help@gmail.com", "Test", "Hello"))
        smtp_obj = InformUsers.smtp_login()
        InformUsers.SendLetters(smtp_obj, answers)
        InformUsers.quit_email_smtp(smtp_obj)
        element = answers[0]
        result = element.Success
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
