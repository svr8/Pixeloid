#include "Adafruit_VL53L0X.h"
//#include <SPI.h>
//#include <SD.h>
#define index_stepPin 0
#define platform_stepPin 3
#define lidar_stepPin 9
#define platform_stepLimit 201
#define lidar_stepLimit 1.8
#define platform_rotationDelay 150
#define lidar_rotationDelay 150

Adafruit_VL53L0X lox = Adafruit_VL53L0X();
//File file;
bool scan_complete = false;
float z = 0;

void setup() {
  // Same baudrate for SD Card and LIDAR VL53LOX
  Serial.begin(115200);

  // INITIALISING VL53LOX
  // wait until serial port opens for native USB devices
  while (! Serial) {
    delay(1);
  }
  
  if (!lox.begin()) {
    Serial.println(F("Failed to boot VL53L0X"));
    while(1);
  }
  // -------------------------------------

  // INITIALISING SD CARD
//  if (!SD.begin(4)) {
//    Serial.println("Failed to initialize SD Card");
//    while (1);
//  }
//
//  file = SD.open("data.txt", FILE_WRITE);
//  if (file) {}
//  else {
//      Serial.println("Error opening test.txt");
//  }
  // -------------------------------------
  
  // INITIALSING STEPPER MOTORS
  pinMode(5, OUTPUT); // ENABLE
  pinMode(2, OUTPUT); // DIR
  digitalWrite(5, 0);
  digitalWrite(2, 0);
  pinMode(platform_stepPin, OUTPUT);
  
  pinMode(10, OUTPUT); // ENABLE
  pinMode(8, OUTPUT); // DIR
  pinMode(lidar_stepPin, OUTPUT); // STEP
  digitalWrite(10, 0);
  digitalWrite(8, 0);
  
  // INTIALISING Z-AXIS
  z = 0;
}


void loop() {
  if(scan_complete) return;

  if(z < lidar_stepLimit) {
      int i = 0;
      VL53L0X_RangingMeasurementData_t measure;
      int mm;
      while(i < platform_stepLimit) {
        lox.rangingTest(&measure, false); // pass in 'true' to get debug data printout!
        if (measure.RangeStatus != 4) {  // phase failures have incorrect data
            if(measure.RangeMilliMeter <= 240) {
              mm = measure.RangeMilliMeter - 127;
            }
            else {
              mm = -1;
            }
          } else {
          mm = -1;
        }
        
        // PLATFORM STEP
        digitalWrite(platform_stepPin, HIGH);
        delayMicroseconds(3200);
        digitalWrite(platform_stepPin, LOW);
        delayMicroseconds(3200);
        delay(platform_rotationDelay);
        
        if(mm != -1) {
        Serial.print(String(cos(i*1.791f/180.0f)*mm));
        Serial.print(" ");
        Serial.print(String(sin(i*1.791f/180.0f)*mm));
        Serial.print(" ");
        Serial.println(z);
        }
        i++;
      }
      z+=0.6;
      // LIDAR STEP
      for(int x = 0; x < 24; x++) {
      digitalWrite(lidar_stepPin, HIGH);
      delayMicroseconds(1800);
      digitalWrite(lidar_stepPin, LOW);
      delayMicroseconds(1200);
      delay(lidar_rotationDelay);
      }
      
      
  } else {
      scan_complete = true;
      Serial.println("Scan complete");
  }
}
