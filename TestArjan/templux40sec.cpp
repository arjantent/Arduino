/* Photocell and temperture

Connect one end of the photocell to 5V, the other end to Analog 0.
Then connect one end of a 10K resistor from Analog 0 to ground
 */

int photocellPin = 0;     // the cell and 10K pulldown are connected to a0
int photocellReading;     // the analog reading from the analog resistor divider

int gemiddelde = 0;
const int temperaturePin = 1;

void setup(void) {
    // We'll send debugging information via the Serial monitor
    Serial.begin(9600);
}

void loop(void) {
    photocellReading = analogRead(photocellPin);

    float voltage,degreesC;

    voltage = getVoltage(temperaturePin);
    degreesC = (voltage - 0.5) * 100.0;

    for(int i = 0 ; i < 41; i++) {
        gemiddelde += degreesC;
        delay(1000);
    }

    Serial.print("Gemiddelde temperatuur afgelopen 40 seconden in C:  ");
    Serial.print(gemiddelde / 40);
    Serial.print('\n');
    gemiddelde = 0;


}

float getVoltage(int pin)
{
    return (analogRead(pin) * 0.004882814);
}