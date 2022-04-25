#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>

#define SERVER "wouldn't you want my ip?"
#define SSID_NET "nice try"
#define SSID_KEY "no pass here"

HTTPClient http;
WiFiClient client;

void setup() {
  Serial.begin(115200);
  delay(10);
  Serial.println('\n');

  WiFi.begin(SSID_NET, SSID_KEY);

  Serial.println("Connecting ...");

  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println('.');
  }
  Serial.println('\n');
  Serial.println("Connected to ");
  Serial.println(WiFi.SSID());
  Serial.print("IP address:\t");
  Serial.println(WiFi.localIP());

  //DONT FORGET TO CHANGE IP
  http.begin(client, "http://" SERVER "/endpoint");
  http.addHeader("Content-Type", "application/json");

  Serial.println(WiFi.macAddress());
  int httpCode = http.POST("{\"mac\":\"" + WiFi.macAddress() + "\"}");
  String payload = http.getString();

  Serial.println(httpCode);
  Serial.println(payload);

  http.end();

  httpCode = http.POST("{\"mac\":\"" + WiFi.macAddress() + "\",\"temp\":\"0\",\"log\":\"13\"}");
  payload = http.getString();
  
  Serial.println(httpCode);
  Serial.println(payload);
  
  http.end();

  ESP.deepSleep(15e6);
  
}

void loop() {
}
