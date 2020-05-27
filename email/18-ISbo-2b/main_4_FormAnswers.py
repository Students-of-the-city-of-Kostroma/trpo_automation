# coding=utf-8
from work_Loger import Logs
from global_AnswersForUsers import AnswersForUsers
import config_Project as cfg
import work_PatternsOfLetter

import inspect

def FormAnswers(letterResult):
    """
    Формирование ответов пользователям
    """

    # Формирование ответов пользователю
    # Глобальная функция 8
    answers = MakeAnswersForUsers(letterResult)

    return answers


def MakeAnswersForUsers(letterResult):
    """
    Функционал:
    - Сформировать список экземпляров класса AnswersForUsers, используя уже готовые ответы на письма
    На входе:
    - Список проверенных писем - экземпляров класса LetterResults и сформированные ответы на письма
    На выходе:
    - answers - список экземпляров класса AnswersForUsers, в котором находятся все необходимые для отправки письма
    Что предусмотреть:
    - поле Who заполняется из письма из поля Student из поля Email
    - поле What заполняется из текстового ответа на это письмо
    - для преподавателя нет письма, из которого можно достать Email, поэтому это нужно вписать в программу вручную
    Участвующие внешние типы переменных
    - AnswersForUsers - из import
    """
    # logs = Logs()
    # name = inspect.currentframe().f_code.co_name
    # logs.Infor(name, letterResult)

    answers = []
    teacher = False
    flag = False
    forTeacher = work_PatternsOfLetter.ForTeacher()

    for i in letterResult:
        if i.CodeStatus == "00":
            pattern = work_PatternsOfLetter.UnknownUser()

        elif i.CodeStatus == "01":
            pattern = work_PatternsOfLetter.UncorrectedTheme()

        elif i.CodeStatus == "02":
            pattern = work_PatternsOfLetter.UncorrectedStructure()

        elif i.CodeStatus == "03":
            pattern = work_PatternsOfLetter.UncorrectedVariant()

        elif i.CodeStatus == "04":
            pattern = work_PatternsOfLetter.LostLinks()

        elif i.CodeStatus == "05":
            pattern = work_PatternsOfLetter.HaveAttachments()

        elif i.CodeStatus == "06":
            pattern = work_PatternsOfLetter.SystemFailure()

        elif i.CodeStatus == "07":
            pattern = work_PatternsOfLetter.SystemFailure()

        elif i.CodeStatus == "08":
            pattern = work_PatternsOfLetter.UncorrectedLink()

        elif i.CodeStatus == "10":
            pattern = work_PatternsOfLetter.WorkCompleted()

        elif i.CodeStatus == "30":
            pattern = work_PatternsOfLetter.WorkVerified(i.IsOK)
            par = (i.Student.NameOfStudent, i.NumberOfLab, i.VariantOfLab)
            forTeacher.add(par)
            teacher = True

        else:
             flag = True

        if flag == False:  
            answer = AnswersForUsers(i.Student.Email, pattern.return_theme(), pattern.return_body())
            answers.append(answer)

        flag = False

    if teacher == True:
        answer = AnswersForUsers(cfg.teacher_email, forTeacher.return_theme(), forTeacher.return_body())
        answers.append(answer)

    return answers
