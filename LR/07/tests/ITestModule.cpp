#include "ITestModule.h"
/**
 * @brief Констркутор класса TestGateway, в котором
 * инициализируется объект тестируемого класса Gateway
 * @param parent
 */
ITestModule::ITestModule(QRegExp re, const std::function<QString(QString)> &callback)
    : regexCaseId(re),
      callBack(callback)
{
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
 * @brief Метод, аккумулирующий данные для далнейшей проверки
 * Описания кейсов есть в сценариях (см testsSuites.xlsx)
 */
void ITestModule::testSuite_data()
{
    QTest::addColumn<QString>("testData");
    QTest::addColumn<QString>("description");
    QTest::addColumn<QString>("expected");

    if (!suites.isNull()) {
        for (QDomElement key = suites.firstChildElement();
             !key.isNull(); key = key.nextSibling().toElement())
        {
            QString caseId = key.attribute("id");
            if (regexCaseId.exactMatch(caseId)) {
                QString inputData = key.elementsByTagName("input").at(0).toElement().attribute("text");
                QString description = key.elementsByTagName("description").at(0).toElement().attribute("text");
                QString expected = key.elementsByTagName("expected").at(0).toElement().attribute("text");

                QTest::newRow(caseId.toLatin1().constData()) << inputData << description << expected;
            }
        }
    } else {
        qDebug() << "Get test suites from Google Sheets first";
    }
}

/**
 * @brief Тестовая функция извлекает из заранее подготовленной таблицы
 * и вызывает переданные ей в качестве callback-ов функции для тестирования
 */
void ITestModule::testSuite()
{
    if (!suites.isNull()) {
        QFETCH(QString, testData);
        QFETCH(QString, description);
        QFETCH(QString, expected);

        try {
            QCOMPARE(callBack(testData), expected);
        } catch (WrongRequestException error) {
            QString result = "{\"messageType\": " + QString::number(3)
                    + ", \"key\": \"" + error.jsonKey()
                    + "\", \"rejectCode\": " + QString::number(error.getRejectCode())
                    + ", \"text\": \"" + error.text() + "\"}";
            QCOMPARE(result, expected);
        } catch (UnexpectedResultException error) {
            QCOMPARE(error.text(), expected);
        } catch (SystemException error) {
            QCOMPARE(error.text(), expected);
        }

    } else {
        qDebug() << "Get test suites from Google Sheets first";
    }
}
