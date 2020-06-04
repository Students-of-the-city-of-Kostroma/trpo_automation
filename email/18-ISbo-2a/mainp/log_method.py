import logging_config as config
import logging

levels = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
}
logging.basicConfig(
    filename=config.filename,
    level=levels[config.level],
    format=config.format)

logger = logging.getLogger(__name__)


def log_method_info(method):
    """
    Декоратор, который выполняет логирование методов

    method - метод, который нужно залогировать
    """

    def write_logs(*args, **kwargs):
        """
        Выполняет логирование

        args, kwargs - параметры, которые нужно передать в метод
        """
        try:
            # Записываем вход в метод
            logger.info(f'Got into - {method.__name__}')
            # Выполняем метод, помещаем результат работы метода в result
            result = method(*args, **kwargs)
            # Записываем результат выполнения метода
            logger.debug(f'Method {method.__name__} has returned - {result}')
            logger.info(f'Method has completed - {method.__name__}')
            # Возвращаем значение, которое было получено из метода
            return result
        except Exception as ex:
            # Записываем в логи ошибку, если такая была
            logger.exception(ex)
            logger.error(f'Method has crashed - {method.__name__}')

    return write_logs


# Пример использования декоратора. Если он не нужен, то все, что ниже, можно просто удалить. Не будет выполняться при имортировании модуля
if __name__ == '__main__':
    @log_method_info
    def ananas():
        print('ananas')
        print(1 / 0)


    ananas()
