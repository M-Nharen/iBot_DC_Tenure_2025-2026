//EE25B089 M Nharen

char val = 'a'

#include <BluetoothSerial.h>

BluetoothSerial SerialBT;

void setup()
{
    SerialBT.begin("ESP32_Nharen");
    pinMode(18,OUTPUT);
}

void loop()
{

    if (SerialBT.available()) { 
        val = SerialBT.read();
    }

    if (val == '1')
    {
        digitalWrite(18,HIGH);
    }
    if (val == '0')
    {
        digitalWrite(18,LOW);
    }
}