//M Nharen EE25B089

#include <WiFi.h>

void setup() {
  Serial.begin(9600);
  
  WiFi.mode(WIFI_STA); 

  Serial.print("MacAddress: ");
  Serial.println(WiFi.macAddress());
}

void loop() {
}
