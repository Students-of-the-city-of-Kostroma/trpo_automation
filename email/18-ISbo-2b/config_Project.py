# coding=utf-8
from datetime import datetime


timeout = 10
teacher_email = "trpo.help@gmail.com"
user_access = 'https://forms.gle/DRxYQxeRn9z7jvD96'
user_rules = 'https://docs.google.com/document/d/1YMtlwsImBzR1ONhY6hH0VZnonpRmHM9UZ0glsG8sMLA/edit?usp=sharing'
filename = ""
logger = None
logfile = None

def num_for_filename():
    n = 1
    while True:
        yield n
        n += 1

gen_num_for_filename = num_for_filename()
last_date = datetime.strftime(datetime.now(), "%Y.%m.%d")
path_to_logs = "D:/trpo/logs/"
