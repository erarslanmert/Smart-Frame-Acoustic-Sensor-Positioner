#include "FeedBackServo.h"
#include <Servo.h>
// define feedback signal pin and servo control pin
#define FEEDBACK_PIN 2
#define SERVO_PIN 3

// set feedback signal pin number
FeedBackServo servo = FeedBackServo(FEEDBACK_PIN);
Servo myservo;

String inByte;
int pos;

void setup() {
    // set servo control pin number
    Serial.begin(9600);
    myservo.attach(SERVO_PIN);
    servo.setServoControl(SERVO_PIN);
    servo.setKp(1.0);
    delay(20);
}

void loop() {
    // rotate servo to 270 and -180 degrees(with contains +-4 degrees error) each 1 second.
    
    if(Serial.available())  // if data available in serial port
    { 
      inByte = Serial.readStringUntil('\n'); // read data until newline
      pos = inByte.toInt();   // change datatype from string to integer        
      servo.rotate(pos,4);
      myservo.write(93);
      // move servo
    }
    Serial.println(servo.Angle());
    delay(1000);
}
