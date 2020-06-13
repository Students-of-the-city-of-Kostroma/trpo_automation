#include "TestGateway.h"

int main(int argc, char *argv[])
{
   int status = 0;

   {
       TestGateway gateway;
       status |= QTest::qExec(&gateway, argc, argv);
   }

   return status;
}
