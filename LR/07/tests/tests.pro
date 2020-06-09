QT += testlib network xml
QT -= gui

CONFIG += c++11

SOURCES += \
    ../src/utils/gateway.cpp \
    ../src/components/strategylab.cpp \
    ../src/utils/internalexception.cpp \
    tests.cpp



HEADERS += \
    ../src/utils/gateway.h \
    ../src/components/strategylab.h \
    ../src/utils/internalexception.h \
    tests.h


RESOURCES += \
    ../src/resources.qrc
