import json
import socket
import traceback
import xml.etree.ElementTree as etree
from enum import Enum

from .log_method import log_method_info, logger

CONFIG_PORTS_URL = "../../labs.xml"
LOCALHOST_ADDRESS = '127.0.0.1'

""" Словарь для хранения существующих соединений с серверами проверки лабораторных работ """
connections = {}


class MessageType(Enum):
    """ Перечисляемый тип для ключа messageType, использующегося в спецификации общения клиента с сервером """
    REQUEST = 1
    DEFAULT_ANSWER = 2
    WRONG_REQUEST = 3
    SERVER_ERROR = 4


@log_method_info
def create_connection(lab_number: int) -> None:
    """
    Создает соединение и записывает сокет в словарь под ключом соответствующей
        лабораторной работы
    :param lab_number: номер лабораторной работы
    :return: None
    """
    try:
        logger.debug("Create connection to server for lab {lab_number}...".format(lab_number=lab_number))
        local_sock: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        local_sock.connect((LOCALHOST_ADDRESS, get_port(lab_number)))
        if local_sock.recv(1024).decode() == "New connection!":
            logger.debug("Connection successful!")
            connections[lab_number] = local_sock
        else:
            raise ConnectionRefusedError("Connection to server for lab {lab_number} refused"
                                         .format(lab_number=lab_number))
    except socket.error as err:
        raise SystemError("Error creating socket: {error} \n with traceback {tb}"
                          .format(error=err, tb=traceback.format_exc()))


@log_method_info
def get_port(lab_number: int) -> int:
    """
    Получает номер порта для сокета по номеру лабораторной работы из конфига
    :param lab_number: номер лабораторной работы
    :return: номер порта
    """
    try:
        logger.debug("Load config for ports stored...")
        tree = etree.parse(CONFIG_PORTS_URL)
        logger.debug("Config loaded. Searching for the port by lab number given")
        for lab in tree.getroot():
            if int(lab.attrib.get('number')) == lab_number:
                return int(lab.attrib.get('port'))
        raise LookupError("No port found for the lab number given")
    except FileNotFoundError as err:
        raise FileNotFoundError("Not found config file: {error} \n with traceback {tb}"
                                .format(error=err, tb=traceback.format_exc()))


@log_method_info
def format_request(lab_number: int, variant: int, link: str) -> str:
    """
    Формирует json строку для сервера
    TODO: продумать обработку, в случае остальных лаб (зависим от спеки)
    :param lab_number: номер лабораторной работы
    :param variant: номер вариат решения
    :param link: ссылка на решение (в случае lab_number in [3, 7] ссылка на репозиторий Github)
    :return: json строка для сервера
    """
    request_data: dict = {
        'messageType': MessageType.REQUEST.value,
        'lab': lab_number,
        'variant': variant,
        'link': link,
    }

    try:
        logger.debug("Formatting request into json string. Args passed: \
            lab_number - {lab_number}, variant - {variant}, link - {link}"
                     .format(lab_number=lab_number, variant=variant, link=link))
        return json.dumps(request_data)
    except TypeError as err:
        raise TypeError("Unable to serialize the object: {error}".format(error=err))


@log_method_info
def check_lab(link: str = 'https://github.com/leshastern/strategy4',
              lab_number: int = 7,
              variant: int = 1) -> dict:
    """
    Контролирует цикл общения с сервером
    TODO продумать систему в случае нескольих лаб (зависим от спеки)
    :param link: ссылка на решение лабораторной работы (в случае с lab_number in [3, 7] ссылка на репозиторий Github)
    :param lab_number: номер лабораторной работы
    :param variant: номер варианта решения
    :return: словарь с результатом проверки вида {'grade': int, 'comment': None or str},
        где ключ 'comment' присутствует только в случае grade == 0
    """
    try:
        if lab_number not in connections:
            logger.debug("No socket for connection found.")
            create_connection(lab_number)

        request: str = format_request(lab_number, variant, link)
        try:
            return handle_reply(connections[lab_number], request)
        except socket.timeout:
            # Если сервер разорвал соединение, или не отвечает, пробуем еще раз
            logger.debug("Connection was closed, trying one more time...")
            create_connection(lab_number)
            try:
                return handle_reply(connections[lab_number], request)
            except socket.timeout as err:
                raise TimeoutError("Server not responding: {error} \n with traceback {tb}"
                                   .format(error=err, tb=traceback.format_exc()))
    # FIXME пока зашил общий Exception, так как неизвестна глубина обрабокти ислючений извне
    except Exception as exc:
        logger.error(exc)
        raise exc


@log_method_info
def handle_reply(current_socket: socket, request: str) -> dict:
    """
    Отправляет сообщение на сервер, получает и обрабатывает ответ
    :param current_socket: сокет для общения с сервером
    :param request: сформированный запрос на сервер
    :return: ответ о проверке лабораторной работы
    """
    logger.info("Sending request on server to check the lab...")
    logger.debug("The request is: {request}".format(request=request))
    current_socket.send(request.encode())
    try:
        reply_data: dict = json.loads(current_socket.recv(1024).decode())
        logger.info("Got a reply from server!")
        message_type: int = reply_data.pop('messageType')
        if message_type == MessageType.WRONG_REQUEST.value:
            raise SystemError("We've got problems: an error \n {error} \n occurred with a key '{key}'"
                              .format(error=reply_data['text'], key=reply_data['key']))
        elif message_type == MessageType.SERVER_ERROR.value:
            raise SystemError("Server has got a problem: {error}".format(error=reply_data['errorMessage']))
        elif message_type == MessageType.DEFAULT_ANSWER.value:
            logger.debug("The lab was successfully checked, moving on..")
            return reply_data
    except TypeError as err:
        raise TypeError("Error reading data from server: {error} \n with traceback {tb}"
                        .format(error=err, tb=traceback.format_exc()))
