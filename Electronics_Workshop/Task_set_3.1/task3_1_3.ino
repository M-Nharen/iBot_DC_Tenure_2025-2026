#include <esp_now.h>
#include <WiFi.h>

typedef struct buttoncollage {
  int button1;
  int button2;
  int button3;
  int button4;
} buttoncollage;

buttoncollage myData;

void control()
{
    digitalWrite(33,myData.button1 == 0 ? LOW:HIGH);
    digitalWrite(25,myData.button2 == 0 ? LOW:HIGH);
    digitalWrite(26,myData.button3 == 0 ? LOW:HIGH);
    digitalWrite(27,myData.button4 == 0 ? LOW:HIGH);
}

void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len) {
    memcpy(&myData, incomingData, sizeof(myData));
    control();
}

void setup()
{
    WiFi.mode(WIFI_STA);

    if (esp_now_init() != ESP_OK) {
        Serial.println("Error initializing ESP-NOW");
        return;
    }

    esp_now_register_recv_cb(OnDataRecv);
}

void loop()
{
}

