import json
import random
import socket

import log_method


@log_method.log_method_info
def server_otvet(port):
    """
    Метод "заглушки" для сервера
    port - по какому порту будет настроено соединение
    (в дальнейшем, можно будет узнать номер лабораторной по номеру порта)
    """
    sock = socket.socket()
    sock.bind(('127.0.0.1', port))
    sock.listen(1)
    conn, addr = sock.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        r = random.randint(0, 1)
        data_j = {
            "labStatus": r,
        }
        y = json.dumps(data_j)
        conn.send(y.encode())
        log_method.logger.debug(f'server_otvet send {r}')

    conn.close()
