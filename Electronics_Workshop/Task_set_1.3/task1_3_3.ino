//EE25B089 M Nharen

#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

const int Width = 128;
const int Height = 64;
const int Reset_Pin = -1;

Adafruit_SSD1306 Display(Width, Height, &Wire, Reset_Pin);

void setup()
{
  if(!Display.begin(SSD1306_SWITCHCAPVCC, 0x3C))
  {
    Serial.println("SSD1306 Allocation Failed");
  }

  Serial.begin(9600);

  Display.clearDisplay();
  Display.setTextSize(1);
  Display.setTextColor(WHITE);
}

void loop()
{
    Display.clearDisplay();

    int sound_volume = analogRead(A0);
    Serial.println(sound_volume);

    int baseline = 200;
    float alpha = 0.5;

    if (sound_volume >= baseline)
    {
        Display.fillRect(54,32-alpha*(sound_volume-baseline),20,alpha*(sound_volume-baseline),WHITE);
    }
    else
    {
        Display.fillRect(54,32,20,alpha*(baseline-sound_volume),WHITE);
    }

    Display.display();
    delay(50);
}