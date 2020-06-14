import unittest

class Test_validation(unittest.TestCase):

    def setUp(self):
        pass
        #crp.decrypt_file('configs/Example.json.bin')
        #crp.decrypt_file('configs/credentials.json.bin')
        #crp.decrypt_file('configs/config.py.bin')
        #crp.decrypt_file('configs/token.pickle.bin')

    def tearDown(self):
        pass
        #add_str_in_table(table='ТeстовыйЛист', cell='N3', line='', id_table=SPREAD_SHEET_ID_TEST)
        #crp.crypt_file('configs/Example.json')
        #crp.crypt_file('configs/credentials.json')
        #crp.crypt_file('configs/config.py')
        #crp.crypt_file('configs/token.pickle')


    def test_all_positive(self):
        from Validation import validation

        message_info = {
            'email_id': r'"Иван Иванович" <test@gmail.com>',
            'body_of_msg': r'Добрый день, вот лабораторная http://github.com -- С уважением, Иван Иванович 18-ИСбо-2а',
            'head_of_msg': r'ТРПО. Лабораторная работа №3',
        }

        valid_dict = validation(message_info['head_of_msg'], message_info['body_of_msg'], 'Иван Иванович')

        self.assertEqual(valid_dict, {'Number': '3', 'URL': ['http://github.com'], 'errorDescription': []})

    def test_sign(self):
        from Validation import validation

        message_info = {
            'email_id': r'"Иван Иванович" <test@gmail.com>',
            'body_of_msg': r'Добрый день, вот лабораторная http://github.com',
            'head_of_msg': r'ТРПО. Лабораторная работа №3',
        }

        valid_dict = validation(message_info['head_of_msg'], message_info['body_of_msg'], '"Иван Иванович"')

        self.assertEqual(valid_dict, {'Number': '3', 'URL': ['http://github.com'], 'errorDescription': ['Отсутствует подпись']})

    def test_title(self):
        from Validation import validation

        message_info = {
            'email_id': r'"Иван Иванович" <test@gmail.com>',
            'body_of_msg': r'Добрый день, вот лабораторная http://github.com -- С уважением, Иван Иванович 18-ИСбо-2а',
            'head_of_msg': r'Лаба',
        }

        valid_dict = validation(message_info['head_of_msg'], message_info['body_of_msg'], '"Иван Иванович"')

        self.assertEqual(valid_dict, {'Number': '', 'URL': ['http://github.com'],
                                      'errorDescription': ['Нет номера лабораторной работы', 'Неверно указана дисциплина']})

    def test_hello(self):
         from Validation import validation

         message_info = {
             'email_id': r'"Иван Иванович" <test@gmail.com>',
             'body_of_msg': r'Вот лабораторная http://github.com -- С уважением, Иван Иванович 18-ИСбо-2а',
             'head_of_msg': r'ТРПО. Лабораторная работа №3',
         }

         valid_dict = validation(message_info['head_of_msg'], message_info['body_of_msg'], '"Иван Иванович"')

         self.assertEqual(valid_dict, {'Number': '3', 'URL': ['http://github.com'],
                                       'errorDescription': ['Нет приветствия']})

    def test_all_negative(self):
        from Validation import validation

        message_info = {
            'email_id': r'"Иван Иванович" <test@gmail.com>',
            'body_of_msg': r'Вот лабораторная http://github.com',
            'head_of_msg': r'Лаба',
        }

        valid_dict = validation(message_info['head_of_msg'], message_info['body_of_msg'], '"Иван Иванович"')

        self.assertEqual(valid_dict, {'Number': '', 'URL': ['http://github.com'],
                                      'errorDescription': ['Отсутствует подпись',
                                                           'Нет приветствия',
                                                           'Нет номера лабораторной работы',
                                                           'Неверно указана дисциплина']})


if __name__ == '__main__':
    unittest.main()
