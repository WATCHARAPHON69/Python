#include <Ethernet.h> //Load Ethernet Library
#include <EthernetUdp.h> //Load UDP Library
#include <SPI.h> //Load the SPI Library
bool Status = true;
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xEE}; //Assign a mac address
IPAddress ip(192, 168, 1, 243); //Assign my IP adress
unsigned int localPort = 8888; //Assign a Port to talk over
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];
String data; //String for our data
int packetSize; //Size of Packet
EthernetUDP Udp; //Define UDP Object
bool Led_status_1 = false;
bool Led_status_2 = false;
unsigned long period = 500; //ระยะเวลาที่ต้องการรอ
unsigned long last_time = 0; //ประกาศตัวแปรเป็น global เพื่อเก็บค่าไว้ไม่ให้ reset จากการวนloop
String DataSend[10];
String p = "";
int number1 = 0;
int number2 = 0;
void setup() {

  Serial.begin(9600); //Turn on Serial Port
  Ethernet.begin(mac, ip); //Initialize Ethernet
  Udp.begin(localPort); //Initialize Udp

  pinMode(13, OUTPUT);
  //delay(1500); //delay
  DataSend[1] = "80.500";
  DataSend[0] = "100.00";
  DataSend[3] = "900";

  Serial.println("Start");
}
void loop() {
  packetSize = Udp.parsePacket(); //Read theh packetSize
  //Serial.println("hhh");
  if (packetSize > 0) { //Check to see if a request is present
    Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE); //Reading the data request on the Udp
    String data(packetBuffer); //Convert packetBuffer array to string datReq
    if (data[0] == 'N') {
      digitalWrite(13, HIGH);
    } else {
      digitalWrite(13, LOW);
    }
    if ( millis() - last_time > period) {

      last_time = millis(); //เซฟเวลาปัจจุบันไว้เพื่อรอจนกว่า millis() จะมากกว่าตัวมันเท่า period

      number1 = number1 + 2;
      number2 = number2 + 1;
      if (number1 == 100) {
        number1 = 0;
      }
      if (number2 == 100) {
        number2 = 0;
      }
    }

    DataSend[0] = String(number1);
    DataSend[1] = String(number2);

    Serial.println(data);

    p = "\n" + DataSend[0] + "\n" + DataSend[1] + "\n" + DataSend[3];
    Udp.beginPacket(Udp.remoteIP(), Udp.remotePort()); //Initialize packet send
    Udp.print(p);
    Udp.endPacket(); //End the packet

  }
  memset(packetBuffer, 0, UDP_TX_PACKET_MAX_SIZE);
}
