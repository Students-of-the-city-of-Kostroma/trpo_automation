#ifndef TESTSTARTEGYLABCHECKCHIKDREN_H
#define TESTSTARTEGYLABCHECKCHIKDREN_H

#include "ITestModule.h"

class TestStrategyLabCheckChikdren : public ITestModule
{
    Q_OBJECT

private:
    StrategyLab *testObject;

public:
    TestStrategyLabCheckChikdren(): ITestModule(QRegExp("issue-173-[0-9]{1,3}"),  [this](QString testData) -> QString {
        testObject = new StrategyLab();

        // TODO номер варината должен браться из тестовых данных - переделать!
        testObject->setVariablesFromConfig(1);
        testObject->divideIntoClasses(testData.split("|||"));
        testObject->checkChildren();
        return QString();
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
