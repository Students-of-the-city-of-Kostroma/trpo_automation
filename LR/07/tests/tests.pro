QT += testlib network xml
QT -= gui

CONFIG += c++11

SOURCES += \
    testgateway.cpp \
    ../src/utils/gateway.cpp \
    ../src/utils/internalexception.cpp \
    testmain.cpp \
    teststrategylab.cpp \


HEADERS += \
    testgateway.h \
    ../src/utils/gateway.h \
    ../src/utils/internalexception.h \
    teststrategylab.h

RESOURCES += \
    ../src/resources.qrc
