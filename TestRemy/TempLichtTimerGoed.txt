int ldrPin = 0;
int ldrReading = 0;
const int temperaturePin = 1;

float averageTemp = 0;
int averageLight = 0; 

// elk "event/timer" (voor input,output) krijgt zijn eigen variabele
unsigned long previousMillis = 0;
unsigned long previousMillis40 = 0;
unsigned long previousMillis30 = 0;
unsigned long previousMillis1 = 0;
unsigned long previousMillis10 = 0;
unsigned long previousMillis15 = 0;

int interval40 = 40000; // 40sec
int interval30 = 30000; // 30sec
int interval10 = 10000; // 10sec
int interval15 = 15000; // 15se
int interval1 = 1000; // 1sec

void setup()
{
  //Start Serial port
  Serial.begin(9600);        // start serial for output - for testing
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
    averageLight += ldrReading;
    averageTemp += degreesC;
    delay(1000);
    previousMillis1 = currentMillis;
    
  }
  if((unsigned long)(currentMillis - previousMillis10) >= interval10){
    Serial.print("Gemiddelde licht afgelopen 40sec: ");
    Serial.print(averageLight / 10);
    Serial.print("\n");
    averageLight = 0;
    previousMillis10 = currentMillis;
  }

  if((unsigned long)(currentMillis - previousMillis15) >= interval15) {
    Serial.print("Gemiddelde temperatuur afgelopen 30sec: ");
    Serial.print(averageTemp / 15);
    Serial.print("\n");
    averageTemp = 0;
    previousMillis15 = currentMillis;
  }

}

float getVoltage(int pin)
{
  return (analogRead(pin) * 0.004882814);
}