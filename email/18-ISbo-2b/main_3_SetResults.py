# coding=utf-8
from logs import log_config as l_cfg
from work_Loger import Logs
from work_Sheet import Sheet

import inspect


@l_cfg.logger.logdebug
def SetResults(letterResults):
    """
    Выставить необходимые оценки в журнал
    """

    # Выставление оценок в журнал
    # Глобальная функция 7
    SetMarks(letterResults)

    return letterResults


@l_cfg.logger.logdebug
def SetMarks(letterResults):
    """
     Функционал:
    - Выставить необходимые оценки в журнал
    На входе:
    - letterResults - заполненный и проверенный список писем - экземпляров класса LetterResults
    На выходе:
    - None
    Что предусмотреть:
    - None
    """
    # logs = Logs()
    # name = inspect.currentframe().f_code.co_name
    # logs.Infor(name, letterResults)

    for i in letterResults:
        if i.CodeStatus == "30":
            value = 0
            if i.IsOK:
                value = 1

            group = i.Student.GroupOfStudent
            name = i.Student.NameOfStudent.split(' ')
            first_name = name[0]
            surname = name[1]
            patronymic = name[2]
            lab_id = '{}'.format(i.NumberOfLab)

            result = Sheet.journal(group, first_name, surname, patronymic, lab_id, value)
            if result:
                if result[0] == '1':
                    i.CodeStatus = '10'
