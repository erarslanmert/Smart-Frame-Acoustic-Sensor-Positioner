#include "FeedBackServo.h"
// define feedback signal pin
#define FEEDBACK_PIN 2

// set feedback signal pin number
FeedBackServo servo = FeedBackServo(FEEDBACK_PIN);

void setup() {
    // serial communication start with 115200 bps
    Serial.begin(9600);
}

void loop() {
    
    Serial.println(servo.Angle());
}
