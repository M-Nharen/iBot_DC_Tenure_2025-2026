//M Nharen EE25B089

#include <WiFi.h>

const char* ssid = "Mi 11X";
const char* password = "Nharen07";

void setup() {
  Serial.begin(9600);
  
  WiFi.mode(WIFI_STA); 

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected!");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
}
