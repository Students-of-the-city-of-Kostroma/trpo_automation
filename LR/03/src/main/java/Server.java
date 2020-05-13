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
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.LinkedList;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Server {
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
    private static final String FILENAME = "Repository.xml";

    private static void SetPort(){
        try {
            final File xmlFile = new File(System.getProperty("user.dir") + File.separator + FILENAME);
            DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
            DocumentBuilder db = dbf.newDocumentBuilder();
            Document doc = db.parse(xmlFile);

            doc.getDocumentElement().normalize();

            NodeList NodeList = doc.getElementsByTagName("port");

            for (int i = 0; i < NodeList.getLength(); i++) {
                // Вывoдиm инфopmaцию пo kaждomy из нaйдeнных элemeнтoв
                Node node = NodeList.item(i);
                if (Node.ELEMENT_NODE == node.getNodeType()) {
                    Element element = (Element) node;
                    port= Integer.parseInt(element.getElementsByTagName("portnumber").item(0).getTextContent());
                }
            }
        }
        catch (ParserConfigurationException | SAXException | IOException ex){
            Logger.getLogger(Server.class.getName()).log(Level.SEVERE,null,ex);
        }
    }

    //ФУНКЦИЯ создания ДЖСОН ОТВЕТА
    public static String Otvet(String grade,String comment) {//Получаем рез.работы силениума
        JSONObject jsonObject = new JSONObject();//Создаем новый обьект
        jsonObject.put("messageType", "2");//Все ли успешно
        jsonObject.put("grade", grade);
        jsonObject.put("comment", comment);//Если нет, то где ошибки
        System.out.println(jsonObject.toJSONString());
        return jsonObject.toString();//обьект ДЖСОН в строку и отправляем
    }
    public static String ErrorServer(IOException a) {//метод с ошибкой на сервере
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("messageType", "4");
        jsonObject.put("errorMessage", a);
        System.out.println(jsonObject.toJSONString());
        return jsonObject.toString();
    }
    public static String ErrorArg(String nameKey,String rejectCodeName,String comment) {//метод с ошибкой на ДЖСОН
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("messageType", "3");
        jsonObject.put("key",nameKey);
        jsonObject.put("text",comment);
        jsonObject.put("rejectCode",rejectCodeName);
        System.out.println(jsonObject.toJSONString()+"OSHIBKA:");
        return jsonObject.toString();
    }
    public static void OsnovaDecoda(String word) throws ParseException, IOException
    {
        try {
            System.out.println(word);
            JSONObject Cilka = (JSONObject)JSONValue.parseWithException(word);
            String proverka=Cilka.toString();
            conec=false;

            if(conec==false) {
                TypeMessage=Cilka.get("messageType").toString();
//                     System.out.println(TypeMessage);
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
            System.out.println(TypeMessage);

            if(conec==false) {
                NomberLab=Cilka.get("lab").toString();
//                     System.out.println(NomberLab);
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
            System.out.println(NomberLab);


            if(conec==false) {
                NomberVar=Cilka.get("variant").toString();
//                     System.out.println(NomberVar);
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
            System.out.println(NomberVar);

            if(conec==false) {
                Repos=Cilka.get("link").toString();
//                   System.out.println(Repos);
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
            System.out.println(Repos);
        }
        catch(ParseException e){
            TypeMessage="3";
            NomberLab="messageType, variant, link, lab";
            NomberVar="1";
            Repos="Неверная JSON строка";
            ErrorArg(NomberLab,NomberVar,Repos);
        }
    }

    public static void Priem() throws IOException
    {
        SetPort();
        if (port!=0)
        server = new ServerSocket(port);
        System.out.println("Sosdano");
        try {
            while (true) {
                // Блокируется до возникновения нового соединения:
                Socket clientSocket = server.accept();
                try {
                    serverList.add(new ServerSomthing(clientSocket)); // добавить новое соединенние в список
                } catch (IOException e) {
                    // Если завершится неудачей, закрывается сокет,
                    // в противном случае, нить закроет его при завершении работы:
                    clientSocket.close();
                }
            }
        } finally {
            server.close();
            System.out.println("Server1 zakrit");
        }
    }


    public static void main(String[] args) throws ParseException, IOException {
        Priem();
    }
}