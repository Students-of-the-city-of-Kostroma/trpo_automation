#include "internalexception.h"
#include "logfile.h"

/**
 * @brief Метод формирует сообщение об ошибке
 * @param explanation - человеческое оъяснение проблемы
 * @param systemError - системный вывод сообщения об ошибке
 */
void InternalException::formatMessage(QString explanation, QString systemError)
{
    logfile::logInfo("format Message");

    errorMessage = explanation;
    if (!systemError.isEmpty()) {
        errorMessage += ". System output: " + systemError;
    }
}
