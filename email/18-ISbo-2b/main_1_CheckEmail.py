# coding=utf-8
from work_Sheet import Sheet
from global_Letter import Letter
from global_User import User
from work_ValidateRules import ValidationMail as Val
from work_Loger import Logs
import work_EmailLibrary as EmailLibrary

import inspect
import re
import email



def CheckEmail():
    """
    Точка входа в работу модуля.
    Первая функция-контроллер
    Чтение писем, их парсинг и валидация.
    """

    # Получение писем с почты
    # Создание IMAP объекта
    imap_obj = EmailLibrary.imap_login()

    # Получение списка сырых писем
    raw_letters = GetLetters(imap_obj)
    letters = []

    if len(raw_letters) > 0:
        for item in raw_letters:
            # Создание списка с информацией из писем
            # Глобальная функция 1
            letters.append(FormListWithLetters(item))

    # Закрытие IMAP объекта
    EmailLibrary.quit_email_imap(imap_obj)

    # Проверка пользователей на существование в системе
    # Глобальная функция 2
    CheckUsers(letters)

    # Валидация писем
    # Глобальная функция 3
    ValidateLetters(letters)

    return letters


def GetLetters(mail):
    """
    Функционал:
    - Прочитать письма на почте
    - Пометить прочитанные письма метками
    На входе:
    - None
    На выходе:
    - letters - объект, содержащий письма
    Что предусмотреть:
    - None
    Участвующие внешние типы переменных
    - None
    """
    # logs = Logs()
    # name = inspect.currentframe().f_code.co_name
    # logs.Infor(name, mail)

    # Количество непрочитанных писем
    count = EmailLibrary.count_unseen_mess(mail)
    letters = []

    if count > 0:
        # Выполняет поиск и возвращает UID писем.
        result, data = mail.uid('search', None, "unseen")
        print(count)

        for i in range(count):
            latest_email_uid = data[0].split()[i]

            # Извлечение информации по заданному UID
            result, date = mail.uid('fetch', latest_email_uid, '(RFC822)')

            # Получение сырого письма
            raw_email = date[0][1]

            # Добавление сырого письма в список
            letters.append(raw_email)

    else:
        pass

    return letters


def FormListWithLetters(mails):
    """
    Функционал:
    - Сформировать список экземпляров класса Letter на основе сырых данных по письмам
    На входе:
    - Объект с сырыми данными по письмам
    На выходе:
    - Список экземпляров класса Letter
    Что предусмотреть:
    - Парсинг сырых данных
    - Декодирование сырых данных
    - Заполнение всех полей в Letter на основе обработанной информации кроме 'Code' и 'CodeComment'
    - Поля 'Code' и 'CodeComment' заполняются только в случае существующего приложения к письму (что противоречит
    правилам отправки писем)
    - Заполнение поля User - вытаскивание всех данных о конкретном пользователе (кроме поля isRegistered)
    Участвующие внешние типы переменных
    - User (from import)
    - Letter (from import)
    """
    # logs = Logs()
    # name = inspect.currentframe().f_code.co_name
    # logs.Infor(name, mails)

    try:
        try:
            # Преобразуем сырое письмо в экземпляр класса Email
            email_message = email.message_from_string(mails)

        except TypeError:
            email_message = email.message_from_bytes(mails)

        error_code = ""

        # Извлечение информации об отправителе
        from_mes = EmailLibrary.get_from(email_message)

        # Извлечение информации о теме письма
        subject_mes = EmailLibrary.get_subject(email_message)

        # Извлечение электронного адреса отправителя
        user_email = EmailLibrary.from_parse(from_mes)

        # Извлечение ФИ отправителя
        user_name = EmailLibrary.name_parse(from_mes)

        # Извлечение закодированного тела письма
        body_str = EmailLibrary.get_body(email_message)

        # Декодировка тела письма
        body = EmailLibrary.body_parse(body_str)
        if body == "UNKNOWN":
            error_code = "05"

        user = User(user_name, None, user_email, None)
        letter_item = Letter(user, subject_mes, body, None, None)
        letter_item.CodeStatus = error_code

        return letter_item

    except:
        user = User("UNKNOWN", None, "UNKNOWN", None)
        letter = Letter(user, "UNKNOWN", "UNKNOWN", None, None)
        letter.CodeStatus = "07"
        return letter


def CheckUsers(letters):
    """
    Функционал:
    - Проверить зарегистрированность каждого пользователя в системе по email
    На входе:
    - Список писем
    На выходе:
    - Расставленное поле 'isRegistered' в каждом письме в поле 'User'
    Что предусмотреть:
    - None
    Участвующие внешние типы переменных
    - None
    """
    # logs = Logs()
    # name = inspect.currentframe().f_code.co_name
    # logs.Infor(name, letters)

    for i in letters:
        if i.CodeStatus == "":
            result = Sheet.check_email(i.Student.Email)

            if not result:
                i.CodeStatus = "00"
                i.CodeStatusComment = "Пользователь не зарегистрирован"
            else:
                i.Student.IsRegistered = True
                i.Student.NameOfStudent = '{} {} {}'.format(result[0][0], result[0][1], result[0][2])
                i.Student.GroupOfStudent = '{}'.format(result[0][3])


def ValidateLetters(letters):
    """
    Функционал:
    - Провалидировать каждое письмо по правилам валидации
    На входе:
    - Список писем
    На выходе:
    - Расставленные поля 'Code' и 'CodeComment' в каждом письме
    Что предусмотреть:
    - Просле проверки вытащить ссылки на ресурсы и поместить их в поле 'Body' каждого письма
    - Проверку выполнять только если поле 'Code' ещё не заполнено
    - Поле 'CodeComment' заполнять сокращённой информацией по результатам проверки как угодно.
    Участвующие внешние типы переменных
    - None
    """
    # logs = Logs()
    # name = inspect.currentframe().f_code.co_name
    # logs.Infor(name, letters)

    for let in letters:
        if let.CodeStatus is None or let.CodeStatus == "":
            val = Val(let.ThemeOfLetter, let.Body)
            let.CodeStatus = val.validation(val.subject, val.body)

            if let.CodeStatus == '20':
                if val.verify_name_and_group(let.Student.NameOfStudent, let.Student.GroupOfStudent) is not True:
                    let.CodeStatus = '02'
                    let.CodeStatusComment = 'Подпись не соответствует заявленной при регистрации'

            if let.CodeStatus == '01':
                let.CodeStatusComment = 'Тема письма не соответствует требованиям к теме'

            elif let.CodeStatus == '02':
                if let.CodeStatusComment is None:
                    let.CodeStatusComment = 'Структура письма не соответствует требованиям к оформлению'

            elif let.CodeStatus == '03':
                let.CodeStatusComment = 'Неверно указан номер работы или варианта'

            elif let.CodeStatus == '04':
                let.CodeStatusComment = 'Письмо не содержит необходимых ссылок на ресурсы.'

            else:
                num, var = val.get_num_and_var(val.subject)
                if num is None or (int(var) > 15 or int(num) > 12 or int(var) == 0):
                    let.CodeStatus = '03'
                    let.CodeStatusComment = 'Номер лабораторной не существует'

                else:
                    let.NumberOfLab = int(num)
                    let.VariantOfLab = int(var)

            if let.CodeStatus == '20':
                let.Body = re.findall(r'http[^ \n]*', let.Body)[0]
                body = let.Body[-1:]

                if body == "\r":
                    let.Body = let.Body[:-1]

                let.CodeStatusComment = 'Работа отправлена на проверку'
