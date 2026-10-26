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
Monitoring the *inside* of the bin is vital for municipal route optimization and fair acoustic deterrence.

* **Stationary Collar Angled Sensor Architecture**:
  Rather than mounting the ultrasonic transducer underneath the swinging lid (which causes cable snags, flexing, and severing during municipal emptying), the waterproof JSN-SR04T transducer is mounted to the **stationary upper collar / inner rigid rim**, angled downward at $\sim 25^\circ$ toward the center of the container.
  * **Zero wire movement during municipal emptying**: The sealed 2.5m coaxial cable remains completely static; sanitation workers can slam lids open or hoist inner bins without touching or stressing the wiring.
  * **Full-range capacity tracking (0–100%)**: Rather than a crude binary on/off switch, the sensor continuously measures depth along the hypotenuse, which firmware converts to vertical fill percentage ($h = d \cdot \cos(25^\circ)$) for fleet route forecasting.
  * **Direct line-of-sight to the central trash cone**: Accounts for the natural pyramid/cone heap that forms directly beneath the drop opening.
* **Interactive Deterrent**: 
  * If the *external* Daneben sensor detects someone leaving trash outside, it quickly queries the *internal* collar sensor.
  * If the internal sensor confirms capacity is available (<90% full), the external unit triggers the weatherproof speaker: *"Bitte den Müll in die Tonne werfen. Es ist noch Platz!"* (Please put the trash inside, there is still room).
  * If the bin is $\ge 90\%$ full, the audio reprimand is suppressed (fairness policy), and an immediate overflow alert is dispatched to the city.
* **Dual-Button NVS Calibration Subsystem**:
  To support any container size (120L, 240L, 360L, or underground bins up to 4m) and any pavement curb height without custom code:
  * Two tactile buttons are located on the internal PCB: `SW_CAL_IN` (inside depth) and `SW_CAL_OUT` (pavement distance).
  * During initial setup with the casing open, pressing either button triggers a 15-cycle ultrasonic test burst with outlier rejection.
  * Dedicated status LEDs (`LED_CAL_IN` Amber, `LED_CAL_OUT` Blue) blink rapidly during sampling and glow solid for 2 seconds upon successful NVS flash storage.
  * Once calibrated, the technician fastens the lid screws, preserving 100% IP67 waterproofing with zero external button holes.
* **Data Tracking**: The system logs this interaction. If the trash remains outside 5 minutes later, it logs an "Ignored Warning" event with a timestamp.

## 3. Reporting to the Trash Company (Cloud Expansion)
* **The Dashboard**: The devices send small MQTT or LoRaWAN payloads to a central server.
* **Live Fleet Monitoring**: The trash company has a map view. Bins turn RED if trash is accumulating outside. They can dynamically reroute drivers to clean up hotspots before residents complain.
* **Data Analytics**: The city can see "Bin #402 gets illegal dumping every Thursday at 9 PM and warnings are ignored 80% of the time." This allows them to dispatch a fine enforcement officer exactly when needed.
