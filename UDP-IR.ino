#include <SPI.h>
#include <Ethernet.h>
#include <EthernetUdp.h>
#include <IRremote.h>

EthernetUDP Udp;
byte mac[] = {0x90, 0xA2, 0xDA, 0x10, 0xDE, 0x6F};
IPAddress ip(10,33,109,122);
int broche_reception = 7;
IRrecv reception_ir(broche_reception);
decode_results decode_ir;
unsigned int localport = 8888;

IPAddress remoteIP(IP_ras);
unsigned int remotePort = 8888;

void setup(){
  Serial.begin(9600);
  Serial.println("****************");
  Serial.println("Serial Port OK");
  Ethernet.begin(mac,ip);
  Serial.print("IP : ");
  Serial.println(Ethernet.localIP());
  Udp.begin(localport);
  Udp.beginPacket(remoteIP, remotePort);
  Udp.println("Begin");
  Udp.endPacket();
  reception_ir.enableIRIn();
}

void loop(){
  if (reception_ir.decode(&decode_ir)){
    Serial.println(decode_ir.value, HEX);
    Udp.beginPacket(remoteIP, remotePort);
    Udp.println(decode_ir.value, HEX);
    Udp.endPacket();
    reception_ir.resume();
  }
 }
  
