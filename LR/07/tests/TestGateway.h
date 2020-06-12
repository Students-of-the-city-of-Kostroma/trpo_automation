#ifndef TESTGATEWAY_H
#define TESTGATEWAY_H

#include "ITestModule.h"

#include <QObject>

const static QString REGEX_CASE_ID = "issue-393-[0-9]{1,3}";

class TestGateway : public ITestModule
{

private:
    Gateway *testObject;

public:
    TestGateway(): ITestModule(REGEX_CASE_ID) {}

    ~TestGateway() {}
};

#endif // TESTGATEWAY_H
