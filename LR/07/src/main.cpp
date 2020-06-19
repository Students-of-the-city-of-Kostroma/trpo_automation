#include <QCoreApplication>
#include "components/tcpserver.h"

static const int LAB_NUMBER = 7;

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    logfile log;

    log.logInfo("<==================================================================================================="
                "============================================>");
    log.logInfo("<==================================================================================================="
                "============================================>");
    log.logInfo("Programm start work");
    TcpServer* server = new TcpServer(LAB_NUMBER);

    return a.exec();
}
