#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>

ESP8266WiFiMulti wifiMulti;

String ssid = "haha you thought";
String ssid_pass = "not a real password";

void setup() {
  Serial.begin(115200);
  delay(10);
  Serial.println('\n');

  wifiMulti.addAP(ssid, ssid_pass);

  Serial.println("Connecting ...");
  int i = 0;
  while(wifiMulti.run() != WL_CONNECTED) {
    delay(1000);
    Serial.println('.');
  }
  Serial.println('\n');
  Serial.println("Connected to ");
  Serial.println(WiFi.SSID());
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());

}

void loop() {
  // put your main code here, to run repeatedly:

}
