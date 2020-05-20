# coding=utf-8
import inspect
from Loger import Logs 
logs = Logs()
name = None

import socket
import global_LetterResult
import json
import select
import lxml
import requests
from bs4 import BeautifulSoup
import global_Letter
import requests
from bs4 import BeautifulSoup
from main_3_send_SetResults import SetResults
import config_Project as cfg

def WorkWithLetters(letters):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name,letters)
    """
    Работа с письмами, формирование правильного формата данных,
    отправка их на проверку, принятие результатов и их передача дальше
    """
    # Подготовка писем - получение сырых данных
    letters = LettersConvertToString(letters)

    print(letters)

    # Формирование JSON
    jsonDates = FormJSONDates(letters)

    print(letters)

    # Отправка данных
    letterResults = SendJSONForCheck(jsonDates, letters)

    print(letters)

    # SetResults - Передать данные следующему модулю в формате списка экземпляров класса EmailResults
    SetResults(letterResults)

def LettersConvertToString(letters):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name,letters)
    """
    Функционал:
    - Вытащить сырые данные по ссылкам из поля Body
    - Переконвертировать их в строковой формат и разместить в поле Body
    На входе:
    - letter - заполненный и провалидированный список писем - экземпляров класса Letter
    На выходе:
    - letters - Список писем, в каждом из которых в поле Body лежит необходимая для отправки информация
    Что предусмотреть:
    - Для некоторых писем нужно вытаскивать данные, для какой-то достаточно ссылки. Предусмотреть проверку на это
    в соответствии со спецификацией по JSON
    """

    with open(cfg.filename, "a") as file:
        file.write("\nПолучение данных... ")

    LabsForWork = [4, 5, 6, 7, 8, 9, 10, 12]
    for tmp in letters:
        if tmp.CodeStatus == "20" and tmp.NumberOfLab in LabsForWork:
            html = get_html(tmp.Body)
            tmp.Body = finding_files(html, tmp.Student.NameOfStudent)

    with open(cfg.filename, "a") as file:
        file.write("Данные получены!")

    return letters


def FormJSONDates(letters):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name,letters)
    """
    Функционал:
    - Сформировать список, хранящий экземпляры json с данными, необходимыми для отправки по каждой лабораторной
    На входе:
    - convertedLetter - список писем - экземпляров класса Letter, в каждом из которых в поле Body лежит необходимая для
    отправки информация
    На выходе:
    - jsonDates - список json с нужными данными и в нужном формате
    Что предусмотреть:
    - Формат json для каждой лабораторки прописан в спецификации по json, но по факту он везде одинаковый
    - Продумать момент обработки списка писем
    """

    with open(cfg.filename, "a") as file:
        file.write("\nФормирование JSON... ")

    jsons = []
    for i in range(len(letters)):
        num = letters[i].NumberOfLab
        if letters[i].CodeStatus == "20":
            json1 = {
                "messageType" : 1,
                "lab" : letters[i].NumberOfLab,
                "variant" : letters[i].VariantOfLab,
                "link" : letters[i].Body if num == 2 or num == 3 or num == 11 else None,
                "code" : letters[i].Body if num == 4 or num == 5 or num == 6 or num == 7 or num == 8 or num == 9 or num == 10 or num == 12 else None
                }
            mystr = json.dumps(json1)
            jsons.append(mystr)

    with open(cfg.filename, "a") as file:
        file.write("Объекты JSON сформированы!")

    return jsons

def SendJSONForCheck(jsonDates, letters):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name, jsonDates, letters)
    """
    Функционал:
    - Отправить письма на проверку в модули проверки писем от ВТ
    - Дождаться проверки каждого из писем
    - Сформировать список экземпляров классов LetterResults по каждому письму, расставить оценки и комментарии от ВТ
    На входе:
    - jsonDates - список с экземплярами json, с нужными данными в нужном формате
    - letters - список писем, передаваемый от модуля к модулю. Используются при заполнении экземпляров класса LetterResult
    На выходе:
    - letterResult - заполненный список экземпляров класса LetterResult с результатами обработки писем
    Что предусмотреть:
    - Будет синхронный режим работы, когда сначала отправляется первый json потом происходит ожидание ответа на него,
    после чего происходит заполнение нужных полей
    отправить json1 ->
    получить ответ на json1 ->
    Заполнить нужные поля в result1 ->
    отправить json3 ->
    получить ответ на json3 ->
    Заполнить нужные поля в result3 ->
    отправить json3 ->
    получить ответ на json3 ->
    Заполнить нужные поля в result3 ->
    ...
    - Каждый json нужно отправить на нужный порт. Предусмотреть проверку на это в соответствии со спецификацией по JSON
    - Предусмотеть таймаут ожидания, чтобы система не зависала на бесконечное время при ошибках в модулях проверки
    В этом случае заполнять не только поле IsOK но и поле Code
    """

    # Список новых писем
    new_letters = []

    # IP адрес
    configServ = open("config_Server.txt", "r")
    HOST = configServ.readline()
    HOST = HOST.replace("\n", '')

    # Словарь лабораторных и портов к ним
    config_port = open("config_Port.json", "r")
    configLab = config_port.read()

    # Соответствие номера лабораторной и номера порта
    dataLab = json.loads(configLab)

    # Счётчик для параллельного обращения в два списка
    count = 0

    for i in letters:
        letter = global_LetterResult.LetterResult()

        IsOk = False
        if i.CodeStatus == "20":
            sock = socket.socket()

            # Подключение и отправка JSON на порт
            port = dataLab[str(i.NumberOfLab)]

            # На случай если сервер не доступен
            try:

                # Подключение к серверу
                sock.connect((HOST, port))
                sock.send(jsonDates[count].encode())

                count += 1

                # Ожидание ответа сервера 10 секунд
                ready = select.select([sock], [], [], 10)

                # При условии, что ответ был получен в течение 10 секунд
                if ready[0]:
                    otv_serv = sock.recv(1024)
                    otvetServ = json.loads(otv_serv.decode())
                    if otvetServ["messageType"] == 2:
                        if otvetServ["grade"] == 1:
                            IsOk = True
                        letter.Comment = otvetServ["comment"]
                        letter.CodeStatus = "30"
                        letter.Comment = ""
                        sock.close()

                    elif otvetServ["messageType"] == 3:
                        letter.CodeStatus = "07"
                        letter.CodeStatusComment = ""
                        letter.Comment = otv_serv.decode()
                        sock.close()

                    elif otvetServ["messageType"] == 4:
                        letter.CodeStatus = "06"
                        letter.CodeStatusComment = ""
                        letter.Comment = otv_serv.decode()
                        sock.close()
                else:
                    sock.close()
                    letter.CodeStatus = "06"
                    letter.CodeStatusComment = "ERROR. Длительное ожидание ответа от сервера"
            except:

                # Для того, чтобы знать что случилось
                letter.CodeStatusComment = "Сервер был не доступен"
                letter.CodeStatus = "06"
        else:
            # Заполнение полей letterResult
            letter.CodeStatus = i.CodeStatus
            letter.Student = i.Student
            letter.IsOK = IsOk
            letter.VariantOfLab = i.VariantOfLab
            letter.NumberOfLab = i.NumberOfLab

        # Добавление нового письма
        new_letters.append(letter)

    with open(cfg.filename, "a") as file:
        file.write("Данные отправлены и обработаны!")

    return new_letters



def get_html(url):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name, url)
    """Достаю html с введённой ссылки и возвращаю в виде текста"""
    r = requests.get(url)    # Получим метод Response
    r.encoding = 'utf8'
    return r.text   # Вернем данные объекта text


def csv_read(data):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name, data)
    """Принятые данные принимает, проверяя: являются ли они строковыми данными
    Если да, записываю их в файл, в конце делаю перенос строки"""
    if isinstance(data, str):
        with open("data.txt", 'a') as file:
            file.write(data+'\n')
            return data


def get_link(html):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name, html)
    """Построчно ищу поля таблицы с id = LC1,LC2 и т.д., затем передаю их на запись в метод csv
    Если больше нет полей таблицы( то есть кода или текстовых данных), тогда метод закончит работу"""
    soup = BeautifulSoup(html, 'lxml')
    head = soup.find('strong', class_="final-path")
    data = ""
    if head != None:
        csv_read("\nFile Title: "+head.getText()+"\n")
    i = 1
    flag = True
    while flag:
        head = soup.find('td', id="LC"+i.__str__())
        if head is None:
            flag = False
        else:
            data += csv_read(head.getText())
            i += 1
    return data


def finding_files(html, name):
    nameFun = inspect.currentframe().f_code.co_name
    logs.Infor(nameFun, html,name)
    """Метод отвечает за поиск и открытие файлов или папок в репозитории Git'a;
    если ссылка, которую мы открыли не имеет ссылок на другие объекты(файлы или папки),
    мы предполагаем, что это открытый файл и передаём его на парсинг файла в get_link"""
    main_data = ""
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find_all('td', class_ = "content")
    date = finding_links(table)
    if len(date) == 0:
        data = get_link(html)
        return data
    for item in date:
        title = item.get('title')
        if title == name or title.split(".")[0] == name:
            item = item.get('href')
            if item != None:
                main_data += finding_files(get_html("https://github.com"+item), name)
    return main_data



def finding_links(table):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name, table)
    """Ищет ссылки, на которые можно перейти, то есть проверяет есть ли файлы или папки
    на этой странице или же это уже страница самого файла"""
    date = []
    for item in table:
        date.append(item.find('a', class_="js-navigation-open"))
        if date[len(date) - 1] == None:
            date = date[:len(date) - 1]
    return date
