from APIgoogle import *
from log_method import *
import client
import Validation
import config
import time

# Id почты
USER_ID = 'me'
# Получение сервиса
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
                # Проверка валидации письма
                valid_dict = Validation.validation(message_info['head_of_msg'], message_info['body_of_msg'])
                if len(valid_dict["errorDescription"]) > 0:
                    send_message(service, USER_ID, email_name, email_name_surname, 2, None, valid_dict, message_info)
                    logger.warning(r"main: Message failed validation. Email_id :%s" % email_id)
                    print(f"main: Message failed validation. Email_id :{email_id}")
                else:
                    # Получение результата из модуля проверки
                    answer = client.send_a_laboratory_work_for_verification(labNumber=valid_dict['Number'],
                                                                            labLink=valid_dict['URL'])
                    logger.info(r"main: Receiving a response from the verification module. Mark in table :%s" % answer)
                    print(f"main: Receiving a response from the verification module. Mark in table :{answer}")

                    # Получение группы и таблицы пользователя
                    group_user = search_group(email)
                    table_cell = search_tablic(data_user[0], valid_dict['Number'], data_user[1])
                    logger.info(r"main: Get user's group and table")
                    print(r"main: Get user's group and table")

                    # Лабораторная неправильно сделана
                    if answer == 0:
                        send_message(service, USER_ID, email_name, email_name_surname, 1, answer, None, message_info)
                        logger.warning(f'main: Lab done wrong from {email_id}')
                        print('main: Lab done wrong from %s' % email_id)
                    # Лабораторная сделана правильно
                    else:
                        add_mark_in_table(data_user[0], cell, 1)
                        send_message(service, USER_ID, email, email_name_surname, 0, None, None, message_info)
                        logger.info('main: Lab done right from %s' % email_id)
                        print(f'main: Lab done wrong from {email_id}')

            email_archiving(service, USER_ID, message_info)
        else:
            logger.info('main: Service asleep and wait new message')
            print('main: Service asleep and wait new message')
            time.sleep(1000)
except:
    send_message_to_techsub(service, USER_ID, email_name, email_name_surname, None, {'message': 'все сломалось!'}, 1)
