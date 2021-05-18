/*
This code is modified from summer camp heat controlling
workshop for use in Heat Quilt by Zoe Kaputa

---------- 
modified for summer camp heat controlling workshop:
instead of LED, it is connected to heat element on pin 10 and 11
as you press the button it triggers a simple sequence 
2013 July eTextile summercamp
www.eTextile-summercamp.org
---------
 
 
 created 2005
 by DojoDave <http://www.0j0.org>
 modified 30 Aug 2011
 by Tom Igoe
 
 This example code is in the public domain.
 
 http://www.arduino.cc/en/Tutorial/Button
 */

// constants won't change. They're used here to 
// set pin numbers:
const int heatPin1 =  9;
const int heatPin2 =  10;


void setup() {
  // initialize the LED pin as an output:
  pinMode(heatPin1, OUTPUT);      
  pinMode(heatPin2, OUTPUT); 
}

void loop(){
  // start the heat sequence
  digitalWrite(heatPin1, HIGH);
  digitalWrite(heatPin2, HIGH);
  delay(3000); // you can change the timing as you like, 1sec=1000 //10 sec on
  digitalWrite(heatPin1, LOW);
  digitalWrite(heatPin2, LOW);
  delay(3000); // you can change the timing as you like, 1sec=1000 //15 sec on

}
