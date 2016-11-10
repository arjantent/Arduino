// Pin numbers
const int temperaturePin = 1;
const int ldrPin = 0;
const int ledGroen = 8;
const int ledGeel = 9;
const int ledRood = 10;

int ledState = LOW;

int ldrReading = 0;
int countLight = 0;
float countTemp = 0;
int averageTemp = 20;
int averageLight = 800; 

int standaardtemp = 10;
int standaardlux = 700;

// elk "event/timer" (voor input,output) krijgt zijn eigen variabele
unsigned long previousMillis = 0;
unsigned long previousMillis1s = 0;
unsigned long previousMillis40 = 0;
unsigned long previousMillis30 = 0;
unsigned long previousMillis1 = 0;
unsigned long previousMillis10 = 0;
unsigned long previousMillis15 = 0;
unsigned long previousMillis20 = 0;

int interval20 = 20000; // 20sec
int interval40 = 40000; // 40sec
int interval30 = 30000; // 30sec
int interval10 = 10000; // 10sec
int interval15 = 15000; // 15se
int interval1 = 1000; // 1sec
int interval1s = 1000; // 1sec

void setup()
{
  //Start Serial port
  Serial.begin(9600);        // start serial for output - for testing
  pinMode(ledGroen, OUTPUT);
  pinMode(ledGeel, OUTPUT);
  pinMode(ledRood, OUTPUT);
}

void loop()
{   
  

  ldrReading = analogRead(ldrPin);
  float voltage,degreesC;
  voltage = getVoltage(temperaturePin);
  degreesC = (voltage - 0.5) * 100.0;

  // geef huidige tijd
  unsigned long currentMillis = millis();

  // lees waarde van LDR per seconde en stop het in de variabele averageLight
  if((unsigned long)(currentMillis - previousMillis1) >= interval1){
    previousMillis1 = currentMillis;
    countLight += ldrReading;
    countTemp += degreesC;
    delay(1000);

  }
  
  if((unsigned long)(currentMillis - previousMillis10) >= interval10){
    averageLight = countLight / 10;
    countLight = 0;
    previousMillis10 = currentMillis;
  }
  if((unsigned long)(currentMillis - previousMillis15) >= interval15) {
    previousMillis15 = currentMillis;
    averageTemp = countTemp / 15;
    countTemp = 0;
  
  }


 if((unsigned long)(currentMillis - previousMillis20) >= interval20) {
    previousMillis20 = currentMillis;

    if (averageTemp >= standaardtemp && averageLight >= standaardlux) {
      digitalWrite(ledGroen,HIGH);
      digitalWrite(ledRood,LOW);
      for (int i=0; i <4; i++){
        Serial.print("hoi");
      if((unsigned long)(currentMillis - previousMillis1s) >= interval1s){
      previousMillis1s = currentMillis;
      
      if (ledState == LOW){
        ledState = HIGH;
        }
        else{
          ledState = LOW;
          }
      digitalWrite(ledGeel, ledState);
      
    }}
    digitalWrite(ledGroen, LOW);
    digitalWrite(ledRood, HIGH);
  }
 }



  if (Serial.available()) {
        char serialListener = Serial.read();
        if (serialListener == 'H') {
            digitalWrite(ledGroen, HIGH);
        }
        else if (serialListener == 'L') {
            digitalWrite(ledGroen, LOW);
        }
        else if (serialListener == 'A') {
            digitalWrite(ledRood, HIGH);
        }
        else if (serialListener == 'U') {
            digitalWrite(ledRood, LOW);
        }
        else if (serialListener == 'Q') {
            digitalWrite(ledGeel, HIGH);
        }
        else if (serialListener == 'W') {
            digitalWrite(ledGeel, LOW);
        }
        else if (serialListener == 'N') {
            digitalWrite(ledGeel, HIGH);
        }
        else if (serialListener == 'M') {
            digitalWrite(ledGeel, LOW);
        }
        else if(serialListener == 'V') {
          Serial.print(averageLight);
          Serial.print(",");
          Serial.print(averageTemp);
          Serial.print("\n");
         }
         
        else if (serialListener == 'X') {
         Serial.println(50);
         }


}
}

float getVoltage(int pin)
{
  return (analogRead(pin) * 0.004882814);
}
