#include "tests.h"
/**
 * @brief Констркутор класса TestGateway, в котором
 * инициализируется объект тестируемого класса Gateway
 * @param parent
 */
Tests::Tests(QObject *parent)
    : QObject(parent)
{
    testObj = new Gateway(nullptr);
    testObjj = new StrategyLab(nullptr);
    QDomDocument config;
    QFile file(QDir::currentPath() + "/../../07/tests/getTestSuites/testSuites.xml");
    if (file.open(QIODevice::ReadOnly)) {
        if (config.setContent(&file)) {
            suites = config.documentElement();
        }
        file.close();
    }
    QRegExp gatewayCases ("issue-393-[0-9]{1,3}");
    testSuite_data(suites, gatewayCases);
    testSuite(suites);
    delete testObj;
    QRegExp checkChildrenCases ("issue-173-[0-9]{1,2}");
    testSuite_data(suites, checkChildrenCases);
    testSuite(suites);
    delete testObjj;
}

/**
 * @brief Метод, аккумулирующий некорректные Json для далнейшей проверки
 * описания кейсов есть в сценариях (см testsSuites.xlsx)
 */
void Tests::testSuite_data(QDomElement suites, QRegExp re)
{
    QTest::addColumn<QByteArray>("testData");
    QTest::addColumn<QString>("description");
    QTest::addColumn<QString>("expected");

    if (!suites.isNull()) {
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

/**
 * @brief Тестовая функция извлекает из заранее подготовленной таблицы
 * некорректные Json и отдает их на проверку методу validateData()
 */
void Tests::testSuite(QDomElement suites)
{
    if (!suites.isNull()) {
        QFETCH(QByteArray, testData);
        QFETCH(QString, description);
        QFETCH(QString, expected);

        try {
         testObj->validateData(testData);
          QFAIL("Test worked like input data is valid, but it is invalid (at least it should be)");
        } catch (WrongRequestException error) {
    //        TODO: заменить после задачи https://github.com/Students-of-the-city-of-Kostroma/trpo_automation/issues/51
    //        Добавить reject коды
            QString gatewayResult = "{\"messageType\": " + QString::number(3) + ", \"key\": \""
                    + error.jsonKey() + "\", \"text\": \"" + error.text() + "\"}";
            QCOMPARE(gatewayResult, expected);
        }
    } else {
        qDebug() << "Get test suites from Google Sheets first";
    }
}

QTEST_MAIN(Tests)
