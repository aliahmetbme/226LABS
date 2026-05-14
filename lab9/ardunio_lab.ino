/*
int LED1pin=44;//TASK1 define digital pin to number of LED1
int LED0pin=43;
int LED2pin=45;
int LED3pin=46; //TASK 4 define all LEDS
//TASK 2 Initialization digital pin
void setup() {
 pinMode(LED1pin, OUTPUT);
 pinMode(LED0pin, OUTPUT);
 pinMode(LED2pin, OUTPUT);
 pinMode(LED3pin, OUTPUT); //TASK 5 Initiliaze LEDS as output
}
void loop(){ // TASK 3 & TASK 6
digitalWrite(LED1pin,HIGH);
delay(1000);
digitalWrite(LED1pin,LOW);
delay(1000);
digitalWrite(LED2pin,HIGH);
delay(1000);
digitalWrite(LED2pin,LOW);
delay(1000);
digitalWrite(LED3pin,HIGH);
delay(1000);
digitalWrite(LED3pin,LOW);
delay(1000);
digitalWrite(LED0pin,HIGH);
delay(1000);
digitalWrite(LED0pin,LOW);
delay(1000);
 }
*/

int LED1pin = 44;
int LED0pin = 43;
int LED2pin = 45;
int LED3pin = 46;

int ledPins[] = {43, 44, 45, 46};
int btnPins[] = {38, 39, 40, 41};

int lastButonStates[] = {LOW, LOW, LOW, LOW};
int ledStates[] = {LOW, LOW, LOW, LOW};

void setup() {
  for (int i = 0; i < 4; i++) {
    pinMode(ledPins[i], OUTPUT);
    pinMode(btnPins[i], INPUT);
  }
}

void loop() {
  for (int i = 0; i < 4; i++) {
    int currentButonState = digitalRead(btnPins[i]);

    if (currentButonState == HIGH && lastButonStates[i] == LOW) {
      ledStates[i] = !ledStates[i];

      digitalWrite(ledPins[i], ledStates[i]);

      delay(500);
    }
    lastButonStates[i] = currentButonState;
  }
}