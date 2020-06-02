import java.net.Socket;
import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.LinkedList;

import javax.swing.text.Document;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.json.simple.*;
import org.json.simple.parser.*;

import org.w3c.dom.NodeList;
public class ServerSomthing {
    private Socket socket; // сокет, через который сервер общается с клиентом,
    // кроме него - клиент и сервер никак не связаны
    private static Socket clientSocket; //Сокет клиента
    private static ServerSocket server; //Сокет сервера
    private static BufferedReader in; //Чтобы принимать и отправлять сообщения буферы
    private static BufferedWriter out;
    public Selenium selenium;
    public static String TypeMessage;
    public static String NomberVar;
    public static String Repos;
    public static String NomberLab;
    public static String Oshibka;
    public static boolean conec=false;

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


    public ServerSomthing(Socket socket) throws IOException {

        this.socket = socket;
        // если потоку ввода/вывода приведут к генерированию исключения, оно проброситься дальше
        in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));

        out.write("New connection!");
        out.flush();


        run(); // вызываем run()
    }
    public void run() {
        String word;
        try {
            word = in.readLine();

            System.out.println(word);


            try {
                System.out.println(word);
                JSONObject Cilka = (JSONObject)JSONValue.parseWithException(word);
                String proverka=Cilka.toString();
                conec=false;

                if(conec==false) {
                    TypeMessage=Cilka.get("messageType").toString();
//                    System.out.println(TypeMessage);
                    String TestTipeMes1="";
                    if(TypeMessage.equals(TestTipeMes1)&&conec==false)
                    {
                        TypeMessage="3";
                        NomberLab="messageType";
                        NomberVar="2";
                        Repos="Отстуствует ключ";
                        conec=true;
                        send(ErrorArg(NomberLab,NomberVar,Repos));
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
                                send(ErrorArg(NomberLab,NomberVar,Repos));
                            }
                        }
                        catch(NumberFormatException e) {
                            TypeMessage="3";
                            NomberLab="messageType";
                            NomberVar="4";
                            Repos="Не тот тип данных";
                            send(ErrorArg(NomberLab,NomberVar,Repos));
                            conec=true;
                        }
                    }}
                System.out.println(TypeMessage);

                if(conec==false) {
                    NomberLab=Cilka.get("lab").toString();
//                    System.out.println(NomberLab);
                    String TestNomberLab1="";
                    if(NomberLab.equals(TestNomberLab1)&&conec==false)
                    {
                        TypeMessage="3";
                        NomberLab="lab";
                        NomberVar="2";
                        Repos="Отстуствует ключ";
                        send(ErrorArg(NomberLab,NomberVar,Repos));
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
                                send(ErrorArg(NomberLab,NomberVar,Repos));
                                conec=true;
                            }
                        }
                        catch(NumberFormatException e) {
                            TypeMessage="3";
                            NomberLab="lab";
                            NomberVar="4";
                            Repos="Не тот тип данных";
                            send(ErrorArg(NomberLab,NomberVar,Repos));
                            conec=true;
                        }
                    } }
                System.out.println(NomberLab);


                if(conec==false) {
                    NomberVar=Cilka.get("variant").toString();
//                    System.out.println(NomberVar);
                    String TestNomberVar1="";
                    if(NomberVar.equals(TestNomberVar1)&&conec==false)
                    {
                        TypeMessage="3";
                        NomberLab="variant";
                        NomberVar="2";
                        Repos="Отстуствует ключ";
                        send(ErrorArg(NomberLab,NomberVar,Repos));
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
                                send(ErrorArg(NomberLab,NomberVar,Repos));
                                conec=true;
                            }
                        }
                        catch(NumberFormatException e) {
                            TypeMessage="3";
                            NomberLab="variant";
                            NomberVar="4";
                            Repos="Не тот тип данных";
                            send(ErrorArg(NomberLab,NomberVar,Repos));
                            conec=true;
                        }
                    }}
                System.out.println(NomberVar);

                if(conec==false) {
                    Repos=Cilka.get("link").toString();
//                  System.out.println(Repos);
                    try {
                        String s2="https://github.com/";
                        String s3="";
                        if(Repos.equals(s3)&&conec==false)
                        {
                            TypeMessage="3";
                            NomberLab="link";
                            NomberVar="2";
                            Repos="Отстуствует ключ";
                            send(ErrorArg(NomberLab,NomberVar,Repos));
                            conec=true;
                        }
                        if(conec==false) {
                            String s1=Repos.substring(0,19);
                            if(!s1.equals(s2)&&conec==false) {
                                TypeMessage="3";
                                NomberLab="link";
                                NomberVar="3";
                                Repos="Неверное значение";
                                send(ErrorArg(NomberLab,NomberVar,Repos));
                                conec=true;}
                        }

                    }
                    catch(StringIndexOutOfBoundsException e) {
                        TypeMessage="3";
                        NomberLab="link";
                        NomberVar="3";
                        Repos="Неверное значение";
                        send(ErrorArg(NomberLab,NomberVar,Repos));
                        conec=true;
                    }}
                System.out.println(Repos);
            }
            catch(ParseException e){
                TypeMessage="3";
                NomberLab="messageType, variant, link, lab";
                NomberVar="1";
                Repos="Неверная JSON строка";
                conec=true;
                send(ErrorArg(NomberLab,NomberVar,Repos));
            }


            if(conec==false) {
                selenium=new Selenium(Repos,NomberVar);

                selenium.test();
                send( Otvet(selenium.Get_Ozenka(),selenium.Get_Result())); // отослать принятое сообщение с
                selenium.driver.quit();

            }


        } catch (IOException e) {

        }
    }

    private void send(String msg) {
        try {
            System.out.println(msg);
            out.write(msg);

            out.flush();
        } catch (IOException ignored) {}
    }
}


