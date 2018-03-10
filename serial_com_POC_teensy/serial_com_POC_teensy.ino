
const int ledPin =  13;      // the number of the LED pin

// Variables will change:
int ledState = LOW;// ledState used to set the LED
String inputString = "";         // a String to hold incoming data
boolean Light = false;  // whether the string is complete






void setup()
  {
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);  
    Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);    

  }

void loop() 
{
  // put your main code here, to run repeatedly:
  if(Light)
  {
    digitalWrite(ledPin, HIGH);
  }
  else if(!Light)
  {
    digitalWrite(ledPin, LOW);
  }
  
}







/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == 'L') 
      {
        Light = true;
      }
     else if(inChar == 'H')
      {
        Serial.println("GoatCart");
      }
     else 
     {
      Light = false;
     }
  }
}
