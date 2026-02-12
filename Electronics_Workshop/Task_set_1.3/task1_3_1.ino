//EE25B089 M Nharen

#include <LiquidCrystal.h>

LiquidCrystal lcd(12,11,5,4,3,2);

void setup()
{
  pinMode(9,OUTPUT);
  pinMode(13,OUTPUT);
}

void loop()
{
  digitalWrite(9,HIGH);
  int val = digitalRead(10);
  if (val == 1)
  {
    lcd.setCursor(0,0);
    lcd.print("Interference detected");
     tone(13,200);
  }
  else
  {
    lcd.setCursor(0,0);
    lcd.print("No Interference");
    noTone(11);
  }
  delay(50);
}
