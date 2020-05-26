#ifndef LOGFILE_H
#define LOGFILE_H

#include<QFile>
#include<QTextStream>
#include<QDateTime>

class logfile
{
public:
    logfile();
    void logInfo(QString Msg);
    void logDebug(QString Msg);
    void logWarning(QString Msg);
    void logCritical(QString Msg);
    void logFatal(QString Msg);
};

#endif // LOGFILE_H
