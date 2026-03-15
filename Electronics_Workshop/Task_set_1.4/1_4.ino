# include <Wire.h>
# include <Adafruit_GFX.h>
# include <Adafruit_SSD1306.h>
# define OLED_Addr 0x3C


int password = 9999;
int w = 128;
int h = 64;

long seconds_passed = 0;
unsigned long start_millis = 0;
bool correct_password = false;
int button1 = 5;
int button1_state =0;
int button1_last =0;
int button2 = 4;
int button2_state =0;
int button2_last =0;
int button3 = 3;
int button3_state =0;
int button3_last =0;
int button4 = 2;
int button4_state =0;
int button4_last =0;
int check_button = 12;
int check_button_state = 0;
int check_button_last =0;
int debounce = 5;
int buzzer = 9;

Adafruit_SSD1306 Display(w,h,&Wire,-1);

int entered =0;
void setup()
{
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(button3, INPUT);
  pinMode(button4, INPUT);
  pinMode(check_button,INPUT);
  Serial.begin(9600);
  Wire.begin();

  if(!Display.begin(SSD1306_SWITCHCAPVCC, OLED_Addr))
  {
    Serial.println("oled not detected");
    while(true);
  }
  Display.clearDisplay();
  Display.setTextSize(1);
  Display.setTextColor(WHITE);
  Display.setCursor(15,27);
  Display.println("Security System");
  Display.display();
  delay(2000);
}

void loop()
{
  int reading = digitalRead(6);
  Serial.println(reading);
  if (reading == 1)
  {
    start_millis = millis();
    Display.clearDisplay();
    Display.setCursor(53,20);
    Display.print(60-seconds_passed);
    Display.display();
    while (millis()-start_millis < 60000)
    {
      if (((unsigned long)(millis()-start_millis)/1000) > seconds_passed)
      {
        seconds_passed += 1;
        Display.clearDisplay();
        Display.setCursor(53,20);
        Display.print(60-seconds_passed);
        Display.display();
      }

      button1_state = digitalRead(button1);
      button2_state = digitalRead(button2);
      button3_state = digitalRead(button3);
      button4_state = digitalRead(button4);
      check_button_state = digitalRead(check_button);

      if (button1_state==0 && button1_last==1)
      {
        Serial.println("button1 pressed");
        entered += 1;
        Serial.println(entered);
        Display.clearDisplay();
        Display.setCursor(53,20);
        Display.print(60-seconds_passed);
        Display.setCursor(53,40);
        Display.print(entered);
        Display.display();
      }
      else if(button2_state ==0 && button2_last ==1)
      {
        Serial.println("button2 pressed");
        entered += 10;
        Serial.println(entered);
        Display.clearDisplay();
        Display.setCursor(53,20);
        Display.print(60-seconds_passed);
        Display.setCursor(53,40);
        Display.print(entered);
        Display.display();
      }
      else if (button3_state==0 && button3_last==1)
      {
        Serial.println("button3 pressed");
        entered += 100;
        Serial.println(entered);
        Display.clearDisplay();
        Display.setCursor(53,20);
        Display.print(60-seconds_passed);
        Display.setCursor(53,40);
        Display.print(entered);
        Display.display();
      }
      else if(button4_state ==0 && button4_last ==1)
      {
        Serial.println("button4 pressed");
        entered += 1000;
        Serial.println(entered);
        Display.clearDisplay();
        Display.setCursor(53,20);
        Display.print(60-seconds_passed);
        Display.setCursor(53,40);
        Display.print(entered);
        Display.display();
      }
      else if(check_button_state ==0 && check_button_last ==1)
      {
        Serial.println("checking the value");
        if(password == entered){
          Serial.println("correct");
          Display.clearDisplay();
          Display.setCursor(15,20);
          Display.print(F("Correct Password"));
          Display.display();
          correct_password = true;
          break;
        }
        else{
          Serial.println("incorrect");
          Display.clearDisplay();
          Display.setCursor(15,20);
          Display.print(F("Incorrect Password"));
          Display.display();
          while (true)
          {
            tone(buzzer,1000);
          }
        }
        entered = 0;
      }

      button2_last = button2_state;
      button1_last = button1_state;
      button3_last = button3_state;
      button4_last = button4_state;
      check_button_last = check_button_state;

      delay(debounce);
    }

    if (reading == 1 && correct_password == false)
    {
      Display.clearDisplay();
      Display.setCursor(7,20);
      Display.print(F("Time Limit Exceeded"));
      Display.display();

      while (true)
      {
        tone(buzzer,1000);
      }
    }

    correct_password = false;
  }
 
}