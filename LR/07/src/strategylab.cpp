#include "strategylab.h"

/**
 * @brief Конструктор
 * @param objectFromServer
 * @param parent
 */
StrategyLab::StrategyLab(QObject* parent)
    : QObject(parent)
{
    log.logInfo("Include XML config");
    /* Подключаем answerStructure.xml для проверки лабораторной работы
       Храниться в rootAnswerStructure */
    QDomDocument config;
    QFile file(":/config/answerStructure.xml");
    if (file.open(QIODevice::ReadOnly)) {
        if (config.setContent(&file)) {
            rootAnswerStructure = config.documentElement();
        }
        file.close();
    }
}
/**
 * @brief Метод проверяет строку кода на наследование
 * @param strOfCode - распарсенная строка кода
 * @return возвращает 1 если строка является наследником и 0 если нет
 */
bool StrategyLab::findChildrenClasses(QString strOfCode)
{
    log.logInfo("Check string for inheritance");
    if (strOfCode.indexOf("class") != -1) {
        if (strOfCode.indexOf(':', strOfCode.indexOf("class")) < strOfCode.indexOf('{', strOfCode.indexOf("class"))
                && strOfCode.indexOf(':', strOfCode.indexOf("class")) != -1)
            return 1;
    }
    return 0;
}
/**
 * @brief Делим присланный код на классы Context, abstract, children и main функцию
 * @param code - лист с кодом распарсенного решения
 */
void StrategyLab::divideIntoClasses(QList<QString> code)
{
    log.logInfo("Divide the code sent to classes");
    for (int i = 0; i < code.size(); i++) {
        if (code[i].contains("Context") && code[i].contains("class")) {
            classes.insert("Context", code[i]);
        }
        else if (code[i].contains("virtual") && code[i].contains("class")) {
            classes.insert("parent", code[i]);
        }
        else if (code[i].contains("int main(")) {
            classes.insert("main", code[i]);
        }
        else if (findChildrenClasses(code[i])) {
            children.append(code[i]);
        }
    }
}
/**
 * @brief Здесь параллельно реализуется функицонал проверки кода по конфигу
 *        а также разделение кода на классы (divideIntoClasses)
 * @param variant - вариант лабораторной работы
 * @param code - присланное решение
 * TODO переписать это!!
 * @return
 */
void StrategyLab::checkByConfig(int variant, QList<QString> code)
{
    log.logInfo("Сhek code by XML Config");
    //Делим присланный код на классы для удобства работы с ними
    divideIntoClasses(code);

    /* Извлекаем часть конфига answerStructure.xml, подходящую для варианта лабораторной */
    QDomElement elem;
    QDomNodeList labsConfig = rootAnswerStructure.elementsByTagName("lab");
    for (QDomNode node = labsConfig.at(0); !node.isNull(); node = node.nextSibling()) {
        elem = node.toElement();
        if (elem.attribute("number").toInt() == variant) break;
    }

    for (int i = 0; i < elem.elementsByTagName("class").size(); i++) {
    className.append(elem.elementsByTagName("class").at(i).toElement().attribute("name"));
    }

    QDomElement abstract = elem.elementsByTagName("abstract").at(0).toElement();
       abstractClassName = abstract.attribute("name");
       abstractMethodName = abstract.elementsByTagName("method").at(0).toElement().attribute("name");
       heirsAmount = elem.elementsByTagName("heirs").at(0).toElement().attribute("amount").toInt();

    QDomNode temp;
    QString child;
    QString tempString;

    temp = elem.firstChild();
    tempString = classes.value("parent");

    /* Проверяем имя абстрактного класса */
    if (!tempString.contains(abstractClassName)) {
        throw UnexpectedResultException("Invalid parent class name");
    }
        temp = temp.firstChild();

    /* Проверяем имя метода абстрактного метода */
    if (!tempString.contains(abstractMethodName)) {
        throw UnexpectedResultException("Invalid abstract method name");
    }

    child = classes.value("children");

    /* Проверяем колличество параметров абстрактного метода */
    child = child.simplified();
    if (!child.contains(temp.toElement().attribute("hasParams") + "()") ||
            !child.contains(temp.toElement().attribute("hasParams") + " ()") ||
            !child.contains(temp.toElement().attribute("hasParams") + "( )") ||
            !child.contains(temp.toElement().attribute("hasParams") + " ( )")) {
        throw UnexpectedResultException("An abstract method must have 0 parameters");
    }

    /* Проверяем возвращаемое занчение метода */
    if (!child.contains("return")) {
        throw UnexpectedResultException("An abstract method should return a value");
    }

    /* Проверка имен наследников */
    temp = elem.lastChild();
    int amountChild = 0;

    temp = temp.firstChild();
    child = classes.value("children");

    while (!temp.isNull()) {
        if (!child.contains(temp.toElement().attribute("name"))) {
            throw UnexpectedResultException("Invalid heir name");
        }
        temp = temp.nextSibling();
    }

     /* Проверка количества наследников */
    amountChild = child.count("class");
    if (heirsAmount != amountChild) {
        throw UnexpectedResultException("Incorrect number of heirs");
    }
}

/**
 * @brief Проверки на абстрактный класс и его наследников
 * @return
 */
void StrategyLab::checkParentChildrenRelations()
{
    log.logInfo("Testing for an abstract class");
    /***** Проверки на абстрактный класс *****/

    QString parent = classes.value("parent");

    // Проверка: абстрактный класс обладает абстрактным методом
    if (!parent.contains("virtual")) {
        throw UnexpectedResultException("No abstract methods inside your abstract class '" + \
                                        abstractClassName + "'. You should have at least one.");
    }

    // Проверка: абстрактный класс обладает абстрактным методом с модификатором public
    checkAbstractMethodModifier(abstractClassName, parent);

    // Проверка: абстрактный класс обладает чистым абстрактным методом
    if (!parent.mid(parent.indexOf(abstractMethodName)).simplified().split(" ").join("").contains("=0;")) {
        throw UnexpectedResultException("Your abstract method '" + abstractMethodName + \
                                        "' is not declared as pure abstract.\n " + \
                                        "You should use '= 0' at the end of declaration");
    }

    /***** Проверки на наследников абстрактного класса *****/

}

/**
 * @brief Проверка каждого наследника (на престол), годятся?
 * @return
 */
void StrategyLab::checkChildren()
{
    log.logInfo("Chek children");
    QSet<QString> childMethodBodies;

    foreach (QString child, children) {

        // Проверка: класс ребенок наследуется от родителя
        QString childClassName = child.left(child.indexOf("{")).split(" ", QString::SkipEmptyParts).at(1);
        if (!child.contains(abstractClassName)) {
            throw UnexpectedResultException("Class '" + childClassName + \
                                            "' is not an instance of abstract class '" + abstractClassName + "'");
        }

        // Проверка: класс ребенок наследуется от родителя черз модификтаор public
        QString betweenChildAndAbstarct = child.left(child.indexOf(abstractClassName));
        if (!betweenChildAndAbstarct.contains("public")) {
            QString modifier = betweenChildAndAbstarct.split(":").at(1).split(" ", QString::SkipEmptyParts).at(0);
            throw UnexpectedResultException("Your class '" + childClassName + "' instantiating abstract class '" + \
                                            abstractClassName + "' with '" + modifier + " modificator. It should be 'public'");
        }

        // Проверка: класс ребенок переопределяет абстрактный метод родителя
        if (!child.contains(abstractMethodName) || !child.contains("override")) {
            throw UnexpectedResultException("Your class '" + childClassName + "' does not override abstract method '" + \
                                            abstractMethodName + "' that you \n described inside abstract class '" + \
                                            abstractClassName + "'");
        }

        // Проверка: класс ребенок переопределяет абстрактный метод родителя c модификатором public
        checkAbstractMethodModifier(childClassName, child);

        // Закидываем тела переопределенных методов наследников в массив
        QString methodBody = child.mid(child.lastIndexOf(abstractMethodName));
        QString cutBodyToStart = methodBody.mid(methodBody.indexOf("{"));
        QString cutBodyToEnd = cutBodyToStart.left(cutBodyToStart.lastIndexOf("}"));
        childMethodBodies.insert(cutBodyToEnd.simplified());
    }

    // Проверка: реализации переопределенных методов наследников различаются
    if (childMethodBodies.count() != heirsAmount) {
        throw UnexpectedResultException("Your classes that are instances of abstract class '" + \
                                        abstractClassName + "' override \n abstract method '" + \
                                        abstractMethodName + "' with the same implementation");
    }
}

/**
 * @brief Проверяет, чтобы модификатор метода в классе соответствовал указанному
 * @param className - имя класса
 * @param classBody - класс, где есть проверяемый метод
 * @param modifier - нужный модификатор
 * @return
 */
void StrategyLab::checkAbstractMethodModifier(QString className, QString classBody, QString modifier)
{
    log.logInfo("Check Abstract Method modifier");
    QString fromStartToAbstractMethod = classBody.left(classBody.indexOf(abstractMethodName));
    QString modifierForAbstractMethod = classBody.left(fromStartToAbstractMethod.lastIndexOf(":")).simplified();
    if (!modifierForAbstractMethod.split(" ", QString::SkipEmptyParts).endsWith(modifier)) {
        throw UnexpectedResultException("Method '" + abstractMethodName + "' inside class '" + \
                                        className + "' should be '" + modifier + "'");
    }
}

/**
 * @brief Проверки на класс контекста
 * @return
 */
void StrategyLab::checkContext()
{
    log.logInfo("Check Context");
    /* Убираем лишние элементы в строке */
       QString context = classes.value("context");
       for (int i = 0; i < context.size(); i++) {
           context.remove(" ");
           context.remove("\n");
           context.remove("\t");
           context.remove("\r");
       }

       /* Получаем имя класса */
       nameClassContext = "";
       QString nameClassField = "";
       for (int i = 0; context[i] != '{'; i++) {
           nameClassContext.append(context[i]);
       }
       nameClassContext.remove(QChar('class'), Qt::CaseInsensitive);
       nameClassContext.remove(QChar('{'), Qt::CaseInsensitive);

       /* Проверка приватного поля */
       if (!context.contains("private:" + abstractClassName + "*")) {
           throw UnexpectedResultException(nameClassContext + " must contain a private field such as an abstract class");
       }

       /* Имя приватного поля */
       for (int i = context.indexOf("private:"); i != context.indexOf(";"); i++) {
           nameClassField.append(context[i]);
       }
       for (int i = 0; i < nameClassField.size(); i++) {
                 nameClassField.remove("private:");
                 nameClassField.remove(abstractClassName);
       }
       nameClassField.remove(QChar('*'), Qt::CaseInsensitive);
       nameClassField.remove(QChar(';'), Qt::CaseInsensitive);

       /* Методы не должны возвращать */
       if (context.contains("return")) {
           throw UnexpectedResultException("Class " + nameClassContext + " 1 methods should not return");
       }

       /* Оставляем модификатор public */
       for (int i = 0; i < context.indexOf("public"); i++) {
           context[i] = ' ';
       }
       context.remove(" ");
       for (int i = context.indexOf(nameClassContext); i < context.indexOf("}"); i++) {
           context[i] = ' ';
       }
       context.remove(" ");

       /* Проверка необходимых вызовов в методах */
       if ((!context.contains("this->" + nameClassField + "->")) && (!context.contains("this." + nameClassField + "."))) {
           throw UnexpectedResultException("Class " + nameClassContext + " should call a strategy method");
       }
       if (!context.contains( abstractClassName + "*")) {
           throw UnexpectedResultException("One of the methods of class " + nameClassContext + "1 must accept an argument of the type of an abstract class.");
       }
       if ((!context.contains("this->" + nameClassField + "=")) && (!context.contains("this." + nameClassField + "="))) {
           throw UnexpectedResultException("One of the methods of class " + nameClassContext + " must assign an argument to a property of a class such as an abstract class");
       }
}

/**
 * @brief Проверки на основную функцию (int main)
 * @return
 */
void StrategyLab::checkMainFunction()
{
    log.logInfo("Check Main Function");
    QString mainFunction = classes.value("main"), methodName;
    //Проверка на создание объекта класса context
    if (!mainFunction.contains("new " + nameClassContext)) {
       throw UnexpectedResultException("Object of class context is not created");
    }
    if (mainFunction.lastIndexOf(nameClassContext + "->") != -1) {
        QString arrow = "->";
        int index = mainFunction.lastIndexOf(nameClassContext + "->") + nameClassContext.size() + arrow.size(), i = 0;
        while (mainFunction[index] != '(') {
            methodName[i] = mainFunction[index];
            i++;
            index++;
        }
        if (mainFunction.indexOf(methodName) != mainFunction.lastIndexOf(methodName)) {
            throw UnexpectedResultException("The execute function is called more than once");
        }
    }
    else {
        throw UnexpectedResultException("There is no function call on the context class object");
    }

    for (int i = 0; i < className.size(); i++) {
        if (!mainFunction.contains("new " + className[i])) {
            throw UnexpectedResultException("In the main function, the descendants of the abstract class are not created");
        }
    }
}

/**
 * @brief Деструктор
 */
StrategyLab::~StrategyLab()
{
    // TODO дописать
}
