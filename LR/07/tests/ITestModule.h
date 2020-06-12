#ifndef TESTGATEWAY_H
#define TESTGATEWAY_H

#include "../src/utils/gateway.h"
#include "../src/components/strategylab.h"
#include "../src/utils/internalexception.h"

#include <QObject>
#include <QtTest/QtTest>

/**
 * @brief Класс тестирования сервиса Gateway
 */
class ITestModule
{
protected:
    QDomElement suites;
    QRegExp regexCaseId;

protected:
    ITestModule(QRegExp);

protected slots:
    void testSuite_data();
    void testSuite();
};

#endif // TESTGATEWAY_H
