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
class Tests : public QObject
{
    Q_OBJECT

private:
    Gateway *testObj;
    StrategyLab *testObjj;
    QDomElement suites;

public:
    explicit Tests(QObject *parent = nullptr);

private slots:
    void testSuite_data(QDomElement, QRegExp);
    void testSuite(QDomElement);
};

#endif // TESTGATEWAY_H
