#ifndef TESTGATEWAY_H
#define TESTGATEWAY_H

#include "../src/utils/gateway.h"
#include "../src/utils/internalexception.h"

#include <QObject>
#include <QtTest/QtTest>

static const int COLUMN_INDEX_FOR_TEST_DATA = 3;
static const int COLUMN_INDEX_FOR_EXPECTED_DATA = 6;
static const int COLUMN_INDEX_FOR_CASE_DESCRIPTION = 2;

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

private slots:
    void testTrueJson();
    void testSuite_data();
    void testSuite();
    void cleanupTestCase();
};

#endif // TESTGATEWAY_H
