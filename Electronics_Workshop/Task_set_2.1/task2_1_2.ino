//M Nharen EE25B089

#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "Mi 11X";
const char* password = "Nharen07";

WebServer server(80);

void on()
{
  digitalWrite(18,HIGH);
  server.send(200,"text/html","<h1>LED turned ON</h1>");
}

void off()
{
  digitalWrite(18,LOW);
  server.send(200,"text/html","<h1>LED turned OFF</h1>");
}

void error()
{
  server.send(404,"text/html","<h1>Error 404 Page not Found</h1>");
}

void setup() {
  Serial.begin(9600);

  pinMode(18,OUTPUT);
  digitalWrite(18,HIGH);
  
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

  server.on("/H",on);
  server.on("/L",off);
  server.onNotFound(error);

  server.begin();
  Serial.println("Server has started.");
}

void loop() {
  server.handleClient();
}
