import unittest
import httplib2
import requests
import apiclient.discovery
import utils.crypto as crp
from oauth2client.service_account import ServiceAccountCredentials


class TestGoogle(unittest.TestCase):
    def setUp(self):
        crp.decrypt_file('configs/Example.json.bin')
        crp.decrypt_file('configs/credentials.json.bin')
        crp.decrypt_file('configs/config.py.bin')
        #crp.decrypt_file('configs/token.pickle.bin')

    def tearDown(self):
        crp.crypt_file('configs/Example.json')
        crp.crypt_file('configs/credentials.json')
        crp.crypt_file('configs/config.py')
        #crp.crypt_file('configs/token.pickle')

    def test_get_service(self):
        from APIgoogle import get_service

        service = get_service()

        assert service

    def test_add_str_in_table(self):
        from APIgoogle import add_str_in_table
        from configs.config import SPREAD_SHEET_ID_TEST

        # Выставление отметки
        add_str_in_table(table='ТeстовыйЛист', cell='N3', line='test', id_table=SPREAD_SHEET_ID_TEST)

        # Получение этой отметки из журнала
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
           r'configs/Example.json',
            [
                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive'
            ]
        )
        httpAuth = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
        result = service.spreadsheets().values().get(spreadsheetId=SPREAD_SHEET_ID_TEST,
                                                      range='ТeстовыйЛист!N3').execute()

        self.assertEqual(result['values'][0][0], 'test')

    def test_cleaning_email(self):
        from APIgoogle import cleaning_email

        result = cleaning_email('<username@gmail.com>')
        self.assertEqual(result, 'username@gmail.com')

    def test_name_surname(self):
        from APIgoogle import name_surname

        result = name_surname('"Святослав Котяхов" <k.svyat395@gmail.com>')
        self.assertEqual(result, '"Святослав Котяхов" ')

    def test_get_something(self):
        from APIgoogle import get_something
        from configs.config import SPREAD_SHEET_ID_TEST

        result = get_something('ТeстовыйЛист!L3', spreadsheetid=SPREAD_SHEET_ID_TEST)['values'][0][0]
        self.assertEqual(result, 'Something')

    def test_search_email_positive(self):
        from APIgoogle import search_email
        from configs.config import SPREAD_SHEET_ID_TEST

        result = search_email(email_id='<this@mail.ru>', list='ТeстовыйЛист', id_table=SPREAD_SHEET_ID_TEST)
        self.assertEqual(result, 'this@mail.ru')

    def test_search_email_negative(self):
        from APIgoogle import search_email
        from configs.config import SPREAD_SHEET_ID_TEST

        result = search_email('notThis@mail.ru', id_table=SPREAD_SHEET_ID_TEST)
        self.assertIsNone(result)

    def test_get_message_and_send_message(self):
        from APIgoogle import get_message, send_message, get_service, email_archiving

        USER_ID = 'me'
        service = get_service()

        send_message(service, USER_ID, 'trpo.automation@gmail.com', 'Test', -1,
                     None, None, '"Test Test" <trpo.automation@gmail.com>')

        message_info = get_message(service, USER_ID)
        email_archiving(service, USER_ID, message_info)

        self.assertIsNotNone(message_info)

    def test_error_work(self):
        from APIgoogle import error_in_work

        dict_valid = {
            'errorDescription': ['Ошибка1', 'Ошибка2', 'Ошибка3']
        }

        result = error_in_work(dict_valid)
        self.assertEqual(result, '- Ошибка1\n- Ошибка2\n- Ошибка3\n')


if __name__ == '__main__':
    unittest.main()
