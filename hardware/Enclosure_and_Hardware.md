# Hardware, Enclosure, and Power Architecture

## 1. Weather Conditions & IP Rating
To survive outdoor environments (rain, snow, high pressure washing), the device must achieve an **IP67 rating** (dust-tight, protected against temporary immersion).
* **Build Structure / Box Shape**: 
  * **Sloped Roof**: The top of the enclosure must have a 15 to 30-degree slope. This prevents water pooling, sheds snow, and naturally angles the flush-mounted solar panel toward the sun.
  * **Drip Edge**: The top shell should overhang the bottom shell slightly (like a roof eaves) so water drips off rather than running into the seams.
  * **Seals**: The main body halves must be sealed using a custom continuous silicone O-ring compressed by stainless steel screws.
  * **Camera/Sensor Window**: A recessed scratch-resistant acrylic window facing downwards at a 45-degree angle. Recessing it acts as a lens hood against rain drops and direct sun glare.

## 2. Power System: Solar & Batteries
* **Battery Type**: **LiFePO4 (Lithium Iron Phosphate) 18650 or 26650 cells** are strongly recommended over standard Li-ion. They handle freezing temperatures and high summer heat much better, and won't catch fire if physically damaged by a garbage truck.
* **Solar Integration**: A custom-cut 5V, 1W to 2W monocrystalline solar panel embedded flush on the sloped roof. 
* **Charge Controller**: CN3791 (or similar MPPT chip) designed to extract maximum power from small solar panels to trickle-charge the batteries.

## 3. Easy Battery Change Mechanism
* **The Cartridge System**: Opening an IP67 enclosure in the field often ruins the waterproof seal because dirt gets on the O-ring.
* **Solution**: A bottom-facing, completely isolated waterproof battery tube (similar to a tactical flashlight). The maintenance worker simply unscrews a threaded cap (which has its own double-O-ring), slides out the old 18650 battery cartridge, and slides in a fresh one. The main electronic chamber is never exposed to the outside air.

## 4. Custom PCB Structure
* **Necessity**: Yes, a custom PCB is mandatory to fit the specific enclosure shape and eliminate messy wiring.
* **Shape**: An "Inverted T" or "L" shape.
  * *Top section*: Power management (Solar input, MPPT, Battery contacts).
  * *Middle section*: The MCU (ESP32-S3 module) and communication antenna (placed near the plastic wall for best RF signal).
  * *Bottom section*: Camera module and ToF/Ultrasonic sensors angled downwards. 
* **Protection**: The entire assembled PCB should be covered in an acrylic conformal coating (except for the camera lens and sensor ports) to prevent corrosion from any internal condensation.

## 5. Internal Sensor Mounting Architecture (Stationary Collar Angled Mount)
* **The Problem with Lid Mounting**: Traditional smart waste sensors mount underneath the moving lid. In real-world municipal operations, sanitation workers violently slam lids open, flip them $270^\circ$, or hoist internal liners. Any cable bridging the hinge between a stationary bin body and a swinging lid will quickly pinch, stretch, or sever.
* **The Solution: Angled Collar Mount**: The internal waterproof ultrasonic transducer (JSN-SR04T) is mounted on the **stationary upper collar / inner rigid rim** of the container, tilted downward at a $\sim 20^\circ\text{–}25^\circ$ angle toward the bottom-center of the trash cavity.
* **Three Decisive Advantages**:
  1. **Zero Wire Movement During Municipal Emptying**: Because the sensor is fixed to the rigid outer chassis/hood, the 2.5m sealed coaxial cable remains 100% static. Workers can open front doors or swing lids without flexing or pulling the wiring.
  2. **Full-Range Capacity Tracking (0–100%)**: Unlike a horizontal cross-beam which acts only as a binary on/off switch, the angled downward sensor measures continuous depth along the hypotenuse, which the firmware converts via trigonometry ($h = d \cdot \cos(\theta)$) to continuous percentage fill for municipal fleet route planning.
  3. **Direct Line-of-Sight to the Central Trash Cone**: Trash naturally heaps into a pyramid or cone in the center beneath the deposit aperture. Tilting toward the center measures the critical peak of the pile rather than false voids along the edges.
* **Dead-Zone Prevention**: The angled hypotenuse path provides extra physical distance compared to a straight vertical drop, preventing the trash pile from prematurely entering the sensor's $20\text{ cm}$ ultrasonic blind zone.

## 6. Internal Board-Level Calibration Buttons & Status LEDs
* **Zero Enclosure Penetration (Preserving IP67 Waterproofing)**:
  Rather than piercing the outer enclosure with external button plungers (which introduces potential leak paths and vandalism risks), the calibration controls are mounted **directly on the carrier PCB inside the main enclosure**:
  * **`SW_CAL_IN` (Inside Bin Depth Button)** paired with **`LED_CAL_IN` (Amber Status LED)**.
  * **`SW_CAL_OUT` (Outside Pavement Distance Button)** paired with **`LED_CAL_OUT` (Blue Status LED)**.
* **One-Time Field Installation & Calibration Procedure**:
  1. The municipal technician unfastens the stainless enclosure screws and lifts the cover (revealing the PCB and rubber perimeter O-ring gasket).
  2. **Calibrate Bin Depth (`SW_CAL_IN`)**: On the empty container, the technician presses `SW_CAL_IN`. The inside sensor runs 15 test cycles while the Amber LED blinks rapidly. The firmware filters outliers, applies the $25^\circ$ trigonometric slant correction ($H = D \cdot \cos(25^\circ)$), and saves the baseline into non-volatile storage (`Preferences` / NVS flash). The Amber LED turns solid for 2 seconds upon success.
  3. **Calibrate Pavement Baseline (`SW_CAL_OUT`)**: With the ground clear, the technician presses `SW_CAL_OUT`. The outside sensor runs 15 test cycles while the Blue LED blinks rapidly. The baseline floor distance is saved to NVS. The Blue LED turns solid for 2 seconds upon success.
  4. **Reseal**: The technician places the cover back on and fastens the screws, compressing the silicone O-ring gasket. The enclosure is now completely sealed against dust and water (IP67) with zero external button holes.


