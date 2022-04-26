#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <CommonDef.h>

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

  String mac = WiFi.macAddress();
  mac.replace(':', '_');

  http.begin(client, "http://" SERVER "/endpoint/" + mac);
  http.addHeader("Content-Type", "application/json");
  Serial.println("Looking for endpoint " + mac);
  String payload;
  int httpCode = http.GET();
  if(httpCode == 404) {
    Serial.println("Couldn't find my endpoint... creating one.");
    http.POST("{\"mac\":\"" + mac + "\"}");
    payload = http.getString();

    Serial.println(httpCode);
    Serial.println(payload);

  } else {
    Serial.println("Found my endpoint. Updating.");
    http.PATCH("");
    payload = http.getString();

    Serial.println(httpCode);
    Serial.println(payload);
    
  }

  http.end();

  http.begin(client, "http://" SERVER "/temp");
  http.addHeader("Content-Type", "application/json");
  Serial.println("Sending fake temperature data.");
  http.POST("{\"mac\":\"" + mac + "\",\"temp\":\"0\"}");
  http.end();
  Serial.println("Going to sleep for 15 seconds");
  // Make sure D0 is connected to RST for reboot
  ESP.deepSleep(5e6);
}

void loop() {
}
