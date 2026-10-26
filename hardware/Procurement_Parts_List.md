# "Daneben!" Procurement & Purchasing Guide
**Project:** Daneben! Smart Waste Bin Detection System  
**Academic Context:** HSNR Studium · 5. Semester · Mikro-controller  
**Target Delivery Region:** Germany / EU (Fast shipping prioritized: Amazon.de Prime, BerryBase.de, Reichelt.de, AZ-Delivery)

---

## 1. Purchasing Strategy & Vendor Summary
To build the functional prototype without waiting weeks for overseas shipping, all parts listed below are available from domestic German / EU warehouses with typical delivery times of **1 to 3 business days**.

* **Amazon.de (Prime):** Fastest turnaround (1 business day) with free shipping for Prime members; ideal for getting parts next day.
* **BerryBase.de (Berlin, Germany):** Official distributor for Seeed Studio, Raspberry Pi, and maker modules. Flat €4.90 DHL shipping (free above €79.00) with 1–2 day delivery.
* **Reichelt.de & AZ-Delivery.de:** Fast German stockists for electronic components, connectors, and passives.

---

## 2. Complete Component-by-Component Purchasing Matrix

### 2.1 Core Compute & Vision: Seeed Studio XIAO ESP32-S3 Sense
* **Role:** Central processor running the 2-stage wake-up state machine, Wi-Fi/BLE communication, and on-device Edge Impulse ML vision model (OV2640 camera + 8MB PSRAM).
* **Physical Dimensions:** **21.0 mm × 17.5 mm × 15.0 mm**, Weight: ~5 g, Camera flex length: ~15 mm.

| Store / Provider | Exact Model / Listing | Approx. Price | Shipping Cost (DE) | Total Est. | Delivery Speed | Direct Link |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **BerryBase.de** *(Best Price)* | Seeed Studio XIAO ESP32S3 Sense (102010549) | **€14.90** | €4.90 (DHL) | **€19.80** | 1–2 Days | [BerryBase Listing](https://www.berrybase.de/seeed-studio-xiao-esp32s3-sense) |
| **Amazon.de** *(Fastest Delivery)* | Seeed Studio XIAO ESP32S3 Sense mit Kamera | **€17.99** | **€0.00** (Prime) | **€17.99** | Next Day | [Amazon.de Search](https://www.amazon.de/s?k=Seeed+Studio+XIAO+ESP32S3+Sense) |
| **Reichelt.de** | Seeed Studio XIAO ESP32S3 Sense Modul | **€15.95** | €5.95 (DHL) | **€21.90** | 1–2 Days | [Reichelt Listing](https://www.reichelt.de/seeed-xiao-esp32s3-sense-seeed-102010549-p348981.html) |

---

### 2.2 Distance Sensors: JSN-SR04T 2.0 / 3.0 Waterproof Ultrasonic Sensor (2 Units Needed)
* **Role:**
  * *Unit 1 (External):* Detects presence of deposited objects beside the container (<1.5 m) to trigger the debounce timer.
  * *Unit 2 (Internal):* Mounted on the stationary upper collar / inner rim angled downward (~25°) toward the central trash cone (eliminates moving wires across swinging lids, prevents snagging during municipal emptying, and delivers continuous 0–100% capacity tracking).
* **Physical Dimensions:** Transducer diameter: **Ø 22.0 mm** (flange Ø 25.0 mm, mounting cutout Ø 20.0 mm), Transducer depth: **18.5 mm**, Sealed cable: **2.0 m – 2.5 m**, Driver PCB: **41.5 mm × 28.5 mm × 16.0 mm**.

| Store / Provider | Exact Model / Listing | Approx. Price (1x / 2x) | Shipping Cost (DE) | Total Est. (2 Units) | Delivery Speed | Direct Link |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Amazon.de** *(Best for 2-Pack)* | JSN-SR04T 2.0 Wasserdichter Ultraschallsensor (2er Pack) | **€16.99** (for 2) | **€0.00** (Prime) | **€16.99** | Next Day | [Amazon.de Search](https://www.amazon.de/s?k=JSN-SR04T+wasserdicht+ultraschallsensor) |
| **BerryBase.de** | Elecrow JSN-SR04T-2.0 Wasserdichter Sensor | **€9.90** (each) | €4.90 (DHL) | **€24.70** | 1–2 Days | [BerryBase Listing](https://www.berrybase.de/elecrow-jsn-sr04t-2.0-wasserdichter-ultraschall-entfernungsmesser) |
| **Eckstein Komponente** | JSN-SR04T Waterproof Distance Sensor | **€8.95** (each) | €4.50 (DHL) | **€22.40** | 1–2 Days | [Eckstein Listing](https://eckstein-shop.de/JSN-SR04T-Wasserdichter-Ultraschall-Sensor-fuer-Arduino-Raspberry-Pi) |

---

### 2.3 Audio Amplifier: MAX98357A I2S Mono Class-D DAC/Amp Module
* **Role:** Direct digital audio amplifier driving the external warning speaker over 3 I2S pins (`BCLK`, `LRC`, `DIN`).
* **Physical Dimensions:** **19.0 mm × 17.5 mm × 3.2 mm**, Header pitch: 2.54 mm.

| Store / Provider | Exact Model / Listing | Approx. Price | Shipping Cost (DE) | Total Est. | Delivery Speed | Direct Link |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **AZ-Delivery.de** *(Direct)* | MAX98357A I2S 3W Class D Audio Verstärker Modul | **€4.49** | €2.90 | **€7.39** | 1–2 Days | [AZ-Delivery Listing](https://www.az-delivery.de/products/max98357a-i2s-verstaerker-modul) |
| **Amazon.de** *(AZ-Delivery Prime)* | AZ-Delivery MAX98357A I2S Verstärker Breakout | **€6.99** | **€0.00** (Prime) | **€6.99** | Next Day | [Amazon.de Search](https://www.amazon.de/s?k=MAX98357A+I2S+Verst%C3%A4rker) |
| **BerryBase.de** | Adafruit / SparkFun MAX98357A I2S 3.2W Breakout | **€6.90** | €4.90 (DHL) | **€11.80** | 1–2 Days | [BerryBase Listing](https://www.berrybase.de/adafruit-i2s-3w-class-d-verstaerker-breakout-max98357a) |

---

### 2.4 Outdoor Speaker: 4Ω / 8Ω 2W–3W Waterproof Mini Speaker
* **Role:** Broadcasts the deterrent announcement (*"Bitte den Müll in die Tonne werfen..."*) through the membrane-sealed audio vents.
* **Physical Dimensions:** **Ø 30.0 mm to Ø 40.0 mm**, Thickness: **5.0 mm – 7.5 mm**, 8Ω or 4Ω, 2W–3W.

| Store / Provider | Exact Model / Listing | Approx. Price | Shipping Cost (DE) | Total Est. | Delivery Speed | Direct Link |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **BerryBase.de** *(Best Price)* | Miniatur Lautsprecher 8 Ohm, 2W, Ø 40mm | **€2.80** | €4.90 (DHL) | **€7.70** | 1–2 Days | [BerryBase Listing](https://www.berrybase.de/miniatur-lautsprecher-8-ohm-2w) |
| **Amazon.de** *(Prime)* | Mini Lautsprecher 8 Ohm 2W (2er Pack) | **€6.99** (for 2) | **€0.00** (Prime) | **€6.99** | Next Day | [Amazon.de Search](https://www.amazon.de/s?k=mini+lautsprecher+8+ohm+2w+40mm) |
| **Reichelt.de** | Visaton K 36 WP - 8 Ohm Kleinlautsprecher IP65 | **€4.20** | €5.95 (DHL) | **€10.15** | 1–2 Days | [Reichelt Listing](https://www.reichelt.de/miniatur-lautsprecher-c5806.html) |

---

### 2.5 Solar Panel: 5V–6V 1.5W–2W Monocrystalline Panel
* **Role:** Solar energy harvesting flush-mounted on the 20° sloped enclosure roof.
* **Physical Dimensions:** Surface footprint: **100.0 mm × 60.0 mm to 110.0 mm × 69.0 mm** (exact fit for `daneben_enclosure.scad`), Thickness: **2.5 mm – 3.0 mm**, Output: 5.0V–6.0V, 250mA–330mA.

| Store / Provider | Exact Model / Listing | Approx. Price | Shipping Cost (DE) | Total Est. | Delivery Speed | Direct Link |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Amazon.de** *(Prime)* | 5V / 6V 1.5W–2W Mini Solarpanel 100x60mm / 110x69mm | **€7.49** | **€0.00** (Prime) | **€7.49** | Next Day | [Amazon.de Search](https://www.amazon.de/s?k=mini+solarpanel+5V+6V+1.5W+100x60) |
| **BerryBase.de** | Monokristallines Solarpanel 6V 1.5W | **€6.20** | €4.90 (DHL) | **€11.10** | 1–2 Days | [BerryBase Listing](https://www.berrybase.de/solarpanel-6v) |
| **Eckstein Komponente** | Miniatur Solarpanel 6V 250mA (110x69mm) | **€6.50** | €4.50 (DHL) | **€11.00** | 1–2 Days | [Eckstein Listing](https://eckstein-shop.de/Solarzellen-Module) |

---

### 2.6 Solar MPPT Charger: CN3791 (6V Solar / 3.7V Li-Ion Battery)
* **Role:** Maximum Power Point Tracking (MPPT) solar battery management controller.
* **Physical Dimensions:** **45.0 mm × 20.0 mm × 9.5 mm**, JST-PH 2.0mm connectors.

| Store / Provider | Exact Model / Listing | Approx. Price | Shipping Cost (DE) | Total Est. | Delivery Speed | Direct Link |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **BerryBase.de** *(Soldered Brand)* | Soldered MPPT Li-Ion CN3791 Solar Ladecontroller 6V | **€6.90** | €4.90 (DHL) | **€11.80** | 1–2 Days | [BerryBase Listing](https://www.berrybase.de/soldered-mppt-li-ion-cn3791-ladeboard) |
| **Amazon.de** *(Prime)* | CN3791 MPPT Solar Charge Controller Modul 6V | **€7.99** | **€0.00** (Prime) | **€7.99** | Next Day | [Amazon.de Search](https://www.amazon.de/s?k=CN3791+6V+Solar+Laderegler) |
| **Eckstein Komponente** | CN3791 6V Solar Li-Ion Charger Board | **€5.80** | €4.50 (DHL) | **€10.30** | 1–2 Days | [Eckstein Listing](https://eckstein-shop.de/Solar-Lademodule) |

---

### 2.7 Battery: 18650 Protected Li-Ion Cell (3.7V, 3400–3500 mAh)
* **Role:** High-capacity power storage with built-in safety circuit (protection against overcharge, overdischarge, and short circuit).
* **Physical Dimensions:** Diameter: **Ø 18.5 mm**, Length: **68.5 mm – 69.0 mm** (button top with protection PCB), 3.7V nominal, 3400–3500 mAh (e.g., Panasonic NCR18650B or Samsung 35E).

| Store / Provider | Exact Model / Listing | Approx. Price | Shipping Cost (DE) | Total Est. | Delivery Speed | Direct Link |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Akkuteile.de** *(German Battery Specialist)* | Panasonic NCR18650B geschützt (3400mAh, Button Top) | **€7.95** | €4.50 (DHL) | **€12.45** | 1–2 Days | [Akkuteile Listing](https://www.akkuteile.de/lithium-ionen-akkus/18650) |
| **Amazon.de** *(Prime)* | 18650 Li-Ion Akku 3.7V 3400mAh geschützt | **€9.99** | **€0.00** (Prime) | **€9.99** | Next Day | [Amazon.de Search](https://www.amazon.de/s?k=18650+akku+gesch%C3%BCtzt+3.7v+3400mah) |
| **Reichelt.de** | Enerpower 18650 Li-Ion Zelle 3400mAh geschützt | **€9.50** | €5.95 (DHL) | **€15.45** | 1–2 Days | [Reichelt Listing](https://www.reichelt.de/industrie-akkuzellen-lithium-c5705.html?q=18650+gesch%C3%BCtzt) |

---

### 2.8 18650 Single-Cell Battery Holder with Wire Leads
* **Role:** Secure contact inside the enclosure's tubular cartridge chamber.
* **Physical Dimensions:** **77.0 mm × 21.0 mm × 21.5 mm**.

| Store / Provider | Exact Model / Listing | Approx. Price | Shipping Cost (DE) | Total Est. | Delivery Speed | Direct Link |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **BerryBase.de** *(Best Price)* | Batteriehalter für 1x 18650 mit offenen Litzen | **€1.30** | €4.90 (DHL) | **€6.20** | 1–2 Days | [BerryBase Listing](https://www.berrybase.de/batteriehalter-fuer-1x-18650-mit-offenen-kabelenden) |
| **Amazon.de** *(Prime 2-Pack)* | 18650 Batteriehalter 1-Fach (2er Set) | **€4.49** (for 2) | **€0.00** (Prime) | **€4.49** | Next Day | [Amazon.de Search](https://www.amazon.de/s?k=18650+batteriehalter+1+fach) |
| **Reichelt.de** | Keystone 1042 1x 18650 SMD/THT Halter | **€2.10** | €5.95 (DHL) | **€8.05** | 1–2 Days | [Reichelt Listing](https://www.reichelt.de/batteriehalter-fuer-18650-keystone-1042-p154332.html) |

---

### 2.9 Weatherproofing & Enclosure Hardware

| Component | Exact Specs & Dimensions | Store | Approx. Price | Shipping | Link |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **Camera Window** | Borosilicate Optical Disc: **Ø 20.0 mm × 1.5–2.0 mm** | Amazon.de | **€4.99** (2er Pack) | Prime Free | [Amazon.de Search](https://www.amazon.de/s?k=optisches+glas+rund+20mm) |
| **Speaker Vent Membrane** | Hydrophobic ePTFE Vent Stickers: **Ø 12.0 mm – 16.0 mm** | Amazon.de | **€5.99** (10er Bogen) | Prime Free | [Amazon.de Search](https://www.amazon.de/s?k=ePTFE+akustik+membran+wasserdicht) |
| **M4 Screws & Inserts** | M4×20mm A2 Stainless Screws + M4 Heat-Set Brass Inserts | BerryBase | **€5.40** (Set) | €4.90 | [BerryBase Listing](https://www.berrybase.de/gewindeeinsaetze-m4) |
| **Bin Mounting Clamps** | Stainless Steel Hose Clamps **Ø 90 mm – 160 mm** (2x) | Amazon.de | **€5.99** (4er Pack) | Prime Free | [Amazon.de Search](https://www.amazon.de/s?k=schlauchschellen+edelstahl+100-120mm) |
| **Alternative Bin Ties** | UV-Resistant Industrial Cable Ties **370 mm × 7.6 mm** | Amazon.de | **€6.99** (100er Pack) | Prime Free | [Amazon.de Search](https://www.amazon.de/s?k=kabelbinder+uv+best%C3%A4ndig+370+x+7.6) |

---

### 2.10 KiCad Prototype Circuit Passives
*(Components matching your KiCad schematic: `SW1`, `R1`, `R2`, `D1`, `D2`, `J1`)*

| Component | Specific Value & Footprint | Store | Approx. Pack Price | Link |
| :--- | :--- | :--- | :---: | :--- |
| **Tactile Push Buttons (`SW_CAL_IN`, `SW_CAL_OUT`)** | 2× 6×6mm / 12×12mm Tactile Buttons (Inside & Outside Cal) | BerryBase / Reichelt | **€0.50** (or €2.99 / 10-pack) | [Reichelt Taster](https://www.reichelt.de/kurzhubtaster-6x6mm-hoehe-5-0mm-taster-3301-p109404.html) |
| **Metal Film Resistors (`R1`, `R2`, `R_PULL`)** | 330 Ω (LEDs) & 10 kΩ (Button Pull-ups) | BerryBase | **€0.30** (or €1.99 / 20-pack) | [BerryBase 330 Ohm](https://www.berrybase.de/widerstand-metallschicht-330-ohm-0-25w-1) |
| **Status LEDs (`LED_CAL_IN`, `LED_CAL_OUT`, `LED_PWR`)** | 3× 3mm / 5mm Diffused LEDs (Amber, Blue, Green) | BerryBase / Reichelt | **€0.60** total | [BerryBase 5mm LED](https://www.berrybase.de/led-5mm-bedrahtet) |
| **Connector Socket (`J1`)** | 2-Pin 2.54 mm Socket / JST-XH 2.54 mm 2-pin | BerryBase | **€0.35** | [BerryBase 2-Pin](https://www.berrybase.de/buchsenleiste-1x2-polig-rm-2-54) |

---

## 3. "Smart Cart" Sourcing Optimization

Instead of ordering individual items across 10 different sites and paying multiple delivery fees, you can assemble the entire project using **two consolidated baskets**:

### Option A: The "BerryBase Maker Cart" (Consolidated Electronics)
Ordering all electronics together from **BerryBase.de** pays only a single **€4.90 DHL fee** (or €0 shipping if above €79):
1. Seeed Studio XIAO ESP32-S3 Sense: **€14.90**
2. 2× Elecrow JSN-SR04T Waterproof Sensors: **€19.80** (€9.90 × 2)
3. Adafruit/SparkFun MAX98357A I2S Amplifier: **€6.90**
4. 40mm 8Ω 2W Mini Speaker: **€2.80**
5. Soldered CN3791 6V Solar MPPT Board: **€6.90**
6. 6V 1.5W Mini Solar Panel: **€6.20**
7. 18650 Battery Holder: **€1.30**
8. KiCad Passives (Button, LEDs, Resistors, Pins): **~€2.50**
* **BerryBase Cart Subtotal:** **€61.30** (+ €4.90 DHL = **€66.20**)

### Option B: The "Amazon.de Prime Cart" (Fastest Turnaround & Mechanical Hardware)
Ordering the mechanical, optical, and battery parts with next-day Prime delivery (€0 shipping):
1. Protected 18650 Li-Ion Cell 3400mAh (with safety PCB): **€9.99**
2. 20mm Borosilicate Optical Glass Disc (2-pack): **€4.99**
3. ePTFE Hydrophobic Acoustic Vent Stickers: **€5.99**
4. M4×20mm Screws + Brass Heat-Set Inserts kit: **€6.99**
5. Stainless Steel Hose Clamps (Ø 90–120mm): **€5.99**
* **Amazon Cart Subtotal:** **€33.95** (Prime free next-day delivery)

---

### Grand Total Prototype Build Cost: **~€95.25 – €100.15**
*(Includes all electronic modules, dual waterproof sensors, camera, battery, solar charging system, optical glass, waterproof vents, and mounting hardware delivered to your door in Germany within 1–2 business days).*
