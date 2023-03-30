/*
  Analog Feedback Servo Calibration Demo
  feedback_servo_calib.ino
  Uses S1213 Analog Feedback Servo Motor
  Results displayed on Serial Monitor
 
  DroneBot Workshop 2019
  https://dronebotworkshop.com
*/
 
// Include Arduino Servo Library
#include <Servo.h> 
 
// Control and feedback pins
int servoPin = A5;
int feedbackPin = 2;
 
// Value from feedback signal
int feedbackValue;
 
// Create a servo object
Servo myservo; 
 
void setup() 
{ 
  // Setup Serial Monitor
  Serial.begin(9600);
  
  // Attach myservo object to control pin
  myservo.attach(servoPin); 
  
  // Home the servo motor
  myservo.write(0);
  
  // Step through servo positions
  // Increment by 5 degrees
  for (int servoPos = 0; servoPos <=360; servoPos = servoPos + 1){
    
    // Position servo motor
    myservo.write(servoPos);
    // Allow time to get there
    delay(50);
    
    // Read value from feedback signal
    feedbackValue = analogRead(feedbackPin);
    
    // Write value to serial monitor
    Serial.print("Position = ");
    Serial.print(servoPos);
    Serial.print("\t");
    Serial.println(feedbackValue);
  
  }
 
  // Move back to home position
  myservo.write(0);
  
  // Print to serial monitor when done
  Serial.println("Finished!");
 
}  
 
void loop()
{
  // Nothing in loop
}
