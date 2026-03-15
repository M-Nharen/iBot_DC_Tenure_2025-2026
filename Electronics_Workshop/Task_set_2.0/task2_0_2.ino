//M Nharen EE25B089

void setup() {
  pinMode(18,OUTPUT);
  ledcAttach(18, 5000, 10);
}

void loop() {
  for (int i = 0; i <= 1023; i++) {
    ledcWrite(18, i);
    delay(1);
  }
  for (int i = 1023; i >= 0; i--) {
    ledcWrite(18, i);
    delay(1);
  }
}
