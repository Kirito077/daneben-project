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
