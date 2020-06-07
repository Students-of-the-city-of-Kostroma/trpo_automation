#ifndef STARTEGYLAB_H
#define STARTEGYLAB_H

#include "utils/internalexception.h"
#include "utils/logfile.h"

#include <QObject>
#include <QtXml>

/**
 * @brief Класс для проверки лабораторных работ
 *  по паттерну 'Стратегия'
 */
class StrategyLab: public QObject
{
    Q_OBJECT

private:
    QList<QString> className;
    QDomElement rootAnswerStructure;
    QMap<QString, QString> classes;
    QList<QString> children;
    QString nameClassContext;
    QString abstractClassName;
    QString abstractMethodName;
    int heirsAmount;
    logfile log;

public:
    explicit StrategyLab(QObject* parent = nullptr);
    ~StrategyLab();
    bool findChildrenClasses(QString);
    void divideIntoClasses(QList<QString>);
    void checkByConfig(int, QList<QString>);
    void checkParentChildrenRelations();
    void checkContext();
    void checkMainFunction();
    void checkChildren();

private:
    void checkAbstractMethodModifier(QString, QString, QString modifier = "public");
};

#endif // STARTEGYLAB_H
