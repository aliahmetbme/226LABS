#include <LiquidCrystal.h>

// LCD
LiquidCrystal lcd(36, 37, 26, 27, 28, 29);

// 7 Segment Pins
int aPin = 22;
int bPin = 23;
int cPin = 24;
int dPin = 25;
int ePin = 26;
int fPin = 27;
int gPin = 28;

// Digit Pins
int gnd1 = 33;
int gnd2 = 34;
int gnd3 = 35;
int gnd4 = 36;

int count = 0;

unsigned long lastUpdate = 0;

void setup() {

  // Segment pins
  pinMode(aPin, OUTPUT);
  pinMode(bPin, OUTPUT);
  pinMode(cPin, OUTPUT);
  pinMode(dPin, OUTPUT);
  pinMode(ePin, OUTPUT);
  pinMode(fPin, OUTPUT);
  pinMode(gPin, OUTPUT);

  // Digit pins
  pinMode(gnd1, OUTPUT);
  pinMode(gnd2, OUTPUT);
  pinMode(gnd3, OUTPUT);
  pinMode(gnd4, OUTPUT);

  // LCD
  lcd.begin(16, 2);

  lcd.setCursor(0, 0);
  lcd.print("Counter:");
}

void loop() {

  int d1 = count % 10;
  int d2 = (count / 10) % 10;
  int d3 = (count / 100) % 10;
  int d4 = (count / 1000) % 10;

  // multiplexing
  showDigit(gnd1, d1);
  showDigit(gnd2, d2);
  showDigit(gnd3, d3);
  showDigit(gnd4, d4);

  // increase every second
  if (millis() - lastUpdate >= 1000) {

    lastUpdate = millis();

    count++;

    if (count > 9999) {
      count = 0;
    }

    updateLCD();
  }
}

void updateLCD() {

  lcd.setCursor(0, 1);

  if (count < 10) lcd.print("000");
  else if (count < 100) lcd.print("00");
  else if (count < 1000) lcd.print("0");

  lcd.print(count);
  lcd.print(" ");
}

void showDigit(int digitPin, int number) {

  turnOffDigits();

  clearSegments();

  setNumber(number);

  digitalWrite(digitPin, HIGH);

  delay(3);

  digitalWrite(digitPin, LOW);
}

void turnOffDigits() {

  digitalWrite(gnd1, LOW);
  digitalWrite(gnd2, LOW);
  digitalWrite(gnd3, LOW);
  digitalWrite(gnd4, LOW);
}

void clearSegments() {

  digitalWrite(aPin, LOW);
  digitalWrite(bPin, LOW);
  digitalWrite(cPin, LOW);
  digitalWrite(dPin, LOW);
  digitalWrite(ePin, LOW);
  digitalWrite(fPin, LOW);
  digitalWrite(gPin, LOW);
}

void on(int pin) {

  digitalWrite(pin, HIGH);
}

void setNumber(int n) {

  switch (n) {

    case 0:
      on(aPin);
      on(bPin);
      on(cPin);
      on(dPin);
      on(ePin);
      on(fPin);
      break;

    case 1:
      on(bPin);
      on(cPin);
      break;

    case 2:
      on(aPin);
      on(bPin);
      on(dPin);
      on(ePin);
      on(gPin);
      break;

    case 3:
      on(aPin);
      on(bPin);
      on(cPin);
      on(dPin);
      on(gPin);
      break;

    case 4:
      on(bPin);
      on(cPin);
      on(fPin);
      on(gPin);
      break;

    case 5:
      on(aPin);
      on(cPin);
      on(dPin);
      on(fPin);
      on(gPin);
      break;

    case 6:
      on(aPin);
      on(cPin);
      on(dPin);
      on(ePin);
      on(fPin);
      on(gPin);
      break;

    case 7:
      on(aPin);
      on(bPin);
      on(cPin);
      break;

    case 8:
      on(aPin);
      on(bPin);
      on(cPin);
      on(dPin);
      on(ePin);
      on(fPin);
      on(gPin);
      break;

    case 9:
      on(aPin);
      on(bPin);
      on(cPin);
      on(dPin);
      on(fPin);
      on(gPin);
      break;
  }
}