# AI, Picture Analysis, and System Expansions

## 1. Picture Analysis: Background Subtraction vs. Lightweight AI

### Background Subtraction / Pixel Diff
* **How it works**: Takes a photo of the empty area. Every new photo is compared pixel-by-pixel. If a large block of pixels changes, it flags an anomaly.
* **Pros**: Extremely low processing power, fast.
* **Cons (Severe)**: Terrible outdoors. A cloud passing by (shadows), a puddle reflecting light, snow, or leaves blowing into the frame will trigger constant false alarms.

### Lightweight Edge AI (User Preferred & Recommended)
* **How it works**: Uses a trained neural network (e.g., MobileNetV2 or YOLO-nano via Edge Impulse) running locally on the ESP32-S3 to recognize specific shapes (trash bags, cardboard boxes).
* **Pros**: Highly accurate. It knows what a garbage bag looks like regardless of lighting, shadows, or weather. It can differentiate between a trash bag and a stray dog sleeping next to the bin.
* **Cons**: Requires more RAM and processing time (taking ~1-2 seconds to process an image instead of milliseconds), consuming slightly more battery.
* **Conclusion**: Lightweight AI is definitely the right choice. The battery usage is mitigated by the solar panel and the 2-stage wake-up filter.

## 2. System Expansion: Internal Fullness Sensor & Acoustic Deterrent
You proposed an excellent addition: monitoring the *inside* of the bin.

* **Internal Sensor Unit**: A secondary module placed under the lid of the bin looking down. It uses an ultrasonic sensor (or ToF) to measure the distance to the trash. If the distance is small, the bin is 100% full.
* **Interactive Deterrent**: 
  * If the *external* Daneben sensor detects someone leaving trash outside, it quickly queries the *internal* sensor.
  * If the internal sensor says "I have space!", the external unit triggers a small weatherproof speaker: *"Bitte den Müll in die Tonne werfen. Es ist noch Platz!"* (Please put the trash inside, there is still room).
* **Data Tracking**: The system logs this interaction. If the trash remains outside 5 minutes later, it logs an "Ignored Warning" event with a timestamp.

## 3. Reporting to the Trash Company (Cloud Expansion)
* **The Dashboard**: The devices send small MQTT or LoRaWAN payloads to a central server.
* **Live Fleet Monitoring**: The trash company has a map view. Bins turn RED if trash is accumulating outside. They can dynamically reroute drivers to clean up hotspots before residents complain.
* **Data Analytics**: The city can see "Bin #402 gets illegal dumping every Thursday at 9 PM and warnings are ignored 80% of the time." This allows them to dispatch a fine enforcement officer exactly when needed.
