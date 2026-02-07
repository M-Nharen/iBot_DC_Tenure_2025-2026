//EE25B089 M Nharen

void setup()
{
    pinMode(A0,INPUT);
  	Serial.begin(9600);
}

void loop()
{
  	int IR_Reading = analogRead(A0);
  	Serial.println(IR_Reading);
  	delay(50);
  	
}
 