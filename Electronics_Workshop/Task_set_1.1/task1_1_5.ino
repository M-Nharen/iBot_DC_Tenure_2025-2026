//EE25B089 M Nharen

void setup()
{
    pinMode(A0,INPUT);
    pinMode(LED_BUILTIN,OUTPUT);
}

void loop()
{
    int sound_volume = analogRead(A0);
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