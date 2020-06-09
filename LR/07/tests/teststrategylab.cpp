#include "teststrategylab.h"


/**
 * @brief Констркутор класса TestStrategyLab, в котором
 * инициализируется объект тестируемого класса StrategyLab
 * @param parent
 */
TestStrategyLab::TestStrategyLab(QObject *parent)
    : QObject(parent)
{
    testObj = new StrategyLab(nullptr);
    QDomDocument config;
    QFile file(QDir::currentPath() + "/../../07/tests/getTestSuites/testSuites.xml");
    if (file.open(QIODevice::ReadOnly)) {
        if (config.setContent(&file)) {
            suites = config.documentElement();
        }
        file.close();
    }
}

/**
 * @brief Метод, аккумулирующий данные тест-кейсов метода проверок классов-наследников
 * описания кейсов есть в сценариях (см testsSuites.xlsx)
 */
void TestStrategyLab::testCheckChildren_data()
{
    QTest::addColumn<QList<QString>>("testData");
    QTest::addColumn<QString>("description");
    QTest::addColumn<QString>("expected");

    if (!suites.isNull()) {
        QRegExp re("issue-173-[0-9]{1,2}");
        for (QDomElement key = suites.firstChildElement();
             !key.isNull(); key = key.nextSibling().toElement())
        {
            QString caseId = key.attribute("id");
            if (re.exactMatch(caseId)) {
                QString inputData = key.elementsByTagName("input").at(0).toElement().attribute("text");
                QString description = key.elementsByTagName("description").at(0).toElement().attribute("text");
                QString expected = key.elementsByTagName("expected").at(0).toElement().attribute("text");

                QTest::newRow(caseId.toLatin1().constData()) << QByteArray(inputData.toStdString().c_str()) << description << expected;
            }
        }
    } else {
        qDebug() << "Get test suites from Google Sheets first";
    }
}

void TestStrategyLab::testCheckChildren()
{
    if (!suites.isNull()) {
        QFETCH(QList<QString>, testData);
        QFETCH(QString, description);
        QFETCH(QString, expected);

        try {
          testObj->divideIntoClasses(testData);
          testObj->checkParentChildrenRelations();
          testObj->checkChildren();
          QFAIL("Test worked like input data is valid, but it is invalid (at least it should be)");
        } catch (WrongRequestException error) {
            QString methodResult = error.text();
            QCOMPARE(methodResult, expected);
        }
    } else {
        qDebug() << "Get test suites from Google Sheets first";
    }
}
