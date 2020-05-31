import log_method
import re
from pattern import *


@log_method.log_method_info
def validation(head_of_msg,body_of_msg,name):
    """
    Проверка полученного письма на все возможные ошибки
    :param head_of_msg: тема письма (заголовок)
    :param body_of_msg: тело письма, основной текст
    name= Фамилия и имя студента
    :return: { 'Number', 'URL', "errorDescription" }
    """
    url = []
    number = ''
    Error = []
    count = 0
    if (re.search(name, body_of_msg) == None): # Подпись
        Error.append('Отсутствует подпись')
    for i in GREATING_LIST: # Приветсвие
        if re.search(i, body_of_msg) != None:
            count += 1
    if count == 0:
        Error.append('Нет приветствия')
    if re.search(r'№\w+', head_of_msg) != None:    # лаба
        number = re.search(r'№\w+', head_of_msg)[0]
    else:
        Error.append('Неверно указан номер лабораторной')
    if re.search(r'(ТРПО)', head_of_msg) == None:    # дисциплина
        Error.append('Неверно указана дисциплина')
    url.append(re.findall("(?P<url>https?://[^\s]+)",body_of_msg)) # ссылка
    if(len(url[0]) == 0):
        Error.append('Нет ссылки на выполненое задание')
    validation = {
        'Number': number,
        'URL': url[0],
        'Error': Error
        }
    return validation
