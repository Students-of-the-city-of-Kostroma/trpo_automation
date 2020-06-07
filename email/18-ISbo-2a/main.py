from utils.crypto import crypt_file, decrypt_file

decrypt_file('configs/credentials.json.bin')
decrypt_file('configs/Example.json.bin')
decrypt_file('configs/config.py.bin')
decrypt_file('configs/token.pickle.bin')

from APIgoogle import *
from Validation import validation
from utils.log_method import *

# Id почты
USER_ID = 'me'
# Получение сервиса
# Если не работает get_service, то token закинуть новый.
service = get_service()

try:
    while True:
        # Получение информации о последнем письме
        message_info = get_message(service, USER_ID)
        logger.info(r"main: Get message from email")
        print(r"main: Get message from email")

        # Проверка на существование активных писем в электронном ящике
        if message_info:
            email_id = message_info['email_id']
            email_name = cleaning_email(email_id)
            email_name_surname = name_surname(email_id)
            email = search_email(email_id)

            # Проверка на существование в таблице
            if not email:
                send_message(service, USER_ID, email_name, email_name_surname, 3, None, None, message_info)
                logger.warning(r"main: Email don't exist in table_valid")
                print(r"main: Email don't exist in table_valid")
            else:
                # Получение группы пользователя
                result = search_group(email)
                group_user = result[0]
                group_name_surname = result[1]
                # Выставление его в журнал, если отсутствует
                result_add_table = add_table(group_user, group_name_surname)[0]

                if result_add_table == 'available' or result_add_table == 'accepted':
                    # Проверка валидации письма
                    valid_dict = validation(message_info['head_of_msg'], message_info['body_of_msg'])
                    if len(valid_dict["errorDescription"]) > 0:
                        send_message(service, USER_ID, email_name, email_name_surname, 2, valid_dict,
                                     valid_dict, message_info)
                        logger.warning(r"main: Message failed validation. Email_id :%s" % email_id)
                        print(f"main: Message failed validation. Email_id :{email_id}")
                    else:
                        # Получение результата из модуля проверки
                        answer = 1 # check_lab(valid_dict['URL'], valid_dict['Number'])['grade']
                        logger.info(
                            r"main: Receiving a response from the verification module. Mark in table :%s" % answer)
                        print(f"main: Receiving a response from the verification module. Mark in table :{answer}")

                        # Получение ячейчки для выставления
                        table_cell = search_tablic(group_user, valid_dict['Number'], group_name_surname)
                        logger.info(r"main: Get user's table cell for add mark")
                        print(r"main: Get user's group and table")

                        # Лабораторная неправильно сделана
                        if answer == 0:
                            send_message(service, USER_ID, email_name, email_name_surname, 1, answer, None,
                                         message_info)
                            logger.warning(f'main: Lab done wrong from {email_id}')
                            print('main: Lab done wrong from %s' % email_id)
                        # Лабораторная сделана правильно
                        else:
                            add_str_in_table(group_user, table_cell, 1)
                            send_message(service, USER_ID, email, email_name_surname, 0, valid_dict, None, message_info)
                            logger.info('main: Lab done right from %s' % email_id)
                            print(f'main: Lab done wrong from {email_id}')
                else:
                    send_message_to_techsub(service, USER_ID, email_name, email_name_surname, None,
                                            {'message': 'все сломалось!'}, 1)
                    logger.info('main: Error with add in table %s' % email_id)
                    print(f'main: Error with add in table {email_id}')
            email_archiving(service, USER_ID, message_info)
            print(f'main: Archive message {email_id}')
        else:
            logger.info('main: Service asleep and wait new message')
            print('main: Service asleep and wait new message')
            time.sleep(1)
except:
    send_message_to_techsub(service, USER_ID, email_name, email_name_surname, None, {'message': 'все сломалось!'}, 0)

crypt_file(r'configs/token.pickle')
crypt_file(r'configs/Example.json')
crypt_file(r'configs/credentials.json')
crypt_file(r'configs/config.py')