import org.json.simple.JSONObject;
import org.json.simple.JSONValue;
import org.json.simple.parser.ParseException;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.LinkedList;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.logging.*;

public class Server {
    static Logger LOGGER;
    public static Selenium selenium;
    public static String otvet;
    public static LinkedList<ServerSomthing> serverList = new LinkedList<>();
    public static int port=0;
    public static Socket clientSocket; //Сокет клиента
    public static ServerSocket server; //Сокет сервера
    public static BufferedReader in; //Чтобы принимать и отправлять сообщения буферы
    public static BufferedWriter out;
    public static String TypeMessage;
    public static String NomberVar;
    public static String Repos;
    public static String NomberLab;
    public static String Oshibka;
    public static boolean conec=false;
    private static final String FILENAME = "labs.xml";

    static {
        File theDir = new File("log_LR3");
        if (!theDir.exists()) {
            boolean result = false;

            try{
                theDir.mkdir();
                result = true;
            }
            catch(SecurityException se){
                //handle it
            }
            if(result) {

            }
        }
        try (Writer writer = new BufferedWriter(new OutputStreamWriter(
                new FileOutputStream(System.getProperty("user.dir")  + File.separator+"log_LR3"+File.separator+"loger.config"), "utf-8"))) {
            writer.write("handlers = java.util.logging.FileHandler, java.util.logging.ConsoleHandler\n" +
                    "\n" +
                    "java.util.logging.FileHandler.level     = INFO\n" +
                    "java.util.logging.FileHandler.formatter = java.util.logging.SimpleFormatter\n" +
                    "java.util.logging.FileHandler.append    = true\n" +
                    "java.util.logging.FileHandler.pattern   = log_LR3/logLR3.%u.%g.txt\n" +
                    "\n" +
                    "java.util.logging.ConsoleHandler.level     = INFO\n" +
                    "java.util.logging.ConsoleHandler.formatter = java.util.logging.SimpleFormatter");
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

        try(FileInputStream ins = new FileInputStream(System.getProperty("user.dir")  + File.separator+"log_LR3"+ File.separator+"loger.config")){
            LogManager.getLogManager().readConfiguration(ins);
            LOGGER = Logger.getLogger(Server.class.getName());
        }catch (Exception ignore){
            ignore.printStackTrace();}

    }

    private static void SetPort(){
        try {
            LOGGER.log(Level.INFO,"Попытка считать конфиг портов");
            final File xmlFile = new File(System.getProperty("user.dir") +File.separator +".." + File.separator+ File.separator +".." + File.separator + FILENAME);
            DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
            DocumentBuilder db = dbf.newDocumentBuilder();
            Document doc = db.parse(xmlFile);
            doc.getDocumentElement().normalize();

            NodeList NodeList = doc.getElementsByTagName("lab");

            for (int i = 0; i < NodeList.getLength(); i++) {
                // Вывoдиm инфopmaцию пo kaждomy из нaйдeнных элemeнтoв
                Node node = NodeList.item(i);
                if (Node.ELEMENT_NODE == node.getNodeType()) {
                    Element element = (Element) node;
                    if (element.getAttribute("number").equals("3")){
                        port=Integer.parseInt(element.getAttribute("port"));
                        LOGGER.log(Level.INFO,"Попытка считать конфиг портов успешна");
                        break;

                    }
                }
            }
        }
        catch (ParserConfigurationException | SAXException | IOException ex){
            LOGGER.log(Level.SEVERE,"Попытка считать конфиг портов провалилась",ex);
        }
    }

    //ФУНКЦИЯ создания ДЖСОН ОТВЕТА
    public static String Otvet(String grade,String comment) {//Получаем рез.работы силениума
        JSONObject jsonObject = new JSONObject();//Создаем новый обьект
        jsonObject.put("messageType", "2");//Все ли успешно
        jsonObject.put("grade", grade);
        jsonObject.put("comment", comment);//Если нет, то где ошибки

        return jsonObject.toString();//обьект ДЖСОН в строку и отправляем
    }
    public static String ErrorServer(IOException a) {//метод с ошибкой на сервере
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("messageType", "4");
        jsonObject.put("errorMessage", a);

        return jsonObject.toString();
    }
    public static String ErrorArg(String nameKey,String rejectCodeName,String comment) {//метод с ошибкой на ДЖСОН
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("messageType", "3");
        jsonObject.put("key",nameKey);
        jsonObject.put("text",comment);
        jsonObject.put("rejectCode",rejectCodeName);

        return jsonObject.toString();
    }
    public static void OsnovaDecoda(String word,boolean flag) throws ParseException, IOException
    {
        try {

            JSONObject Cilka = (JSONObject)JSONValue.parseWithException(word);
            String proverka=Cilka.toString();
            conec=false;

            if(conec==false) {
                TypeMessage=Cilka.get("messageType").toString();

                String TestTipeMes1="";
                if(TypeMessage.equals(TestTipeMes1)&&conec==false)
                {
                    TypeMessage="3";
                    NomberLab="messageType";
                    NomberVar="2";
                    Repos="Отстуствует ключ";
                    ErrorArg(NomberLab,NomberVar,Repos);
                    conec=true;
                }
                if(conec==false) {
                    try {
                        byte x1=Byte.parseByte(TypeMessage);
                        if(x1!=1&&conec==false) {
                            TypeMessage="3";
                            NomberLab="messageType";
                            NomberVar="3";
                            Repos="Неверное значение";
                            conec=true;
                            ErrorArg(NomberLab,NomberVar,Repos);
                        }
                    }
                    catch(NumberFormatException e) {
                        TypeMessage="3";
                        NomberLab="messageType";
                        NomberVar="4";
                        Repos="Не тот тип данных";
                        ErrorArg(NomberLab,NomberVar,Repos);
                        conec=true;
                    }
                }}


            if(conec==false) {
                NomberLab=Cilka.get("lab").toString();

                String TestNomberLab1="";
                if(NomberLab.equals(TestNomberLab1)&&conec==false)
                {
                    TypeMessage="3";
                    NomberLab="lab";
                    NomberVar="2";
                    Repos="Отстуствует ключ";
                    ErrorArg(NomberLab,NomberVar,Repos);
                    conec=true;
                }
                if(conec==false) {
                    try {
                        byte x2=Byte.parseByte(NomberLab);
                        if(x2!=3&&conec==false) {
                            TypeMessage="3";
                            NomberLab="lab";
                            NomberVar="3";
                            Repos="Неверное значение";
                            ErrorArg(NomberLab,NomberVar,Repos);
                            conec=true;
                        }
                    }
                    catch(NumberFormatException e) {
                        TypeMessage="3";
                        NomberLab="lab";
                        NomberVar="4";
                        Repos="Не тот тип данных";
                        ErrorArg(NomberLab,NomberVar,Repos);
                        conec=true;
                    }
                } }



            if(conec==false) {
                NomberVar=Cilka.get("variant").toString();

                String TestNomberVar1="";
                if(NomberVar.equals(TestNomberVar1)&&conec==false)
                {
                    TypeMessage="3";
                    NomberLab="variant";
                    NomberVar="2";
                    Repos="Отстуствует ключ";
                    ErrorArg(NomberLab,NomberVar,Repos);
                    conec=true;
                }
                if(conec==false) {
                    try {
                        byte x3=Byte.parseByte(NomberVar);
                        if((x3<=0||x3>15)&&conec==false) {
                            TypeMessage="3";
                            NomberLab="variant";
                            NomberVar="3";
                            Repos="Неверное значение";
                            ErrorArg(NomberLab,NomberVar,Repos);
                            conec=true;
                        }
                    }
                    catch(NumberFormatException e) {
                        TypeMessage="3";
                        NomberLab="variant";
                        NomberVar="4";
                        Repos="Не тот тип данных";
                        ErrorArg(NomberLab,NomberVar,Repos);
                        conec=true;
                    }
                }}


            if(conec==false) {
                Repos=Cilka.get("link").toString();

                try {
                    String s2="https://github.com/";
                    String s3="";
                    if(Repos.equals(s3)&&conec==false)
                    {
                        TypeMessage="3";
                        NomberLab="link";
                        NomberVar="2";
                        Repos="Отстуствует ключ";
                        ErrorArg(NomberLab,NomberVar,Repos);
                        conec=true;
                    }
                    if(conec==false) {
                        String s1=Repos.substring(0,19);
                        if(!s1.equals(s2)&&conec==false) {
                            TypeMessage="3";
                            NomberLab="link";
                            NomberVar="3";
                            Repos="Неверное значение";
                            ErrorArg(NomberLab,NomberVar,Repos);
                            conec=true;}
                    }

                }
                catch(StringIndexOutOfBoundsException e) {
                    TypeMessage="3";
                    NomberLab="link";
                    NomberVar="3";
                    Repos="Неверное значение";
                    ErrorArg(NomberLab,NomberVar,Repos);
                    conec=true;
                }}

        }
        catch(ParseException e){
            TypeMessage="3";
            NomberLab="messageType, variant, link, lab";
            NomberVar="1";
            Repos="Неверная JSON строка";
            ErrorArg(NomberLab,NomberVar,Repos);
        }
        if(conec==false&&flag) {
            Server.LOGGER.log(Level.INFO,"Запуск модуля Selenium");
            selenium=new Selenium(Repos,NomberVar);
            selenium.test();
            Server.LOGGER.log(Level.INFO,"Selenium отработал. Формирование ответа");
            otvet=Otvet(selenium.Get_Ozenka(),selenium.Get_Result());
            selenium.driver.quit();
        }
    }

    public static void Priem() throws IOException
    {
        SetPort();
        server = new ServerSocket(port);
        try {
            LOGGER.log(Level.INFO,"Сервер запущен");
            while (true) {
                // Блокируется до возникновения нового соединения:
                Socket clientSocket = server.accept();
                try {
                    LOGGER.log(Level.INFO,"Создано соединение");
                    serverList.add(new ServerSomthing(clientSocket));
                    // добавить новое соединенние в список
                } catch (IOException e) {
                    LOGGER.log(Level.WARNING,"Не удалось создать соединение");
                    // Если завершится неудачей, закрывается сокет,
                    // в противном случае, нить закроет его при завершении работы:
                    clientSocket.close();
                }
            }
        } finally {
            server.close();
            LOGGER.log(Level.INFO,"Сервер закрыт");
        }
    }


    public static void main(String[] args) throws ParseException, IOException {
        Priem();
    }
}