#include "TestGateway.h"
#include <QtTest/QtTest>

int main(int argc, char *argv[])
{
   int status = 0;

   {
       TestGateway testClass;
       status |= QTest::qExec(&testClass, argc, argv);
   }

   return status;
}
