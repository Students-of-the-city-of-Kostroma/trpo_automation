import config as cfg
import datetime


class Logger:

    d_file = None

    def __init__(self):
        self.createlogfile()

    def createlogfile(self):
        filename = cfg.filename
        num = filename[-2:]
        if num[0].isdigit() is not True:
            num = num[1]
        num = int(num) + 1
        filename = 'log' + str(num)
        cfg.filename = filename
        filename = filename + '.txt'
        self.d_file = open(filename, 'a', encoding='utf-8')

    def closelogfile(self):
        self.d_file.close()

    def logdebug(self, func):
        def decorated(*args, **kwargs):
            now = datetime.datetime.now()
            info = '[' + str(now.hour) + ':' + str(now.minute) + ']' + '[DEBUG]:' + str(func.__name__) + '\n'
            self.d_file.write(info)
            result = func(*args, **kwargs)
            return result
        return decorated

    def loginfo(self, func):
        def decorated(*args, **kwargs):
            now = datetime.datetime.now()
            info = '[' + str(now.hour) + ':' + str(now.minute) + ']' + '[INFO]:' + str(func.__name__) + '\n'
            info += '[\nВходные параметры\n'
            for i in args:
                info += str(i) + '\n'
            for i in kwargs:
                info += str(i) + '\n'
            info += ']\n'
            self.d_file.write(info)
            result = func(*args, **kwargs)
            return result
        return decorated
#Logger()
