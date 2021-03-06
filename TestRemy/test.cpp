/* Photocell and temperture

Connect one end of the photocell to 5V, the other end to Analog 0.
Then connect one end of a 10K resistor from Analog 0 to ground
 */

int photocellPin = 0;     // the cell and 10K pulldown are connected to a0
int photocellReading;     // the analog reading from the analog resistor divider

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

    Serial.print("Temperatuur in C");
    Serial.print(degreesC);
    Serial.print("Lichtintensiteit ");
    Serial.print(photocellReading);     // the raw analog reading


    float getVoltage(int pin)
    {
        return (analogRead(pin) * 0.004882814);
    }


    // We'll have a few threshholds, qualitatively determined
    if (photocellReading < 10) {
        Serial.println(" - Dark");
    } else if (photocellReading < 200) {
        Serial.println(" - Dim");
    } else if (photocellReading < 500) {
        Serial.println(" - Light");
    } else if (photocellReading < 800) {
        Serial.println(" - Bright");
    } else {
        Serial.println(" - Very bright");
    }
    delay(1000);
}