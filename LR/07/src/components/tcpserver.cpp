#include "tcpserver.h"

/**
 * @brief Конструктор класса, в котором создается объект класса QTcpServer
 * Сервер включается и ждет новых соединений.
 */
TcpServer::TcpServer(int labNumber, QObject *parent)
        : QObject(parent)
{
    logfile::logDebug("TcpServer Constructor");

    mTcpServer = new QTcpServer(this);
    gateWay = new Gateway();
    github = new Functional();

    connect(gateWay, SIGNAL(sendToClient(QJsonObject)), this, SLOT(slotSendToClient(QJsonObject)));
    connect(mTcpServer, &QTcpServer::newConnection, this, &TcpServer::slotNewConnection);

    if (!mTcpServer->listen(QHostAddress::LocalHost, static_cast<quint16>(getPortForLab(labNumber)))) {
        logfile::logCritical("Server is not started");
    } else {
        logfile::logInfo("Server is started");
    }
}

/**
 * @brief Метод получения порта по номеру лабы
 * @param labNumber - номер лабы
 * @return
 */
int TcpServer::getPortForLab(int labNumber)
{
    logfile::logDebug("Get port for lab");

    QDomDocument config;
    QDomElement root;

    QFile file(":/config/labs.xml");
    if (file.open(QIODevice::ReadOnly)) {
        if (config.setContent(&file)) {
            root = config.documentElement();
        }
        file.close();
    } else {
        logfile::logCritical(file.errorString());
    }

    if (!root.isNull()) {
        QDomNodeList portsConfig = root.elementsByTagName("lab");
        for (QDomNode node = portsConfig.at(0); !node.isNull(); node = node.nextSibling()) {
            QDomElement elem = node.toElement();
            if (elem.attribute("number").toInt() == labNumber) {
                return elem.attribute("port").toInt();
            }
        }
    }

    logfile::logFatal("Couldn't read config for a lab's port");
    qApp->quit();
}

/**
 * @brief Метод отвечающий за подключение клиента к серверу
 * @return void
 */
void TcpServer::slotNewConnection()
{
    logfile::logDebug("New connection");

    mTcpSocket = mTcpServer->nextPendingConnection();

    connect(mTcpSocket, SIGNAL(readyRead()), this, SLOT(slotReadingDataJson()));
    connect(mTcpSocket, &QTcpSocket::disconnected, this, &TcpServer::slotClientDisconnected);
}

/**
 * @brief Метод выключает сервер.
 * @return void
 */
void TcpServer::slotClientDisconnected()
{
    logfile::logDebug("Client disconnected");

    mTcpSocket->close();
}

/**
 * @brief Метод отправляет клиенту строку в формате json
 * @param QJsonObjecr answerJson - ответ для клиента
 * @return void
 */
void TcpServer::slotSendToClient(QJsonObject answerJson)
{
    logfile::logDebug("Send data to client");

    QJsonDocument jsonDoc(answerJson);
    QString jsonString = QString::fromLatin1(jsonDoc.toJson());

    mTcpSocket->readAll();
    mTcpSocket->write(jsonString.toLatin1());
}

/**
 * @brief Метод получает данные от клиента в формате json и отдает их на обработку
 * @return void
 */
void TcpServer::slotReadingDataJson()
{
    logfile::logDebug("Reading data json");

    QByteArray data;
    QString labLink;
    QList<QString> pureCode;
    int labNumber = 1;

    data = mTcpSocket->readAll();

    try {
        QJsonDocument jsonDoc = gateWay->validateData(data);
        if (!jsonDoc.isNull()) {
            parsingJson(jsonDoc, &labLink, &labNumber, &pureCode);
            processData(labLink, &pureCode, labNumber);
        }
    } catch (WrongRequestException error) {
        gateWay->wrongRequestFormat(error.jsonKey(), error.getRejectCode(), error.text());
    } catch (SystemException error) {
        gateWay->processSystemError(error.text());
    }
}

/**
 * @brief Метод парсинга пришедших с почтового сервиса Json-данных
 * @param docJson - объект json
 * @param labLink - ссылка на репозиторий решения на Github
 * @param labNumber - номер лабы
 * @param pureData - массив строчек (каждая строчка - класс решения с телами методов)
 */
void TcpServer::parsingJson(QJsonDocument docJson, QString *labLink, int *labNumber, QList<QString> *pureData)
{
    logfile::logDebug("parsing json");

    QJsonValue link;
    QJsonObject jsonObj;

    jsonObj = docJson.object();

    link = jsonObj.take("link");
    if (!link.isUndefined()) {
        (*labLink) = link.toString();
    } else {
        link = jsonObj.take("code");
        foreach (QJsonValue item, link.toArray()) {
            (*pureData).append(item.toString());
        }
    }

    link = jsonObj.take("variant");
    (*labNumber) = link.toInt();
}

/**
 * @brief (коммент года!)Метод обрабатывает код решения пришедший от клиента, проверяет на правильность
 *        и оставляет комментарии, если они необходимы. После этого передает данные для подготовки их передаче клиенту
 * @param link - ссылка на Github репозиторий решения
 * @param code - распарсенный код в массив строчек
 * @param variant - вариант лабы
 */
void TcpServer::processData(QString link, QList<QString> *code, int variant)
{
    logfile::logDebug("Proccess data");

    try {
        if (code->isEmpty()) {
            QUrl urlForRequest = github->linkChange(link);
            QString fileName;
            github->getRequest(urlForRequest, [this, &fileName](QJsonDocument reply) {
                github->getFileInside(reply.array(), fileName);
            });

            if (fileName.isEmpty()) {
                throw UnexpectedResultException("You don't have file with .cpp extension inside your repo");
            }

            github->getRequest(QUrl(urlForRequest.toString() + "/" + fileName),
                               [this, code](QJsonDocument reply) {
                github->parseIntoClasses(github->getCode(reply), code);
            });
        }

        lab = new StrategyLab();
        lab->checkByConfig(variant, *code);
        lab->checkParentChildrenRelations();
        lab->checkChildren();
        lab->checkContext();
        lab->checkMainFunction();
        delete lab;

        gateWay->prepareDataToSend(true);
    } catch (UnexpectedResultException error) {
        gateWay->prepareDataToSend(false, error.text());
    }
}

/**
 * @brief Деструктор
 */
TcpServer::~TcpServer()
{
    logfile::logDebug("TcpServer Destructor");

    delete mTcpServer;
    delete gateWay;
    delete lab;
    delete github;
}
