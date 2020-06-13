#ifndef TESTGATEWAY_H
#define TESTGATEWAY_H

#include "ITestModule.h"

class TestGateway : public ITestModule
{
    Q_OBJECT

private:
    Gateway *testObject;

public:
    TestGateway(): ITestModule(QRegExp("issue-393-[0-9]{1,3}"),  [this](QString testData) -> QString {
        testObject = new Gateway();

        // Возвращаем на случай, когда метод отработает без исключений
        return QString(testObject->validateData(QByteArray(testData.toStdString().c_str())).toJson(QJsonDocument::Compact));
    }) {}

    ~TestGateway() {
        delete testObject;
    }

private slots:
    void testSuite_data() {
        ITestModule::testSuite_data();
    }

    void testSuite() {
        ITestModule::testSuite();
    }
};

#endif // TESTGATEWAY_H
