import log_config as cfg
import datetime
import os


class Logger:

    d_file = None

    def __init__(self):
        pass

    def createlogfile(self):
        self.updatelogfiles()
        filename = cfg.filename + '.txt'
        fullpath = 'logfiles/' + filename
        self.d_file = open(fullpath, 'a', encoding='utf-8')

    def closelogfile(self):
        self.d_file.close()

    def logdebug(self, func):
        def decorated(*args, **kwargs):
            now = datetime.datetime.now()
            info = '[' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + ']' + '[DEBUG]:' \
                   + str(func.__name__) + '\n'
            info += '-----------------------\n'
            self.d_file.write(info)
            result = func(*args, **kwargs)
            return result
        return decorated

    def loginfo(self, func):
        def decorated(*args, **kwargs):
            now = datetime.datetime.now()
            info = '[' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + ']' + '[INFO]:' \
                   + str(func.__name__) + '\n'
            info += '[\nВходные параметры\n'
            for i in args:
                info += str(i) + '\n'
            for i in kwargs:
                info += str(i) + '\n'
            info += ']\n'
            info += '-----------------------\n'
            self.d_file.write(info)
            result = func(*args, **kwargs)
            return result
        return decorated

    def updatelogfiles(self):
        filename = cfg.filename
        num = filename[-2:]
        if num[0].isdigit() is not True:
            num = num[1]
        num = int(num) + 1
        filename = 'log' + str(num)
        if cfg.filename[-1:] == '20':
            folder = 'logfiles/'
            files = os.listdir(folder)
            for i in files:
                path = os.path.join(folder, i)
                os.remove(path)
            filename = 'log' + str(1)
        cfg.filename = filename

#Logger()
