#include <Arduino.h>

#define INTERNAL_TRIG_PIN 14
#define INTERNAL_ECHO_PIN 15
#define SPEAKER_PIN 25 // I2S or PWM speaker output

const int BIN_DEPTH_CM = 120;
const int FULL_THRESHOLD_CM = 20; // If distance to trash is < 20cm, bin is full

void setup() {
  Serial.begin(115200);
  pinMode(INTERNAL_TRIG_PIN, OUTPUT);
  pinMode(INTERNAL_ECHO_PIN, INPUT);
  pinMode(SPEAKER_PIN, OUTPUT);
}

long getFillLevel() {
  digitalWrite(INTERNAL_TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(INTERNAL_TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(INTERNAL_TRIG_PIN, LOW);
  long duration = pulseIn(INTERNAL_ECHO_PIN, HIGH);
  return duration * 0.034 / 2;
}

void playWarningAudio() {
  // Pseudocode for playing WAV file via I2S / DAC
  Serial.println("PLAYING AUDIO: 'Bitte den Müll in die Tonne werfen. Es ist noch Platz!'");
  // playWav("warning.wav");
}

void loop() {
  // In production, this module would sleep and only wake up when 
  // signaled by the main external "Daneben" unit.
  
  // Simulated request from main unit:
  bool dumpAttemptDetected = true; 
  
  if (dumpAttemptDetected) {
    long distanceToTrash = getFillLevel();
    
    if (distanceToTrash > FULL_THRESHOLD_CM) {
      Serial.println("Bin is NOT full. Space is available.");
      playWarningAudio();
      
      // Log event to track if user ignores this warning
      // sendToMainUnit("WARNING_PLAYED");
    } else {
      Serial.println("Bin IS full. Cannot play warning. User has no choice.");
      // sendToMainUnit("BIN_FULL_NO_WARNING");
    }
  }
  
  delay(5000); 
}
