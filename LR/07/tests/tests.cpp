#include "tests.h"

/**
 * @brief Метод, аккумулирующий некорректные Json для далнейшей проверки
 * описания кейсов есть в сценариях (см testsSuites.xlsx)
 */
void testSuite_data(QDomElement suites, QRegExp re)
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
void testSuite(QDomElement suites)
{
    if (!suites.isNull()) {
        QFETCH(QByteArray, testData);
        QFETCH(QString, description);
        QFETCH(QString, expected);

        try {
        //  testObj->validateData(testData);
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


/**
 * @brief Констркутор класса TestGateway, в котором
 * инициализируется объект тестируемого класса Gateway
 * @param parent
 */
TestGateway::TestGateway(QObject *parent)
    : QObject(parent)
{
    testObj = new Gateway(nullptr);
    QDomDocument config;
    QFile file(QDir::currentPath() + "/../../07/tests/getTestSuites/testSuites.xml");
    if (file.open(QIODevice::ReadOnly)) {
        if (config.setContent(&file)) {
            suites = config.documentElement();
        }
        file.close();
    }
    QRegExp re("issue-393-[0-9]{1,3}");
    testSuite_data(suites, re);
    testSuite(suites);
    delete testObj;
}

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
    QRegExp re("issue-173-[0-9]{1,2}");
    testSuite_data(suites, re);
    testSuite(suites);
    delete testObj;
}


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
