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
class TestGateway : public QObject
{
    Q_OBJECT

private:
    Gateway *testObj;
    QDomElement suites;

public:
    explicit TestGateway(QObject *parent = nullptr);

};

class TestStrategyLab : public QObject
{
    Q_OBJECT

private:
    StrategyLab *testObj;
    QDomElement suites;

public:
    explicit TestStrategyLab(QObject *parent = nullptr);

};

#endif // TESTGATEWAY_H
