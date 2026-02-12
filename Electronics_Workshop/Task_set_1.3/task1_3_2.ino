//EE25B089 M Nharen

#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

const int Width = 128;
const int Height = 64;
const int Reset_Pin = -1;

int up = 3;
int down = 4;
int left = 5;
int right = 6;
int location = 0;
int future_location = 0;

Adafruit_SSD1306 Display(Width, Height, &Wire, Reset_Pin);

void setup()
{
  if(!Display.begin(SSD1306_SWITCHCAPVCC, 0x3C))
  {
    Serial.println("SSD1306 Allocation Failed");
  }

  Display.clearDisplay();

  pinMode(up, INPUT_PULLUP);
  pinMode(down, INPUT_PULLUP);
  pinMode(left, INPUT_PULLUP);
  pinMode(right, INPUT_PULLUP);

  Display.setTextSize(1);
  Display.setTextColor(WHITE);
}

void loop()
{
    int upvalue = digitalRead(up);
    int downvalue = digitalRead(down);
    int leftvalue = digitalRead(left);
    int rightvalue = digitalRead(right);

    if (upvalue==LOW)
    {
        future_location = cell(1,location);
    }
    else if (downvalue==LOW)
    {
        future_location = cell(3,location);
    }
    else if (leftvalue==LOW)
    {
        future_location = cell(2,location);
    }
    else if (rightvalue==LOW)
    {
        future_location = cell(0,location);
    }

    show(future_location);
    location = future_location;
}

int cell(int action, int current_location)
{
  int locationj = current_location%16;
  int locationi = (int) (current_location - locationj)/16;

  int mapi[] = {0,-1,0,1};
  int mapj[] = {1,0,-1,0};

  int i = (((locationi + mapi[action]) % 16) + 16) % 16;
  int j = (((locationj + mapj[action]) % 16) + 16) % 16;

  return 16*i+j;
}

void show(int location)
{
  Display.clearDisplay();
  int locationj = (location%16)*8;
  int locationi = (int) ((location - locationj)/16)*8;

  Display.fillRect(locationj,locationi,8,8,WHITE);

  Display.display();
}