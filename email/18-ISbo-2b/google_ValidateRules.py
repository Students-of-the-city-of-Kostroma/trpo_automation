import re


class ValidationMail():

    def __init__(self, subject, body):
        self.subject = subject
        self.body = body
        self.success = False

    @staticmethod
    def validation_subject(subject):
        """
        Проверяет соответствие структуре темы. Включается в общий метод валидации
        :param subject: Тема письма
        :return: Успех валидации
        """
        subject = subject.lower().replace(' ', '')
        if subject[0:4] != "трпо":
            return '01'
        index_v = subject.find("вар", 0, len(subject))
        if index_v == -1:
            return '01'
        index_l = subject.find("лр", 0, len(subject))
        if index_l == -1:
            return '01'
        variant = subject[-2:]
        if variant.isdigit() is not True and variant[1].isdigit() is not True:
            return '03'
        number_work = subject[index_l + 2:index_l + 5]
        if number_work[0].isdigit() is not True:
            number_work = number_work[1:]
        else:
            number_work = number_work[:2]
        if number_work.isdigit() is not True and number_work[0].isdigit() is not True:
            return '03'
        else:
            return '20'

    @staticmethod
    def validation_body(body):
        """
        Проверяет соответствие структуре тела письма. Включается в общий метод валидации
        :param body: Тело письма
        :return: Успех валидации
        """
        salutation = ['здравствуйте', 'добрый', 'доброго', 'привет']
        links = []
        strings = body.split('\n')
        for item in strings:  # Убираю все лишнее
            if item == "" or item == "--" or item == '\r':
                strings.remove(item)
        hello = re.match(r'\w+', strings[0])
        hello = hello.group(0).lower()
        if (hello in salutation) is False:
            return '02'
        name = strings[len(strings) - 1]  # Это подпись
        name = name.replace("\r", "")
        res = re.match(r'\w+[ ]?\w+[, ]{2}\d{2}[-]?\w{4}[-]?\d\w', name)
        if res is None:
            return '02'
        for item in strings:  # Проверяю ссылки
            pattern = re.findall(r'https://[^ ]*', item)
            if len(pattern) != 0:
                links.append(pattern)
        if len(links) == 0:  
            return '04'
        if body.find('http', 0, len(body)) != body.rfind('http', 0, len(body)):
            return '04'
        return '20'

    def validation(self, subject, body):
        """
        Проверяет тему и тело письма на соответствие структуре
        :param subject: Тема письма
        :param body: Тело письма
        :return: Устпех валидации
        """
        if self.validation_subject(subject) == '20' and self.validation_body(body) == '20':
            self.success = True
            return '20'
        elif self.validation_subject(subject) == '20':
            return self.validation_body(body)
        else:
            return self.validation_subject(subject)

        def get_num_and_var(self, subject):
        if self.success is True:
            subject = subject.lower().replace(' ', '')
            var = subject[-2:]
            if var.isdigit() is not True or var[0] == '0':
                var = var[1]
            index = subject.find("лр", 0, 10)
            number_work = subject[index + 2:index + 5]
            if number_work[0].isdigit() is not True or number_work[0] == '0':
                number_work = number_work[1:]
            else:
                number_work = number_work[:2]
            if number_work.isdigit() is not True:
                number_work = number_work[0]

            return number_work, var
        else:
            return None

    def verify_name_and_group(self, main_name, main_group):
        strings = self.body.split('\n')

        count = strings.count("")
        for i in range(count):
            strings.remove("")

        name = strings[len(strings) - 1]
        res = re.match(r'\w+[ ]?\w+[, ]{2}\d{2}[-]?\w{4}[-]?\d\w', name)
        res = res.group(0).lower()
        res = res.split(',')
        res[1] = res[1].strip()
        main_name = main_name.lower()
        main_group = main_group.lower()
        if (main_name.find(res[0], 0, len(main_name)) == -1) or (main_group.find(res[1], 0, len(main_group)) == -1):
            return False
        else:
            return True
