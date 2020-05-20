import datetime
import config_Project as cfg

class BasePattern:
    Theme = None
    TopPart = ("Доброе утро.\n\n", "Добрый день.\n\n", "Добрый вечер.\n\n", "Доброй ночи.\n\n")
    MainPart = None
    BottomPart = "\nСпасибо за использование нашей системы.\n\nКонтакты тех. поддержки: " + cfg.teacher_email + "."

    def return_body(self):
        now = datetime.datetime.now()
        if now.hour > 5 & now.hour <= 10:
            return self.TopPart[0] + self.MainPart + self.BottomPart
        elif now.hour > 10 & now.hour <= 16:
            return self.TopPart[1] + self.MainPart + self.BottomPart
        elif now.hour > 16 & now.hour <= 22:
            return self.TopPart[2] + self.MainPart + self.BottomPart
        else:
            return self.TopPart[3] + self.MainPart + self.BottomPart

    def return_theme(self):
        return self.Theme


class UnknownUser(BasePattern):
    Theme = "Пользователь не найден."
    MainPart = "Ваше письмо было получено, но вас нет в журнале учащихся. Пожалуйста, заполните форму\n" \
               "для вашей регистрации в журнале учащихся и отправьте письмо повторно.\n" \
               "Без этого вы не сможете сдать свои работы дистанционно.\n\n" \
               "Форма: "+ cfg.access + " .\n"


class UncorrectedTheme(BasePattern):
    Theme = "Задание с таким названием не существует."
    MainPart = "Ваше письмо было получено, но вы неверно указали тему. Возможно, это случилось из-за того, что вы \n" \
               "неверно указали номер или название. Поэтому пожалуйста, убедитесь, что номер задания соответствует \n" \
               "заданию и вы правильно указали название задание. После можете отправить письмо повторно.\n"


class WorkCompleted(BasePattern):
    Theme = "Ваша работа уже была проверена.\n"
    MainPart = "Ваша работа уже прошла проверку и зачтена, поэтому вам не надо больше отправлять на проверку.\n"


class UncorrectedStructure(BasePattern):
    Theme = " Ваше письмо не соответствует требованиям к оформлению письма."
    MainPart = "Ваше письмо было получено, но письмо не соответствует требованиям. Возможно, это случилось из-за \n" \
               "того, что вы пользуетесь нашей системой впервые и не были ознакомлены с требованиями к оформлению \n" \
               "писем. Пожалуйста, прочитайте правила оформления писем и проверьте, что вы могли забыть\n" \
               "при написании письма.\n"


class LostLinks(BasePattern):
    Theme = "В письме нет необходимых ссылок."
    MainPart = "Ваше письмо было получено, но в письме не хватает требуемых ссылок. \n" \
               "Проверьте, добавили все необходимые ссылки, и отправьте письмо повторно.\n"


class HaveAttachments(BasePattern):
    Theme = "В письме есть вложения."
    MainPart = "Ваше письмо было получено, но в письме есть вложений. Проверьте, что удалили все вложения, \n" \
               "заменив их на ссылки, и отправьте письмо повторно.\n"


class WorkVerified(BasePattern):
    Theme = "Ваша работа проверена."

    def __init__(self, parameter):
        if parameter:
            self.MainPart = "Ваша работа проверена, оценка: зачтено. Если ваша работа \n" \
                            "не зачтена, вы можете отправить работу на проверку повторно, после исправлений ошибок. \n"
        else:
            self.MainPart = "Ваша работа проверена, оценка: не зачтено. Если ваша работа \n" \
                            "не зачтена, вы можете отправить работу на проверку повторно, после исправлений ошибок. \n"


class SystemFailure(BasePattern):
    Theme = " Система временно недоступна."
    MainPart = "Извините, но в данный момент система не может проверить вашу работу. Поэтому, пожалуйста, немного \n" \
               "подождите и отправьте письмо повторно.\n"


class UncorrectedVariant(BasePattern):
    Theme = "В письме неверно указан вариант работы."
    MainPart = "Ваше письмо было получено, но в письме неверно указан номер варианта. Проверьте, что вы верно \n" \
               "указали свой вариант. Вариант должен входить в диапазон от 1 до 15 и содержит только цифры. \n"


class ForTeacher(BasePattern):
    Theme = "Данные в журнале были изменены."
    MainPart = ""

    def add(self, parameter):
        self.MainPart += parameter[0] + " сдал Работу номер " + parameter[1] + ' ' + parameter[2] + '.\n'