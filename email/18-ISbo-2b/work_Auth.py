# Подключаем библиотеки
import config_Project as l_cfg
import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


class Auth:
    """Авторизация в системе, выбор API для работы с Google Sheets """
    @l_cfg.logger.loginfo	
    def auth_sheets():
        # Имя файла с закрытым ключом, вы должны подставить свое
        CREDENTIALS_FILE = 'trpo-bot-1eb977889b18.json'

        # servis email: trpo-bot@trpo-bot.iam.gserviceaccount.com
        # Читаем ключи из файла
        credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

        # Авторизуемся в системе
        httpAuth = credentials.authorize(httplib2.Http())

        # Выбираем работу с таблицами и 4 версию API
        service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

        return service
