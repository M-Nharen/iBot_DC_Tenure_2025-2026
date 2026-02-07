#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

const int Width = 128;
const int Height = 64;
const int Reset_Pin = -1;

Adafruit_SSD1306 Display(Width, Height, &Wire, Reset_Pin);

void setup()
{
  Display.clearDisplay();

  Display.setTextSize(1);
  Display.setTextColor(WHITE);

  Display.setCursor(4, 28); 
  Display.print(F("HELLO WORLD "));

  Display.drawRect(80, 17, 40, 30, WHITE); 

  Display.display();

}

void loop()
{
}