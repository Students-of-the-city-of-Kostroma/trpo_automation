#ifndef TESTSTARTEGYLABCHECKCHIKDREN_H
#define TESTSTARTEGYLABCHECKCHIKDREN_H

#include "ITestModule.h"

class TestStrategyLabCheckChikdren : public ITestModule
{
    Q_OBJECT

private:
    StrategyLab *testObject;

public:
    TestStrategyLabCheckChikdren(): ITestModule(QRegExp("issue-173-[0-9]{1,3}"),  [this](QByteArray testData) -> QString {
//        testObject = new Gateway();

//        // Возвращаем на случай, когда метод отработает без исключений
//        return QString(testObject->validateData(testData).toJson(QJsonDocument::Compact));
    }) {}

    ~TestStrategyLabCheckChikdren() {
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

#endif // TESTSTARTEGYLABCHECKCHIKDREN_H
