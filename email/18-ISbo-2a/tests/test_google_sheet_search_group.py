import sys
sys.path.append('..')
import unittest
from mainp import crypto


class TestGoogle(unittest.TestCase):
        
    def setUp(self):
        crypto.decrypt_file('Example.json.bin')
        crypto.decrypt_file('config.py.bin')

    def tearDown(self):
        crypto.crypt_file('Example.json')
        crypto.crypt_file('config.py')

    def test_search_group(self):
        """
        TODO сделать два метода с известным результатом
        :return:
        """
        from ..mainp.APIgoogle import search_group

        test_email = '0sashasmirnov0@gmail.com'
        act= ('18-ИСбо-2а', 'Смирнов Александр Алексеевич')
        exp = search_group(test_email)

        self.assertEqual(exp, act)

if __name__ == '__main__':
    unittest.main()
