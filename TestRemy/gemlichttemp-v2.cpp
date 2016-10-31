/* Photocell and temperture
Connect one end of the photocell to 5V, the other end to Analog 0.
Then connect one end of a 10K resistor from Analog 0 to ground
 */

int photocellPin = 0;     // the cell and 10K pulldown are connected to a0
int photocellReading;     // the analog reading from the analog resistor divider

float averageTemp = 0;
int averageLight = 0;
const int temperaturePin = 1;
int counter =0;

void setup(void) {
    // We'll send debugging information via the Serial monitor
    Serial.begin(9600);
}

void loop(void) {
    photocellReading = analogRead(photocellPin);
    
    
    float voltage,degreesC;

    voltage = getVoltage(temperaturePin);
    degreesC = (voltage - 0.5) * 100.0;



    for (int i = 0; i < 10; i++) {
       counter += 1;
       averageLight += photocellReading;
       averageTemp += degreesC;
       delay(1000);

       if (counter== 5) {
          Serial.print("Gemiddelde lichtintensiteit afgelopen 30sec in Lux: ");
          Serial.print(averageLight / 5);
          Serial.print('\n');
          counter=0;
          averageLight=0;
       }
       
       
    }

   

    // print gemiddelde lichtintensiteit afgelopen 30 sec in Lux
   // Serial.print("Gemiddelde lichtintensiteit afgelopen 30 sec in Lux: ");
   // Serial.print(averageLight / 30);
   // Serial.print('\n');
   // averageLight = 0;
    
    // print gemiddelde temp in afgelopen 40sec in C
    Serial.print("Gemiddelde temperatuur afgelopen 40 sec in C:  ");
    Serial.print(averageTemp / 10);
    Serial.print('\n');
    averageTemp = 0;


}

float getVoltage(int pin)
{
    return (analogRead(pin) * 0.004882814);
}