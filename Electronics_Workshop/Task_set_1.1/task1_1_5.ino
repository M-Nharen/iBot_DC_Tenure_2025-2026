//EE25B089 M Nharen

void setup()
{
    pinMode(A0,INPUT);
    pinMode(LED_BUILTIN,OUTPUT);
    Serial.begin(9600);
}

void loop()
{
    int sound_volume = analogRead(A0);
    Serial.println(sound_volume);
    if (sound_volume>100)
    {
        digitalWrite(LED_BUILTIN,HIGH);
        delay(2000);
        digitalWrite(LED_BUILTIN,LOW);
    }
    else
    {
        delay(50);
    }
}