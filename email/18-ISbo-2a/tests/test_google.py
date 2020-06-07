import unittest
import httplib2
import requests
import apiclient.discovery
import utils.crypto as crp
from oauth2client.service_account import ServiceAccountCredentials


class TestGoogle(unittest.TestCase):
    def setUp(self):
        pass
        #crp.decrypt_file('configs/Example.json.bin')
        #crp.decrypt_file('configs/credentials.json.bin')
        #crp.decrypt_file('configs/config.py.bin')
        #crp.decrypt_file('configs/token.pickle.bin')

    def tearDown(self):
        #add_str_in_table(table='ТeстовыйЛист', cell='N3', line='', id_table=SPREAD_SHEET_ID_TEST)
        #crp.crypt_file('configs/Example.json')
        #crp.crypt_file('configs/credentials.json')
        #crp.crypt_file('configs/config.py')
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

        assert result['values'][0][0] == 'test'


if __name__ == '__main__':
    unittest.main()
