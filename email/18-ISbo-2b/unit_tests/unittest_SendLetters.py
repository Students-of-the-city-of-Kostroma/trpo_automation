import unittest
import global_AnswersForUsers as AnswersForUsers
import work_EmailLibrary as EmailLibrary

import config_Project
import global_Logging

config_Project.logger = global_Logging.Logger()
i = config_Project.logger
config_Project.logger.createlogfile()

import main_5_InformUsers as InformUsers


class test_SendLetters(unittest.TestCase):
    def test_S_9_t1(self):
        answers = []
        answers.append(AnswersForUsers.AnswersForUsers("trpo.help@gmail.com", "Test", "Hello"))
        InformUsers.SendLetters(answers)
        element = answers[0]
        result = element.Success
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
    config_Project.logger.closelogfile()
