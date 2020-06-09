#ifndef TESTSTRATEGYLAB_H
#define TESTSTRATEGYLAB_H

#include "../src/components/strategylab.h"
#include "../src/utils/internalexception.h"


#include <QObject>
#include <QtTest/QtTest>

/**
 * @brief Класс тестирования проверок StrategyLab
 */
class TestStrategyLab : public QObject
{
    Q_OBJECT

private:
    StrategyLab *testObj;
    QDomElement suites;

public:
    explicit TestStrategyLab(QObject *parent = nullptr);

private slots:
    void testCheckChildren_data();
    void testCheckChildren();
    void cleanupTestCase();
};

#endif // TESTSTRATEGYLAB_H
