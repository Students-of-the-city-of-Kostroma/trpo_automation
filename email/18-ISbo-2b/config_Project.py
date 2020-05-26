# coding=utf-8
from datetime import datetime

filename = ""
timeout = 10
teacher_email = "trpo.help@gmail.com"
access = 'https://forms.gle/DRxYQxeRn9z7jvD96'


def num_for_filename():
    n = 1
    while True:
        yield n
        n += 1

gen_num_for_filename = num_for_filename()
last_date = datetime.strftime(datetime.now(), "%Y.%m.%d")
path_to_logs = "D:/trpo/logs/"
