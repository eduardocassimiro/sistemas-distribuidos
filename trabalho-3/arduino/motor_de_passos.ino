#include <Stepper.h> 

char serial;
const int stepsPerRevolution = 500; 

Stepper myStepper(stepsPerRevolution, 8,10,9,11); 
  
void setup() 
{ 
 Serial.begin(9600);
 myStepper.setSpeed(60);
} 
  
void loop() 
{
    serial = Serial.read();
    if(serial == 'x'){
      myStepper.step(-700);
    }
    if(serial == 'z'){
      myStepper.step(700);
    }
}
