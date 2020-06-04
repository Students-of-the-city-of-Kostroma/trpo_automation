"""
Шаблоны для заполнения писем
"""


def funcSt(str_of_val_er, str_of_er):   
    pattern = [
        {
             'title': 'ТРПО. Работа успешно принята',
             'our_msg': 'Поздравляю!\nРабота успешно принята!' +
                        '\nОценку можно проверить в журнале:' +
                        '\nhttps://docs.google.com/spreadsheets/d/1gOX8T8ihy3J1khhC16U1qDwaI-K6ndkp9LFWAHncuWA' +
                        '/edit?usp=sharing'
        },
        {
            'title': 'ТРПО. Обнаружены ошибки в работе',
            'our_msg': 'В Вашей работе обнаружены ошибки:\n\n' + str_of_val_er +
                       '\nПросьба исправить их и отправить письмо повторно.'
        },
        {
            'title': 'ТРПО. Обнаружены ошибки в заполнении письма',
            'our_msg': 'В структуре письма обнаружены следующие ошибки:\n\n' +
                       str_of_er + '\nПросьба исправить их в соответствии с ' +
                       'документом\n' + 'https://docs.google.com/document/d/' +
                       '1DRhgepxVwoscylIS2LCW-po5SFBdqOr-oo92bP_XfHE/edit?' +
                       'usp=sharing'
        },
        {
            'title': 'ТРПО. Авторизация пользователя',
            'our_msg': 'Вы не найдены в системе. Пожалуйста, перейдите по' +
                       ' ссылке и зарегистрируйтесь.\n'
                       'https://forms.gle/pNzAtYKWAiDom6MEA'
        },
        {
            'title': 'Ошибка модуля',
            'our_msg': 'В модуле ... обнаружена ошибка. В ближайшее время ' +
                       'проблема будет исправлена. Просим прощения за неудобства.'
        }
    ]
    return pattern


def funcTs(name_of_student, validation_dictionary, str_of_er):
    pattern = [
        {
            'hello': 'Здравствуйте, Юрий Викторович!\n\n',
            'title': 'ТРПО. Ошибка в работе студента',
            'our_msg': 'Студент ' + name_of_student +
                       ' не справился с задачей №' +
                       validation_dictionary['Numder'] +
                       ' (' + validation_dictionary['URL'] + ')' +
                       '\nБыли допущены ошибки в работе:\n\n' +
                       str_of_er
        },
        {
            'hello': 'Здравствуйте!',
            'title': 'ТРПО. Служба дала сбой',
            'our_msg': 'В модуле ... возникла ошибка ...'
        }
    ]
    return pattern


SIGNATURE = "\n\nС уважением,\nБот"

def funcReturnMsg(hello_student, our_msg, SIGNATURE, 
                   date_of_msg, return_body, return_head):
    date_part = f'\n\n-----\nRe: <{date_of_msg}>\n'
    return_part = date_part + f'Тема: {return_head}\n{return_body}\n-----'
    text_of_msg = hello_student + our_msg + return_part + SIGNATURE
    return text_of_msg

def funcHello(name_of_student):
    return 'Здравствуйте, '+ f'{name_of_student}' + '!\n\n'


GMAIL_OF_TRPO = "trpo.automation@gmail.com"


EMAIL_OF_TEACHER = 'yuri.silenok@gmail.com'


MAS_OF_TO = ['yuri.silenok@gmail.com', '0sashasmirnov0@gmail.com',
             'k.svyat395@gmail.com', 'MaXLyuT2000@gmail.com',
             'majishpro@gmail.com', 'Sirokko77@gmail.com',
             'nikita.lukyanow@gmail.com', 'generalgrigorevous@gmail.com', 
             'molchok.yurij@gmail.com', 'amr15319@gmail.com']


"""
Валидация
"""



GREATING_LIST =  ['добрый день','добрый вечер',# Список приветствий
                  'добрейший вечерочек','доброй ночи','здравствуйте','привет',
                  'здравия желаю','хаю хай','доброго времени суток'] 

