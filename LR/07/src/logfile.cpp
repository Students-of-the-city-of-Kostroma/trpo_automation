#include "logfile.h"

/**
 * @brief Конструктор
 */
logfile::logfile()
{

}

/**
 * @brief Метод создания лога типа Info
 * @param Сообщение лога
 */
void logfile::logInfo(QString msg) {
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
void logfile::logDebug(QString msg) {
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
void logfile::logWarning(QString msg) {
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
void logfile::logCritical(QString msg) {
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
void logfile::logFatal(QString msg) {
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
