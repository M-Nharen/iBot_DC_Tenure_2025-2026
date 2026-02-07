//EE25B089 M Nharen

void setup()
{
    pinMode(11,OUTPUT);
}

void loop()
{
    tone(11,200);
    delay(1000);
    noTone(11);
    delay(1000);
}