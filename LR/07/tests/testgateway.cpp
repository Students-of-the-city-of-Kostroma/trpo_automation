#include "testgateway.h"

/**
 * @brief Констркутор класса TestGateway, в котором
 * инициализируется объект тестируемого класса Gateway
 * @param parent
 */
TestGateway::TestGateway(QObject *parent)
    : QObject(parent),
      xlsx(":/config/testSuites.xlsx")
{
    testObj = new Gateway(nullptr);
}

/**
 * @brief Тестовая функция отправляет Gateway полностью корректную строчку формата Json
 */
void TestGateway::testTrueJson()
{
    QByteArray inputRightData("{\"messageType\": 1, \"lab\": 7, \"variant\": 1, \"link\": \"https://github.com/leshastern/strategy4\"}");

    try {
        testObj->validateData(inputRightData);
    } catch (WrongRequestException error) {
        qCritical() << error.text();
        QFAIL("Эти тесты должны быть пройдены!");
    }
}
/**
 * @brief Метод, аккумулирующий некорректные Json для далнейшей проверки
 * описания кейсов есть в сценариях (см testsSuites.xlsx)
 */
void TestGateway::testSuite_data()
{
    int row = 1;
    Cell* cell = xlsx.cellAt(row, 1);
    QRegExp re("issue-393-[0-9]{1,3}");

    QTest::addColumn<QByteArray>("testData");
    QTest::addColumn<QString>("description");
    QTest::addColumn<QString>("expected");

    while (cell) {
        QString caseId = cell->value().toString();
        if (re.exactMatch(caseId)) {
            QByteArray inputData = xlsx.cellAt(row, COLUMN_INDEX_FOR_TEST_DATA)->value().toByteArray();
            QString description = xlsx.cellAt(row, COLUMN_INDEX_FOR_CASE_DESCRIPTION)->value().toString();
            QString expected = xlsx.cellAt(row, COLUMN_INDEX_FOR_EXPECTED_DATA)->value().toString();

            QTest::newRow(caseId.toLatin1().constData()) << inputData << description << expected;
        }
        cell = xlsx.cellAt(++row, 1);
    }
}

/**
 * @brief Тестовая функция извлекает из заранее подготовленной таблицы
 * некорректные Json и отдает их на проверку методу validateData()
 */
void TestGateway::testSuite()
{
    QFETCH(QByteArray, testData);
    QFETCH(QString, description);
    QFETCH(QString, expected);

    try {
      testObj->validateData(testData);
      QFAIL(("Тест" + description + "не пройден. ID: " + QTest::currentDataTag()).toStdString().c_str());
    } catch (WrongRequestException error) {
//        TODO: заменить после задачи https://github.com/Students-of-the-city-of-Kostroma/trpo_automation/issues/51
//        Добавить reject коды
        QString gatewayResult = "{\"messageType\": " + QString::number(3) + ", \"key\": \""
                + error.jsonKey() + "\", \"text\": \"" + error.text() + "\"}";
        QCOMPARE(gatewayResult, expected);
    }
}

/**
 * @brief Почищаем после всех тестов
 */
void TestGateway::cleanupTestCase()
{
    delete testObj;
}

QTEST_MAIN(TestGateway)
