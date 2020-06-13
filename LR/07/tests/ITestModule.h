#ifndef ITESTMODULE_H
#define ITESTMODULE_H

#include "../src/utils/gateway.h"
#include "../src/components/strategylab.h"
#include "../src/utils/internalexception.h"

#include <QObject>
#include <QtTest/QtTest>

/**
 * @brief Класс тестирования сервиса Gateway
 */
class ITestModule : public QObject
{
    Q_OBJECT

protected:
    QDomElement suites;
    QRegExp regexCaseId;
    const std::function<QString(QByteArray)> callBack;

protected:
    ITestModule(QRegExp, const std::function<QString(QByteArray)> &);

protected slots:
    void testSuite_data();
    void testSuite();
};

#endif // ITESTMODULE_H
