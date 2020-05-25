#include "testgateway.h"

/**
 * @brief Констркутор класса TestGateway, в котором
 * инициализируется объект тестируемого класса Gateway
 * @param parent
 */
TestGateway::TestGateway(QObject *parent)
    : QObject(parent)
{
    testObj = new Gateway(nullptr);
}

/**
 * @brief Тестовая функция отправляет Gateway полностью корректную строчку формата Json
 */
void TestGateway::testTrueJson()
{
    inputData.append("{\"messageType\": 1, \"lab\": 7, \"variant\": 1, \"link\": \"https://github.com/leshastern/strategy4\"}");

    try {
        testObj->validateData(inputData);
    } catch (WrongRequestException error) {
        qCritical() << error.text();
        QFAIL("Эти тесты должны быть пройдены!");
    }
}
/**
 * @brief Метод, аккумулирующий некорректные Json для далнейшей проверки
 * описания кейсов есть в сценариях https://vk.cc/auCgZM
 */
void TestGateway::badJsons_data()
{   QTest::addColumn<QByteArray>("jsons");
    QTest::newRow("issue-393-1") << QByteArray("");
    QTest::newRow("issue-393-2") << QByteArray("{}");
    QTest::newRow("issue-393-3") << QByteArray("");
    QTest::newRow("issue-393-4") << QByteArray("S");
    QTest::newRow("issue-393-5") << QByteArray("{\"messageType\": 1, \"lab\": 7, \"variant\": 1, \"link\": \"yandex.ru\"}");
    QTest::newRow("issue-393-6") << QByteArray("{\"messageType\": 1, \"lab\": 8, \"variant\": 1, \"link\": \"https://github.com/leshastern/strategy4\"}");
    QTest::newRow("issue-393-7") << QByteArray("{\"messageType\": \"1\", \"lab\": 7, \"variant\": 1, \"link\": \"https://github.com/leshastern/strategy4\"}");
    QTest::newRow("issue-393-8") << QByteArray("{\"messageType\": 1, \"lab\": \"7\", \"variant\": 1, \"link\": \"https://github.com/leshastern/strategy4\"}");
    QTest::newRow("issue-393-9") << QByteArray("{\"messageType\": 1, \"lab\": 7, \"variant\": \"1\", \"link\": \"https://github.com/leshastern/strategy4\"}");
    QTest::newRow("issue-393-10") << QByteArray("{\"messageType\": \"1\", \"lab\": 7, \"variant\": 1, \"link\": \"7\"}");
    QTest::newRow("issue-393-11") << QByteArray("{\"messageType\": 1, \"lab\": 7, \"variant\": 1, \"code\": \"https://github.com/leshastern/strategy4\"}");
    QTest::newRow("issue-393-12") << QByteArray("{\"messageType\": 3, \"lab\": 7, \"variant\": 1, \"link\": \"https://github.com/leshastern/strategy4\"}");
    QTest::newRow("issue-393-13") << QByteArray("{\"messageType\": 1, \"lab\": 7, \"variant\": 2, \"link\": \"https://github.com/leshastern/strategy4\"}");
    QTest::newRow("issue-393-14") << QByteArray("{\"lab\": 7, \"variant\": 1, \"link\": \"https://github.com/leshastern/strategy4\"}");
    QTest::newRow("issue-393-15") << QByteArray("{\"messageType\": 1, \"variant\": 1, \"link\": \"https://github.com/leshastern/strategy4\"}");
    QTest::newRow("issue-393-16") << QByteArray("{\"messageType\": 1, \"lab\": 7, \"link\": \"https://github.com/leshastern/strategy4\"}");
    QTest::newRow("issue-393-17") << QByteArray("{\"messageType\": 1, \"lab\": 7, \"variant\": 1}");
    QTest::newRow("issue-393-18") << QByteArray("{\"messageType\": 1, \"lab\": 7, \"variant\": 1, \"link\": \"https://github.com/leshastern/strategy4\", \"code\": []}");
    QTest::newRow("issue-393-19") << QByteArray("{\"messageType\": 1, \"lab\": 7, \"variant\": 1, \"link\": \"https://github.com/leshastern/strategy4\", \"TRPOTHEBEST\": true}");
    QTest::newRow("issue-393-20") << QByteArray("{\"messageType\": 1}");
    QTest::newRow("issue-393-21") << QByteArray("{\"messageType\": 1, \"lab\": 7}");
    QTest::newRow("issue-393-22") << QByteArray("{\"messageType\": 1, \"lab\": 7, \"variant\": 1}");
    QTest::newRow("issue-393-11") << QByteArray("{\"messageType\": 1, \"lab\": 7, \"variant\": 1, \"code\": [yandex.ru]}");
}

/**
 * @brief Тестовая функция извлекает из заранее подготовленной таблицы
 * некорректные Json и отдает их на проверку методу validateData()
 */
void TestGateway::badJsons()
{
    QFETCH(QByteArray, jsons);
    try {
      testObj->validateData(jsons);
      QFAIL("Недопустимые данные");
    } catch (WrongRequestException error) {
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
