//EE25B089 M Nharen

bool on = false;
bool prevhigh = true;

void setup()
{
    pinMode(11,OUTPUT);
    pinMode(9,INPUT_PULLUP);
}

void loop()
{
  	int input = digitalRead(9);
  	if (input == LOW && prevhigh == true)
    {
      on = !on;
      prevhigh = false;
    }

    if (input == HIGH)
    {
      prevhigh = true;
    }
  
  	if (on == true)  	
    {
      digitalWrite(11,HIGH);
    }
  	else
    {
      digitalWrite(11,LOW);
    }
  	delay(250);
}
 
  	