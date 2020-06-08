import org.json.simple.parser.ParseException;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;


import java.io.IOException;
import java.util.Arrays;
import java.util.Collection;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

@RunWith(value = Parameterized.class)
public class ServerAndSeleniumTest {
    private String Gison;
    private Server server;
    private String otvet;


    // Inject via constructor
    // for {8, 2, 10}, numberA = 8, numberB = 2, expected = 10
    public ServerAndSeleniumTest(String Gison,String otvet) throws ParseException, IOException {
        this.Gison=Gison;
        this.otvet=otvet;
        server=new Server();
        server.OsnovaDecoda(Gison,true);
    }

    // name attribute is optional, provide an unique name for test
    // multiple parameters, uses Collection<Object[]>
    @Parameters(name = "{index}: testid {1} {2}")
    public static Collection<Object[]> data() {
        return Arrays.asList(new Object[][]{
            {"{\"messageType\":\"1\",\"variant\":\"1\",\"link\":\"https:\\/\\/github.com\\/vvtatyana\\/Losiash.git\",\"lab\":\"3\"}","{\"messageType\":\"2\",\"grade\":\"0\",\"comment\":\"Неверное имя репозитория\\n\"}"},
             {"{\"messageType\":\"1\",\"variant\":\"2\",\"link\":\"https:\\/\\/github.com\\/vvtatyana\\/Krosh\",\"lab\":\"3\"}","{\"messageType\":\"2\",\"grade\":\"0\",\"comment\":\"Неверное имя ветки\\n\"}"},
             {"{\"messageType\":\"1\",\"variant\":\"3\",\"link\":\"https:\\/\\/github.com\\/vvtatyana\\/Yozhik\",\"lab\":\"3\"}","{\"messageType\":\"2\",\"grade\":\"0\",\"comment\":\"Файл Readme не найден\\nВ ветке master неверное кол-во файлов\\n\"}"},
             {"{\"messageType\":\"1\",\"variant\":\"4\",\"link\":\"https:\\/\\/github.com\\/vvtatyana\\/Barash\",\"lab\":\"3\"}","{\"messageType\":\"2\",\"grade\":\"0\",\"comment\":\"В ветке master неверное кол-во файлов\\n\"}"},
             {"{\"messageType\":\"1\",\"variant\":\"5\",\"link\":\"https:\\/\\/github.com\\/vvtatyana\\/Nusha\",\"lab\":\"3\"}","{\"messageType\":\"2\",\"grade\":\"0\",\"comment\":\"Имя labels не совпадает\\nИмя открытого pull_request неверно,либо не назначен label\\nИмя закрытого issues неверно\\n\"}"},
             {"{\"messageType\":\"1\",\"variant\":\"6\",\"link\":\"https:\\/\\/github.com\\/vvtatyana\\/Pin\",\"lab\":\"3\"}","{\"messageType\":\"2\",\"grade\":\"0\",\"comment\":\"Имя milestone некорректно\\n\"}"},
             {"{\"messageType\":\"1\",\"variant\":\"7\",\"link\":\"https:\\/\\/github.com\\/vvtatyana\\/Sovunya\",\"lab\":\"3\"}","{\"messageType\":\"2\",\"grade\":\"0\",\"comment\":\"Неверное имя project\\n\"}"},{"{\"messageType\":\"1\",\"variant\":\"8\",\"link\":\"https:\\/\\/github.com\\/vvtatyana\\/Pandi\",\"lab\":\"3\"}","{\"messageType\":\"2\",\"grade\":\"0\",\"comment\":\"Доска To do не содержит задачи: Внешность\\nДоска In progress не содержит задачи: Предпочтения и интересы\\nДоска Done не содержит задачи: Характер\\nНеверное имя открытого issue\\/issues\\n\"}"},
            {"{\"messageType\":\"1\",\"variant\":\"9\",\"link\":\"https:\\/\\/github.com\\/vvtatyana\\/Kar-Karych\",\"lab\":\"3\"}","{\"messageType\":\"2\",\"grade\":\"0\",\"comment\":\"В milestone должно быть 5 задач(3 открытых, 2 закрытых)\\nКол-во pull_request неверно\\nНе совпадает кол-во issues\\nВ ветке master неверное кол-во файлов\\n\"}"},
            {"{\"messageType\":\"1\",\"variant\":\"10\",\"link\":\"https:\\/\\/github.com\\/vvtatyana\\/Kopatych\",\"lab\":\"3\"}","{\"messageType\":\"2\",\"grade\":\"0\",\"comment\":\"Имя открытого pull_request неверно,либо не назначен label\\nНеверное имя открытого issue\\issues\\nВ ветке master неверные файлы\\n\"}"},
            {"{\"messageType\":\"1\",\"variant\":\"11\",\"link\":\"https:\\/\\/github.com\\/vvtatyana\\/Bibi\",\"lab\":\"3\"}","{\"messageType\":\"2\",\"grade\":\"0\",\"comment\":\"Доска To do не содержит задачи: Отношения с другими смешариками\\nДоска Done не содержит задачи: Биография\\nИмя закрытого pull_request неверно,либо не назначен label\\nНеверное имя открытого issue\\/issues\\nВ ветке master неверные файлы\\n\"}"},
            {"{\"messageType\":\"1\",\"variant\":\"12\",\"link\":\"https:\\/\\/github.com\\/vvtatyana\\/Mysharik\",\"lab\":\"3\"}","{\"messageType\":\"2\",\"grade\":\"0\",\"comment\":\"В milestone должно быть 5 задач(3 открытых, 2 закрытых)\\nКол-во pull_request неверно\\nНе совпадает кол-во issues\\nНеверное кол-во branches\\n\"}"},
            {"{\"messageType\":\"1\",\"variant\":\"13\",\"link\":\"https:\\/\\/github.com\\/vvtatyana\\/Mulya\",\"lab\":\"3\"}","{\"messageType\":\"2\",\"grade\":\"0\",\"comment\":\"Label верен, но назначен не на все задачи или\\/и pull_requests\\nВ milestone должно быть 5 задач(3 открытых, 2 закрытых)\\nОшибка в pull_requests. Должно быть 1 открытый, 1 закрытый\\nНе совпадает кол-во issues\\/nВ ветке master неверное кол-во файлов\\n\"}"},
            {"{\"messageType\":\"1\",\"variant\":\"14\",\"link\":\"https:\\/\\/github.com\\/vvtatyana\\/Zheleznaya_Nyanya\",\"lab\":\"3\"}","{\"messageType\":\"2\",\"grade\":\"0\",\"comment\":\"Label не назначен на задачи или\\/и pull_requests\\nВ milestone должно быть 5 задач(3 открытых, 2 закрытых)\\nДоска To do не содержит задач.\\nДоска In progress не содержит задач.\\nДоска Done не содержит задач.\\nКол-во pull_request неверно\\nНе совпадает кол-во issues\\nВ ветке master неверное кол-во файлов\\n\"}"},
                {"{\"messageType\":\"1\",\"variant\":\"15\",\"link\":\"https:\\/\\/github.com\\/vvtatyana\\/Tigritsiya\",\"lab\":\"3\"}", "{\"messageType\":\"2\",\"grade\":\"0\",\"comment\":\"В milestone должно быть 5 задач(3 открытых, 2 закрытых)\\nКол-во pull_request неверно\\nНе совпадает кол-во issues\\nНеверное кол-во branches\\n\"}"
                }  });
    }

    @Test
    public void test() {
        Assert.assertEquals(server.otvet,otvet);
    }



}