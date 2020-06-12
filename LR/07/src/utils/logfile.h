#ifndef LOGFILE_H
#define LOGFILE_H

#include<QFile>
#include<QTextStream>
#include<QDateTime>


/**
 * @brief Класс - система логирования
 */
class logfile
{
public:
    logfile();
    static void logInfo(QString Msg);
    static void logDebug(QString Msg);
    static void logWarning(QString Msg);
    static void logCritical(QString Msg);
    static void logFatal(QString Msg);
};

#endif // LOGFILE_H
