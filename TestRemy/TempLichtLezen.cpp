// Pin numbers
const int temperaturePin = 1;
const int ldrPin = 0;
const int ledGroen = 4;
const int ledGeel = 3;
const int ledRood = 2;

int ldrReading = 0;
int countLight = 0;
float countTemp = 0;
float averageTemp = 0;
int averageLight = 0; 

// elk "event/timer" (voor input,output) krijgt zijn eigen variabele
unsigned long previousMillis = 0;
unsigned long previousMillis60 = 0;
unsigned long previousMillis40 = 0;
unsigned long previousMillis30 = 0;
unsigned long previousMillis1 = 0;
unsigned long previousMillis10 = 0;
unsigned long previousMillis15 = 0;
unsigned long previousMillis20 = 0;

int interval60 = 60000; // 60sec
int interval20 = 20000; // 20sec
int interval40 = 40000; // 40sec
int interval30 = 30000; // 30sec
int interval10 = 10000; // 10sec
int interval15 = 15000; // 15se
int interval1 = 1000; // 1sec

const long ledBlink = 1000; // blinkled interval

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

  if((unsigned long)(currentMillis - previousMillis60) >= interval60) {
    Serial.print("Gemiddelde licht afgelopen 40sec: ");
    Serial.print(averageLight);
    Serial.print("\n");
    Serial.print("Gemiddelde temperatuur afgelopen 30sec: ");
    Serial.print(averageTemp);
    Serial.print("\n");
    previousMillis60 = currentMillis;
  }
  }
  if((unsigned long)(currentMillis - previousMillis30) >= interval30){
    averageLight = countLight / 30;
    countLight = 0;
    previousMillis10 = currentMillis;
  }
  if((unsigned long)(currentMillis - previousMillis40) >= interval40) {
    previousMillis15 = currentMillis;
    averageTemp = countTemp / 40;
    countTemp = 0;
  }

}

float getVoltage(int pin)
{
  return (analogRead(pin) * 0.004882814);
}