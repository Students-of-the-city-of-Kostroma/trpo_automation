import log_config as cfg
import datetime
import os


class Logger:

    d_file = None

    def __init__(self):
        pass

    def createlogfile(self):
        """Создает файл для логов в папке logfiles"""
        self.updatelogfiles()
        filename = cfg.filename + '.txt'
        fullpath = 'logfiles/' + filename
        self.d_file = open(fullpath, 'a', encoding='utf-8')

    def closelogfile(self):
        """Закрывает дескриптор файла"""
        self.d_file.close()

    def logdebug(self, func):
        """Логирование уровня DEGUG"""
        def decorated(*args, **kwargs):
            now = datetime.datetime.now()
            info = '[' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + ']' + '[DEBUG]:' \
                   + str(func.__name__)
            info += '\n\n'
            self.d_file.write(info)
            result = func(*args, **kwargs)
            return result
        return decorated

    def loginfo(self, func):
        """Логирование уровня INFO"""
        def decorated(*args, **kwargs):
            now = datetime.datetime.now()
            info = '[' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + ']' + '[INFO]:' \
                   + str(func.__name__) + '\n'
            info += '[Входные параметры\n'
            for i in args:
                #if str(i).find('object at') != -1:
                #    continue
                info += str(i) + '\n'
            for i in kwargs:
                info += str(i)
            info = info[:-2]
            info += ']\n\n'
            self.d_file.write(info)
            result = func(*args, **kwargs)
            return result
        return decorated

    def updatelogfiles(self):
        """Увеличивает номер файла логов. Чистит папку, если их скопилось 20"""
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

    @staticmethod
    def getobjectdata(ob):
        info = ''
        ats = ob.__dict__
        for i in ats.values():
            if str(i).startswith('__main__.'):
                info += getobjectdata(i)
            else:
                info += str(i) + '\n'
        return info