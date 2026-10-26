#include <Arduino.h>
#include <math.h>

// ==============================================================================
// DANEBEN! SMART WASTE IOT - INTERNAL BIN FULLNESS & TELEMATICS MODULE
// ==============================================================================
// ARCHITECTURE NOTE:
// The internal ultrasonic transducer (JSN-SR04T) is mounted on the STATIONARY
// UPPER COLLAR / INNER RIM of the bin, angled downward at ~25 degrees toward the
// bottom-center of the trash cavity.
//
// THREE KEY ENGINEERING ADVANTAGES:
// 1. ZERO WIRE MOVEMENT: Eliminates moving wires across the swinging lid. Cables
//    never flex, snag, or sever when sanitation workers violently flip the lid
//    or hoist inner containers during municipal collection rounds.
// 2. FULL-RANGE CAPACITY TRACKING (0-100%): Provides continuous fill telemetry
//    for municipal fleet route forecasting rather than just an on/off switch.
// 3. DIRECT LINE-OF-SIGHT TO CENTRAL CONE: Directly targets the central pyramid
//    heap where trash naturally accumulates first under the deposit opening.
// ==============================================================================

#define INTERNAL_TRIG_PIN 14
#define INTERNAL_ECHO_PIN 15
#define SPEAKER_PIN 25 // I2S or PWM speaker output

// Physical geometry of standard municipal container (e.g. 120L / 240L wheelie bin)
const float BIN_DEPTH_CM = 100.0;          // Total vertical depth from collar to floor (cm)
const float FULL_THRESHOLD_CM = 20.0;       // Vertical distance threshold considered 100% full (cm)
const float TILT_ANGLE_DEG = 25.0;          // Sensor downward tilt angle from vertical (degrees)
const float TILT_ANGLE_RAD = TILT_ANGLE_DEG * (M_PI / 180.0); // Converted to radians
const float COS_TILT = cos(TILT_ANGLE_RAD); // Pre-computed cosine (~0.9063)

void setup() {
  Serial.begin(115200);
  pinMode(INTERNAL_TRIG_PIN, OUTPUT);
  pinMode(INTERNAL_ECHO_PIN, INPUT);
  pinMode(SPEAKER_PIN, OUTPUT);
  Serial.println("[Internal Sensor] Initialized with Fixed Upper Collar Angled Mount (25 deg tilt)");
}

// Measures raw slant/diagonal distance from upper collar to trash cone
float getRawDiagonalDistance() {
  digitalWrite(INTERNAL_TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(INTERNAL_TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(INTERNAL_TRIG_PIN, LOW);
  
  long duration = pulseIn(INTERNAL_ECHO_PIN, HIGH, 30000); // 30ms timeout (~5m range)
  if (duration == 0) return -1.0; // Echo timeout / out of range
  
  return duration * 0.0343 / 2.0; // Distance in cm
}

// Converts diagonal slant distance to vertical depth and calculates fill percentage (0-100%)
int calculateFillPercentage(float diagonalDistanceCm, float &outVerticalDepthCm) {
  if (diagonalDistanceCm <= 0) return -1;
  
  // Trigonometric conversion: vertical depth = diagonal distance * cos(theta)
  outVerticalDepthCm = diagonalDistanceCm * COS_TILT;
  
  // Constrain within valid physical bounds
  if (outVerticalDepthCm <= FULL_THRESHOLD_CM) {
    return 100; // Bin is completely full (trash heap is at or above full threshold)
  }
  if (outVerticalDepthCm >= BIN_DEPTH_CM) {
    return 0;   // Bin is empty
  }
  
  // Map continuous vertical depth to 0-100% capacity
  // (As depth decreases toward 20cm, fill percentage rises toward 100%)
  float percentage = ((BIN_DEPTH_CM - outVerticalDepthCm) / (BIN_DEPTH_CM - FULL_THRESHOLD_CM)) * 100.0;
  return (int)constrain(percentage, 0.0, 100.0);
}

void playWarningAudio() {
  Serial.println("PLAYING AUDIO: 'Bitte den Müll in die Tonne werfen. Es ist noch Platz!'");
  // Audio playback via MAX98357A I2S amplifier
}

void loop() {
  // In production, this module sleeps and wakes up periodically (every 15-30 min)
  // or on-demand when the external unit detects an object on the pavement.
  
  bool dumpAttemptDetected = true; // Simulated event from external unit
  
  if (dumpAttemptDetected) {
    float diagDistance = getRawDiagonalDistance();
    float verticalDepth = 0.0;
    int fillPercent = calculateFillPercentage(diagDistance, verticalDepth);
    
    Serial.printf("[Telematics] Raw Diagonal: %.1f cm | Vertical Depth: %.1f cm | Fill Level: %d%%\n", 
                  diagDistance, verticalDepth, fillPercent);
    
    if (fillPercent >= 0 && fillPercent < 90) {
      Serial.printf("Bin has available capacity (%d%% full). Prompting citizen...\n", fillPercent);
      playWarningAudio();
      // sendToMainUnit("WARNING_PLAYED", fillPercent);
    } else if (fillPercent >= 90) {
      Serial.printf("Bin is FULL (%d%%). Suppressing warning (fairness) & alerting fleet.\n", fillPercent);
      // sendToMainUnit("BIN_FULL_OVERFLOW", fillPercent);
    } else {
      Serial.println("[Warning] Sensor reading invalid / obscured.");
    }
  }
  
  delay(10000); 
}
