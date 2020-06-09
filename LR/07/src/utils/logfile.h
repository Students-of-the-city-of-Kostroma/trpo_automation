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

    /**
     * @brief Метод создания лога типа Info
     * @param Сообщение лога
     */
    static void logInfo(QString msg) {
        QFile logFile("logFile.txt");
        if(logFile.open(QIODevice::Append | QIODevice::Text)) {
            QTextStream writeStream(&logFile);
            writeStream << QDateTime::currentDateTime().toString("yyyy-MM-dd hh:mm:ss.zzz ");
            writeStream << "INF ";
            writeStream << "Info: ";
            writeStream << msg;
            writeStream << "\n";
            logFile.close();
        }
    }

    /**
     * @brief Метод создания лога типа Debug
     * @param Сообщение лога
     */
    static void logDebug(QString msg) {
        QFile logFile("logFile.txt");
        if(logFile.open(QIODevice::Append | QIODevice::Text)) {
            QTextStream writeStream(&logFile);
            writeStream << QDateTime::currentDateTime().toString("yyyy-MM-dd hh:mm:ss.zzz ");
            writeStream << "DBG ";
            writeStream << "Debug: ";
            writeStream << msg;
            writeStream << "\n";
            logFile.close();
        }
    }

    /**
     * @brief Метод создания лога типа Warning
     * @param Сообщение лога
     */
    static void logWarning(QString msg) {
        QFile logFile("logFile.txt");
        if(logFile.open(QIODevice::Append | QIODevice::Text)) {
            QTextStream writeStream(&logFile);
            writeStream << QDateTime::currentDateTime().toString("yyyy-MM-dd hh:mm:ss.zzz ");
            writeStream << "WRN ";
            writeStream << "Warning: ";
            writeStream << msg;
            writeStream << "\n";
            logFile.close();
        }
    }

    /**
     * @brief Метод создания лога типа Critical
     * @param Сообщение лога
     */
    static void logCritical(QString msg) {
        QFile logFile("logFile.txt");
        if(logFile.open(QIODevice::Append | QIODevice::Text)) {
            QTextStream writeStream(&logFile);
            writeStream << QDateTime::currentDateTime().toString("yyyy-MM-dd hh:mm:ss.zzz ");
            writeStream << "CRT ";
            writeStream << "Critical: ";
            writeStream << msg;
            writeStream << "\n";
            logFile.close();
        }
    }

    /**
     * @brief Метод создания лога типа Fatal
     * @param Сообщение лога
     */
    static void logFatal(QString msg) {
        QFile logFile("logFile.txt");
        if(logFile.open(QIODevice::Append | QIODevice::Text)) {
            QTextStream writeStream(&logFile);
            writeStream << QDateTime::currentDateTime().toString("yyyy-MM-dd hh:mm:ss.zzz ");
            writeStream << "FTL ";
            writeStream << "Fatal: ";
            writeStream << msg;
            writeStream << "\n";
            logFile.close();
        }
    }
};

#endif // LOGFILE_H
