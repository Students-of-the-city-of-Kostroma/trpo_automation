QT += testlib network xml
QT -= gui

CONFIG += c++11

SOURCES += \
    ../src/utils/gateway.cpp \
    ../src/components/strategylab.cpp \
    ../src/utils/internalexception.cpp \
    ITestModule.cpp \
    main.cpp



HEADERS += \
    ../src/utils/gateway.h \
    ../src/components/strategylab.h \
    ../src/utils/internalexception.h \
    ITestModule.h \
    TestGateway.h \
    TestStartegyLabCheckChikdren.h


RESOURCES += \
    ../src/resources.qrc
