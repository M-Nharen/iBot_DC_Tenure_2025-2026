//EE25B089 M Nharen

void setup()
{
    pinMode(6,INPUT);
  	Serial.begin(9600);
}

void loop()
{
  	int IR_Reading = digitalRead(6);
  	Serial.println(IR_Reading);
  	delay(50);
  	
}