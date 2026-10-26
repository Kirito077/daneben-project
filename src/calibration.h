#ifndef CALIBRATION_H
#define CALIBRATION_H

#include <Arduino.h>
#include <Preferences.h>

// ==============================================================================
// DANEBEN! SMART WASTE IOT - DUAL SENSOR BENCH/FIELD CALIBRATION SYSTEM
// ==============================================================================
// Supports variable container depths (e.g. 1m, 2m, up to 4m underground bins)
// and pavement baseline distances using sizable pushbuttons and multi-cycle averaging.
// ==============================================================================

// Pin Definitions matching Daneben Carrier Board v2.0
#define PIN_TRIG_OUT        1   // GPIO1 / D0 (AJ-SR04M Outside Transducer Trigger)
#define PIN_ECHO_OUT        2   // GPIO2 / D1 (AJ-SR04M Outside Transducer Echo)
#define PIN_TRIG_IN         3   // GPIO3 / D2 (AJ-SR04M Inside Transducer Trigger)
#define PIN_ECHO_IN         4   // GPIO4 / D3 (AJ-SR04M Inside Transducer Echo)

#define PIN_BTN_CAL_OUT     5   // GPIO5 / D4 (Sizable 12x12mm Outside Cal Button)
#define PIN_BTN_CAL_IN      6   // GPIO6 / D5 (Sizable 12x12mm Inside Cal Button)

#define PIN_LED_CAL_OUT     43  // GPIO43 / D6 (Blue Status LED Outside Cal)
#define PIN_LED_CAL_IN      44  // GPIO44 / D7 (Amber Status LED Inside Cal)

// Defaults & Geometry
const float DEFAULT_FLOOR_DISTANCE_CM = 150.0f; // Default pavement distance (cm)
const float DEFAULT_BIN_DEPTH_CM      = 100.0f; // Default vertical bin height (cm)
const float FULL_THRESHOLD_MARGIN_CM  = 20.0f;  // Space from collar considered 100% full (cm)
const int   CALIBRATION_CYCLES        = 15;     // Number of pings averaged for calibration
const float TILT_ANGLE_DEG            = 25.0f;  // Internal sensor downward tilt from vertical
const float COS_TILT                  = 0.9063f;// cos(25 deg) for trigonometric vertical depth conversion

class SensorCalibrator {
private:
  Preferences prefs;
  float floorDistanceCm;
  float binDepthCm;

  float pingSensor(uint8_t trigPin, uint8_t echoPin, unsigned long timeoutUs = 35000) {
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    unsigned long duration = pulseIn(echoPin, HIGH, timeoutUs);
    if (duration == 0) return -1.0f; // Timeout / out of range
    return (float)duration * 0.0343f / 2.0f; // Distance in cm
  }

public:
  SensorCalibrator() : floorDistanceCm(DEFAULT_FLOOR_DISTANCE_CM), binDepthCm(DEFAULT_BIN_DEPTH_CM) {}

  void begin() {
    pinMode(PIN_TRIG_OUT, OUTPUT);
    pinMode(PIN_ECHO_OUT, INPUT);
    pinMode(PIN_TRIG_IN, OUTPUT);
    pinMode(PIN_ECHO_IN, INPUT);

    pinMode(PIN_BTN_CAL_OUT, INPUT_PULLUP);
    pinMode(PIN_BTN_CAL_IN, INPUT_PULLUP);

    pinMode(PIN_LED_CAL_OUT, OUTPUT);
    pinMode(PIN_LED_CAL_IN, OUTPUT);
    digitalWrite(PIN_LED_CAL_OUT, LOW);
    digitalWrite(PIN_LED_CAL_IN, LOW);

    // Load persisted baselines from ESP32 NVS flash
    prefs.begin("daneben_cal", false);
    floorDistanceCm = prefs.getFloat("floor_dist", DEFAULT_FLOOR_DISTANCE_CM);
    binDepthCm      = prefs.getFloat("bin_depth", DEFAULT_BIN_DEPTH_CM);

    Serial.println("==================================================");
    Serial.println("[Calibration System] Initialized.");
    Serial.printf("  Loaded Floor Baseline: %.1f cm\n", floorDistanceCm);
    Serial.printf("  Loaded Bin Depth:      %.1f cm\n", binDepthCm);
    Serial.println("==================================================");
  }

  // Multi-cycle calibration for Outside Sensor (Pavement / Floor)
  float calibrateOutside() {
    Serial.println("[Calibrator] Starting OUTSIDE (Floor / Pavement) Calibration...");
    float sum = 0.0f;
    int validCount = 0;

    for (int i = 0; i < CALIBRATION_CYCLES; i++) {
      // Rapid blinking LED feedback
      digitalWrite(PIN_LED_CAL_OUT, (i % 2 == 0) ? HIGH : LOW);
      delay(80);

      float d = pingSensor(PIN_TRIG_OUT, PIN_ECHO_OUT);
      if (d > 10.0f && d < 600.0f) { // Valid range 10cm - 6m
        sum += d;
        validCount++;
        Serial.printf("  Ping %d/%d: %.1f cm\n", i + 1, CALIBRATION_CYCLES, d);
      } else {
        Serial.printf("  Ping %d/%d: Out of range / rejected\n", i + 1, CALIBRATION_CYCLES);
      }
    }

    if (validCount >= (CALIBRATION_CYCLES / 2)) {
      floorDistanceCm = sum / validCount;
      prefs.putFloat("floor_dist", floorDistanceCm);
      Serial.printf(">>> OUTSIDE CALIBRATION SUCCESS: Baseline Floor = %.1f cm <<<\n", floorDistanceCm);

      // Solid LED for 2 seconds to confirm
      digitalWrite(PIN_LED_CAL_OUT, HIGH);
      delay(2000);
      digitalWrite(PIN_LED_CAL_OUT, LOW);
    } else {
      Serial.println(">>> OUTSIDE CALIBRATION FAILED: Too many invalid readings! <<<");
      // Fast triple blink error
      for (int k = 0; k < 6; k++) {
        digitalWrite(PIN_LED_CAL_OUT, !digitalRead(PIN_LED_CAL_OUT));
        delay(150);
      }
    }
    return floorDistanceCm;
  }

  // Multi-cycle calibration for Inside Sensor (Bin Floor / Container Depth)
  float calibrateInside() {
    Serial.println("[Calibrator] Starting INSIDE (Bin Depth) Calibration on EMPTY bin...");
    float sum = 0.0f;
    int validCount = 0;

    for (int i = 0; i < CALIBRATION_CYCLES; i++) {
      // Rapid blinking LED feedback
      digitalWrite(PIN_LED_CAL_IN, (i % 2 == 0) ? HIGH : LOW);
      delay(80);

      float d = pingSensor(PIN_TRIG_IN, PIN_ECHO_IN);
      if (d > 10.0f && d < 600.0f) {
        sum += d;
        validCount++;
        Serial.printf("  Ping %d/%d: %.1f cm\n", i + 1, CALIBRATION_CYCLES, d);
      } else {
        Serial.printf("  Ping %d/%d: Out of range / rejected\n", i + 1, CALIBRATION_CYCLES);
      }
    }

    if (validCount >= (CALIBRATION_CYCLES / 2)) {
      float rawDiagDepth = sum / validCount;
      binDepthCm = rawDiagDepth * COS_TILT; // Apply 25-degree tilt trigonometric conversion
      prefs.putFloat("bin_depth", binDepthCm);
      Serial.printf(">>> INSIDE CALIBRATION SUCCESS: Raw Slant = %.1f cm | Calibrated Vertical Depth = %.1f cm <<<\n", 
                    rawDiagDepth, binDepthCm);

      // Solid LED for 2 seconds to confirm
      digitalWrite(PIN_LED_CAL_IN, HIGH);
      delay(2000);
      digitalWrite(PIN_LED_CAL_IN, LOW);
    } else {
      Serial.println(">>> INSIDE CALIBRATION FAILED: Too many invalid readings! <<<");
      for (int k = 0; k < 6; k++) {
        digitalWrite(PIN_LED_CAL_IN, !digitalRead(PIN_LED_CAL_IN));
        delay(150);
      }
    }
    return binDepthCm;
  }

  // Check buttons in non-blocking fashion
  void checkButtons() {
    // Check Outside Button (Active LOW)
    if (digitalRead(PIN_BTN_CAL_OUT) == LOW) {
      delay(50); // Debounce
      if (digitalRead(PIN_BTN_CAL_OUT) == LOW) {
        calibrateOutside();
        while (digitalRead(PIN_BTN_CAL_OUT) == LOW) delay(10); // Wait for release
      }
    }

    // Check Inside Button (Active LOW)
    if (digitalRead(PIN_BTN_CAL_IN) == LOW) {
      delay(50); // Debounce
      if (digitalRead(PIN_BTN_CAL_IN) == LOW) {
        calibrateInside();
        while (digitalRead(PIN_BTN_CAL_IN) == LOW) delay(10); // Wait for release
      }
    }
  }

  // Get current pavement presence detection
  bool isObjectOnPavement(float currentDistCm) {
    if (currentDistCm <= 0) return false;
    // An object is present if distance is significantly closer than the floor baseline
    return (currentDistCm < (floorDistanceCm - 25.0f));
  }

  // Get current bin fill percentage (0 - 100%) adapted to calibrated bin depth
  int getBinFillPercentage(float currentDistCm) {
    if (currentDistCm <= 0) return -1;
    float verticalDepth = currentDistCm * COS_TILT;
    if (verticalDepth <= FULL_THRESHOLD_MARGIN_CM) return 100;
    if (verticalDepth >= binDepthCm) return 0;

    float percent = ((binDepthCm - verticalDepth) / (binDepthCm - FULL_THRESHOLD_MARGIN_CM)) * 100.0f;
    return (int)constrain(percent, 0.0f, 100.0f);
  }

  float getFloorDistance() const { return floorDistanceCm; }
  float getBinDepth() const { return binDepthCm; }
};

#endif // CALIBRATION_H
