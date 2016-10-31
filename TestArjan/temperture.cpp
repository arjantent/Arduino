const int temperaturePin = 1;


void setup()
{
    Serial.begin(9600);
}


void loop()
{

    float voltage, degreesC, degreesF;

    voltage = getVoltage(temperaturePin);


    degreesC = (voltage - 0.5) * 100.0;


    Serial.print("voltage: ");
    Serial.print(voltage);
    Serial.print("  deg C: ");
    Serial.print(degreesC);
    Serial.print("  deg F: ");
    Serial.println(degreesF);



    delay(10000); // repeat once per second (change as you wish!)
}


float getVoltage(int pin)
{
    // This function has one input parameter, the analog pin number
    // to read. You might notice that this function does not have
    // "void" in front of it; this is because it returns a floating-
    // point value, which is the true voltage on that pin (0 to 5V).

    // You can write your own functions that take in parameters
    // and return values. Here's how:

    // To take in parameters, put their type and name in the
    // parenthesis after the function name (see above). You can
    // have multiple parameters, separated with commas.

    // To return a value, put the type BEFORE the function name
    // (see "float", above), and use a return() statement in your code
    // to actually return the value (see below).

    // If you don't need to get any parameters, you can just put
    // "()" after the function name.

    // If you don't need to return a value, just write "void" before
    // the function name.

    // Here's the return statement for this function. We're doing
    // all the math we need to do within this statement:

    return (analogRead(pin) * 0.004882814);

    // This equation converts the 0 to 1023 value that analogRead()
    // returns, into a 0.0 to 5.0 value that is the true voltage
    // being read at that pin.
}

// Other things to try with this code:

//   Turn on an LED if the temperature is above or below a value.

//   Read that threshold value from a potentiometer - now you've
//   created a thermostat!
