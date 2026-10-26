#include <Arduino.h>
#include <Wire.h>
#include <WiFi.h>
#include <PubSubClient.h>

#include "calibration.h"

// Pseudocode for Edge Impulse Inferencing
// #include <Daneben_Lightweight_AI_inferencing.h> 

#define CAMERA_POWER_PIN 12
const int DEBOUNCE_DELAY_MS = 8000; // 8 seconds wait to ignore passersby

WiFiClient espClient;
PubSubClient client(espClient);
SensorCalibrator calibrator;

void setup() {
  Serial.begin(115200);
  pinMode(CAMERA_POWER_PIN, OUTPUT);
  digitalWrite(CAMERA_POWER_PIN, LOW); // Camera OFF to save battery
  
  // Initialize Dual Sensor Calibration Subsystem (loads NVS baselines)
  calibrator.begin();
  
  // Connect WiFi / MQTT (Implement connection logic here)
}

float readDistance() {
  // Uses outside sensor pins defined in calibration.h
  digitalWrite(PIN_TRIG_OUT, LOW);
  delayMicroseconds(2);
  digitalWrite(PIN_TRIG_OUT, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_TRIG_OUT, LOW);
  long duration = pulseIn(PIN_ECHO_OUT, HIGH, 35000);
  if (duration == 0) return -1.0f;
  return (float)duration * 0.0343f / 2.0f;
}

void loop() {
  // 1. Service installation calibration buttons (active when enclosure lid is opened)
  calibrator.checkButtons();

  // 2. Poll external pavement distance
  float distance = readDistance();
  
  // Check if an object was placed relative to the calibrated pavement baseline
  if (calibrator.isObjectOnPavement(distance)) {
    Serial.printf("[Pavement Monitor] Object detected (Dist: %.1f cm | Floor Baseline: %.1f cm). Debouncing...\n", 
                  distance, calibrator.getFloorDistance());
    delay(DEBOUNCE_DELAY_MS);
    
    // Check again after 8s debounce
    float distance2 = readDistance();
    if (calibrator.isObjectOnPavement(distance2)) {
      Serial.println("[Pavement Monitor] Object persisted! Waking camera and AI...");
      
      // Power up Camera
      digitalWrite(CAMERA_POWER_PIN, HIGH);
      delay(500); // Wait for camera boot
      
      // Capture Image & Run Edge Impulse Model (Pseudocode)
      // capture_image();
      // int ai_result = run_ai_inference();
      int ai_result = 1; // 1 = Trash Bag detected (Simulated)
      
      if (ai_result == 1) {
        Serial.println("AI Confirms: Waste detected outside bin.");
        
        // 3. Query Internal Collar Sensor using Calibrated Baseline
        // float internalDist = readInternalDistance();
        // int fillPercent = calibrator.getBinFillPercentage(internalDist);
        // bool isBinFull = (fillPercent >= 90);
        
        // 4. Send MQTT Payload to Trash Company with combined pavement & capacity telematics
        client.publish("city/bins/daneben/402/status", "ILLEGAL_DUMPING_DETECTED");
      } else {
        Serial.println("AI says it's not trash (e.g., Dog, stroller). Ignoring.");
      }
      
      // Power down camera
      digitalWrite(CAMERA_POWER_PIN, LOW);
      
      // Cooldown delay
      delay(30000); 
    } else {
      Serial.println("[Pavement Monitor] Object left. Transient pedestrian ignored.");
    }
  }
  
  delay(500); // Polling delay
}
