#include "TestGateway.h"
#include "TestStartegyLabCheckChikdren.h"

int main(int argc, char *argv[])
{
   int status = 0;

   {
       TestGateway gateway;
       status |= QTest::qExec(&gateway, argc, argv);
   }

   {
       TestStrategyLabCheckChikdren checkChildren;
       status |= QTest::qExec(&checkChildren, argc, argv);
   }

   return status;
}
