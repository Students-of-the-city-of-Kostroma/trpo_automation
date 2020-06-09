#include "testgateway.h"
#include "teststrategylab.h"

int main(int argc,char* argv[])
{
    int status = 0;
   {
        TestGateway tg;
        status |= QTest::qExec(&tg, argc, argv);
   }
   {
        TestStrategyLab tsl;
        status |= QTest::qExec(&tsl, argc, argv);
    }
    return status;
}
