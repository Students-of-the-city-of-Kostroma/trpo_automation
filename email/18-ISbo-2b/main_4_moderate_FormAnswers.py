# coding=utf-8
import inspect	
from Loger import Logs 	
logs = Logs()	
name = None	

from time import sleep
from datetime import datetime

from global_AnswersForUsers import AnswersForUsers
from main_5_send_InformUsers import InformUsers
import config_Project as cfg
import moderate_PatternsOfLetter

def FormAnswers(letterResult):
    name = inspect.currentframe().f_code.co_name	
    logs.Infor(name,letterResult)
    """
    Формирование ответов пользователям
    """
    # Формирование ответов пользователю
    answers = MakeAnswersForUsers(letterResult)

    # Вызов функции информирования пользователей
    InformUsers(answers)


def MakeAnswersForUsers(letterResult):
    name = inspect.currentframe().f_code.co_name	
    logs.Infor(name,letterResult)
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
    with open(cfg.filename, "a") as file:
        file.write("\nФормирование ответов пользователю... ")

    answers = []
    teacher = False
    forteacher = moderate_PatternsOfLetter.ForTeacher()
    for i in letterResult:
        if letterResult[i].CodeStatus == "00":
            pattern = moderate_PatternsOfLetter.UnknownUser()
        elif letterResult[i].CodeStatus == "01":
            pattern = moderate_PatternsOfLetter.UncorrectedTheme()
        elif letterResult[i].CodeStatus == "02":
            pattern = moderate_PatternsOfLetter.UncorrectedStructure()
        elif letterResult[i].CodeStatus == "03":
            pattern = moderate_PatternsOfLetter.UncorrectedVariant()
        elif letterResult[i].CodeStatus == "04":
            pattern = moderate_PatternsOfLetter.LostLinks()
        elif letterResult[i].CodeStatus == "05":
            pattern = moderate_PatternsOfLetter.HaveAttachments()
        elif letterResult[i].CodeStatus == "06":
            pattern = moderate_PatternsOfLetter.SystemFailure()
        elif letterResult[i].CodeStatus == "07":
            pattern = moderate_PatternsOfLetter.SystemFailure()
        elif letterResult[i].CodeStatus == "10":
            pattern = moderate_PatternsOfLetter.WorkCompleted()
        elif letterResult[i].CodeStatus == "30":
            pattern = moderate_PatternsOfLetter.WorkVerified(letterResult[i].IsOk)
            par = (letterResult[i].Student.NameOfStudent, letterResult[i].NumberOfLab, letterResult[i].VariantOfLab)
            forteacher.add(par)
            teacher = True
        answer = AnswersForUsers(letterResult[i].Student.email, pattern.return_theme(), answers[i])
        answers.append(answer)
    sleep(1)
    if teacher == True:
        answer = AnswersForUsers(cfg.teacher_email, forteacher.return_theme(), forteacher.return_body())
        answers.append(answer)

    with open(cfg.filename, "a") as file:
        file.write("Ответы для пользователей сформированы!")

    return answers
