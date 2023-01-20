#include <SPI.h>
#include <Ethernet.h>
#include <EthernetUdp.h>
#include <IRremote.h>

EthernetUDP Udp;
byte mac[] = {0x90, 0xA2, 0xDA, 0x10, 0xDD, 0x93};
IPAddress ip(10,33,109,191);
int broche_reception = 7;
IRrecv reception_ir(broche_reception);
decode_results decode_ir;
unsigned int localport = 5002;

IPAddress remoteIP(10,33,109,106);
unsigned int remotePort = 5002;

void setup(){
  Serial.begin(9600);
  Ethernet.begin(mac,ip);
  Serial.println(Ethernet.localIP());
  Udp.begin(localport);
  Udp.beginPacket(remoteIP, remotePort);
  Udp.endPacket();
  reception_ir.enableIRIn();
}

void loop(){
  if (reception_ir.decode(&decode_ir)){
    Serial.println(decode_ir.value, HEX);
    Serial.println(decode_ir.value);
    Udp.beginPacket(remoteIP, remotePort);
    if (decode_ir.value != 4294967295){
      Serial.println("salut");
      Udp.write(decode_ir.value);
    }
    Udp.endPacket();
    reception_ir.resume();
  }
 }
  
