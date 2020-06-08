import config_Project as cfg
import datetime
import traceback
import sys


class Logger:

    # d_file = None

    def __init__(self):
        pass

    def createlogfile(self):
        """Создает файл для логов в папке logfiles"""
        self.updatelogfiles()
        filename = cfg.filename + '.txt'
        fullpath = 'logfiles/' + filename
        cfg.logfile = open(fullpath, 'a', encoding='utf-8')

    def closelogfile(self):
        """Закрывает дескриптор файла"""
        cfg.logfile.close()

    def logdebug(self, func):
        """Логирование уровня DEGUG"""
        def decorated(*args, **kwargs):
            now = datetime.datetime.now()
            info = '[' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + ']' + '[DEBUG]:' \
                   + str(func.__name__) + '\n'
            info += '[Входные параметры\n'
            for i in args:
                if str(type(i)) == "<class 'list'>" or str(type(i)) == "<class 'tuple'>":
                    for x in i:
                        info += Logger.getobjectdata(x)
                else:
                    info += Logger.getobjectdata(i)
            for i in kwargs:
                info += Logger.getobjectdata(i)
            info = info[:-1]
            info += ']\n\n'
            cfg.logfile.write(info)
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                tr = traceback.format_exc(10)
                tr = str(tr)
                res = Logger.logerror(func, tr, *args, **kwargs)
                res = str(res)
                cfg.logfile.write(res)
                sys.exit()
        return decorated


    def loginfo(self, func):
        """Логирование уровня INFO"""
        def decorated(*args, **kwargs):

            now = datetime.datetime.now()
            info = '[' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + ']' + '[INFO]:' \
                   + str(func.__name__)
            info += '\n\n'
            cfg.logfile.write(info)
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                tr = traceback.format_exc(10)
                tr = str(tr)
                res = Logger.logerror(func, tr, *args, **kwargs)
                res = str(res)
                cfg.logfile.write(res)
                sys.exit()
        return decorated


    def updatelogfiles(self):
        """Изменяет номер файла логов"""
        now = datetime.datetime.now()
        min = str(now.minute)
        if len(min) == 1:
            min = '0' + min
        filename = 'log' + str(now.year) + '.' + str(now.month) + '.' + str(now.day) + '-' + \
                   str(now.hour) + '.' + min
        cfg.filename = filename


    @staticmethod
    def getobjectdata(ob):
        info = ''
        ats = dir(ob)
        if ats.count('__dict__') > 0:
            ats = ob.__dict__
            for key, i in ats.items():
                if str(i).startswith('<'):
                    info += '<Object attributes:\n'
                    info += key + ' : '
                    info += Logger.getobjectdata(i)
                    info += '>\n'
                else:
                    info += key + ' : '
                    info += str(i) + '\n'
        else:
            info += str(ob) + '\n'
        return info

    @staticmethod
    def logerror(func, tr, *args, **kwargs):
        now = datetime.datetime.now()
        info = '[' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + ']' + '[ERROR]:' \
               + str(func.__name__) + '\n'
        info += '[Входные параметры\n'
        for i in args:
            if str(type(i)) == "<class 'list'>" or str(type(i)) == "<class 'tuple'>":
                for x in i:
                    info += Logger.getobjectdata(x)
            else:
                info += Logger.getobjectdata(i)
        for i in kwargs:
            info += Logger.getobjectdata(i)
        info = info[:-1]
        info += '\n' + tr + '\n\n'
        result = info
        return result

