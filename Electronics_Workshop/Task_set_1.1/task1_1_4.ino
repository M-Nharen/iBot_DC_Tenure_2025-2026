//EE25B089 M Nharen

void setup()
{
    pinMode(11,INPUT);
  	pinMode(10,OUTPUT);
  	Serial.begin(9600);
}

void loop()
{
  	digitalWrite(10,HIGH);
  	delayMicroseconds(10);
  	digitalWrite(10,LOW);
  	
  	long duration = pulseIn(11,HIGH);
  
  	long distance = duration*0.0343/2;
      
    Serial.println(distance);
    delay(10);  
  	
}
 