#include "logfile.h"

logfile::logfile()
{

}

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
