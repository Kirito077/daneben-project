# Daneben Projekt — Complete Architectural & Engineering Conversation Archive

> **Project Reference:** Daneben! — Der Müll gehört in die Tonne  
> **Course / Academic Context:** HSNR Studium · 5. Semester · Mikro-controller  
> **Antigravity Conversation ID:** `793ac40f-0ce7-467c-98f3-dcd30f32e172`  
> **Antigravity Project Path:** `C:\Users\ekwug\.gemini\antigravity\projects\daneben-project\`  
> **OneDrive Project Path:** `C:\Users\ekwug\OneDrive\Documents\Deutschland\HSNR\Studium\5.Semester\Mikro-contoller\Daneben Projekt\`  

---

## Table of Contents
1. [Initial Scoping & Project Comparison](#1-initial-scoping--project-comparison)
2. [Why Daneben Was Chosen Over RoboDog](#2-why-daneben-was-chosen-over-robodog)
3. [System Workflow & Market Analysis](#3-system-workflow--market-analysis)
4. [Hardware & Power Architecture](#4-hardware--power-architecture)
5. [Enclosure, IP67 Sealing & 3D CAD Modeling](#5-enclosure-ip67-sealing--3d-cad-modeling)
6. [Sensing & Edge AI Pipeline](#6-sensing--edge-ai-pipeline)
7. [System Expansions (Internal Bin Sensor & Deterrent)](#7-system-expansions-internal-bin-sensor--deterrent)
8. [Project File Map & Generated Assets](#8-project-file-map--generated-assets)

---

## 1. Initial Scoping & Project Comparison

The initial consultation evaluated two prospective student hardware projects:
1. **RoboDog (Self-built 3D-Printed Quadruped Exoskeleton):**
   * *Objective:* Control a 3D-printed quadruped exoskeleton with 8–12 servos from a smartphone over Wi-Fi/Bluetooth, achieving stable calibration and reliable walking gaits.
   * *Architecture:* ESP32-S3 microcontroller, PCA9685 16-channel I2C PWM driver, 2S LiPo battery (7.4V), 5V/6V 8A peak UBEC buck converter, 1000 µF decoupling capacitor, MPU6050 6-axis IMU, and asynchronous web server joystick UI.
   * *Drawbacks:* High failure rate on demo day due to stripped servo gears, high-current brownout reboots, joint friction, and hours of inverse kinematics (IK) gait tuning.
2. **"Daneben!" (Smart Waste Bin Placement Detector):**
   * *Objective:* Detect trash bags or cardboard boxes placed illegally *beside* waste bins, filter out passing pedestrians (GDPR privacy compliance), notify waste management services, and prompt users if the bin is not full.
   * *Architecture:* Solid-state Edge AI camera (ESP32-S3 Sense), low-power multi-zone ToF / ultrasonic distance sensor, LiFePO4 batteries, solar trickle-charging, waterproof IP67 enclosure, and cloud telemetry.

---

## 2. Why Daneben Was Chosen Over RoboDog

| Metric | RoboDog Exoskeleton | "Daneben!" Smart Waste Monitor |
| :--- | :--- | :--- |
| **Engineering Domain** | Actuation, power surges, dynamic balancing | Embedded IoT, edge sensing, computer vision |
| **Moving Parts** | 8 to 12 servo gearboxes (mechanical fatigue) | **Zero moving parts** (solid-state) |
| **Primary Failure Modes** | Stripped gears, voltage brownouts, slipping feet | Outdoor lighting variation (mitigated by AI) |
| **Testing Environment** | Physical floor space, fragile during falls | Desk-friendly, repeatable software states |
| **Demo Day Reliability** | Low to Moderate | **High (predictable state machine)** |
| **Difficulty Rating** | **8 / 10** | **5 / 10** |

**Conclusion:** Daneben provides far higher engineering reliability, eliminates mechanical breakdowns, and addresses a practical smart-city municipal problem.

---

## 3. System Workflow & Market Analysis

* **The Problem:** Illegal placement of waste bags and cardboard boxes beside containers creates hygiene hazards, attracts pests, and incurs heavy manual labor costs for city sanitation departments.
* **The Solution:** A retrofittable, solar-assisted, Edge-AI smart sensor unit that detects deposited waste, ignores pedestrians, checks internal container capacity, triggers acoustic guidance, and sends telemetry to central dispatch.
* **Market Opportunity:**
  * Municipalities & Smart Cities (route optimization and reduced manual cleanup costs).
  * Private Waste Management Operators (e.g., Remondis, Veolia — SLA performance tracking).
  * Housing Associations & Property Management (preventing residential dumping hotspots).
* **Business Model:**
  * Hardware sale or lease (~$150–$200 per unit; bill-of-materials ~$30–$40 at scale).
  * Software-as-a-Service (SaaS): $3–$5 per bin/month for live dashboard monitoring, heatmaps, and route optimization.
* **Lifespan Calculation:**
  * **LiFePO4 Cells:** ~2,000 charge cycles; with solar trickle charging rarely deep-discharges &rarr; **4 to 6 years**.
  * **Polycarbonate Enclosure:** UV-stabilized resin prevents brittleness &rarr; **5 to 7 years**.
  * **Overall Unit Lifespan:** Rated for **~5 years** continuous outdoor deployment.

---

## 4. Hardware & Power Architecture

### Microcontroller & Processing
* **ESP32-S3 Sense (or Seeed Studio XIAO ESP32-S3 Sense):**
  * Dual-Core Xtensa LX7 @ 240 MHz.
  * Native 8 MB PSRAM for image frame buffering and neural network tensor arena.
  * Integrated 2.4 GHz Wi-Fi and Bluetooth LE 5.0.
  * Direct camera interface (OV2640 / OV5640).

### Power Subsystem
* **Battery Chemistry:** Two **18650 LiFePO4 (Lithium Iron Phosphate)** cells in parallel (3.2V nominal, ~3000–3400 mAh total).
  * Superior thermal stability (-20°C to +60°C) compared to standard Li-ion cells.
  * Non-combustible under mechanical compression.
* **Solar Harvesting:** Flush-mounted 5V, 1.5W monocrystalline solar panel integrated into the 20° sloped lid.
* **Charge Controller:** CN3791 Maximum Power Point Tracking (MPPT) solar charger circuit to maximize power harvest under cloudy conditions.
* **Custom PCB Architecture:**
  * Designed in KiCad (`hardware/Daneben circuit board/`).
  * "Inverted T" or "L" geometry:
    * *Top Section:* Solar input, MPPT charger, reverse-polarity protection, battery contacts.
    * *Mid Section:* ESP32-S3 module, RF antenna trace near enclosure wall, status LEDs.
    * *Bottom Section:* Camera sensor connector, ultrasonic / ToF header, speaker amplifier (MAX98357A I2S).
  * Coated with acrylic conformal coating (except optical and sensor contact surfaces) to protect against condensation.

---

## 5. Enclosure, IP67 Sealing & 3D CAD Modeling

### Geometric Specifications
* **Outer Dimensions:** 120 mm (W) &times; 150 mm (H) &times; 80 mm (D).
* **Wall Thickness:** 3.0 mm UV-stabilized Polycarbonate.
* **Roof Angle:** 20° slope to shed precipitation and optimize solar irradiance.
* **Drip Edge Overhang:** Protrudes 4 mm past the perimeter seam to prevent water pooling on the main silicone gasket.

### Waterproofing Solutions (IP67)
1. **Camera Lens Window:**
   * 20 mm diameter, 2 mm thick scratch-resistant **Borosilicate optical glass disc**.
   * Sealing: Secured from inside against a flat silicone gasket using industrial UV-curable optical adhesive.
2. **Speaker Acoustic Ports:**
   * Front-facing sound ports are protected from the interior by an **ePTFE hydrophobic acoustic membrane** (Gore-Tex acoustic vent).
   * Allows sound waves (&gt;85 dB) and air pressure equalization while completely blocking water ingress.
3. **Distance Sensor Port:**
   * Employs an inherently sealed **JSN-SR04T waterproof ultrasonic transducer** fitted through a compression rubber grommet.
4. **Tool-Free Battery Service Cartridge:**
   * Bottom-accessible isolated tubular battery compartment with a threaded double-O-ring endcap.
   * Allows field technicians to swap batteries in seconds without opening the main electronics chamber or breaking the IP67 seal.
5. **Bin Attachment System:**
   * Concave rear plate matching standard 120L/240L wheelie bin lip contours.
   * Dual 75 mm &times; 5 mm slots for heavy-duty stainless steel band clamps or industrial UV-resistant nylon ties (drill-free mounting).

### CAD Assets Produced
* **Parametric Model:** `hardware/daneben_enclosure.scad` (OpenSCAD script for 3D printing and STL/STEP generation).
* **Technical Blueprints & Renders:** `Enclosure_3D_Design_Report_Detailed.pdf` (Orthographic 3-view blueprints with dimensional callouts and exploded internal renderings).

---

## 6. Sensing & Edge AI Pipeline

### The Two-Stage Presence Debounce Filter
To avoid false triggers and strictly comply with privacy regulations (GDPR: no photography of passersby):

```
[ Ultrasonic / ToF Distance Sensor ] (Ultra-Low Power Polling @ 2 Hz)
                    |
                    | (Object within < 1.5m)
                    v
    [ Debounce Timer: Wait 8.0 Seconds ]
                    |
         +----------+----------+
         |                     |
   (Object Clears <3s)   (Object Remains >8s)
         |                     |
         v                     v
   [ Discard Event ]     [ Wake ESP32-S3 Camera ]
   (Pedestrian Ignored)        |
                               v
                         [ Ground-Angle Image Capture ]
                               |
                               v
                         [ Edge Impulse Neural Classifier ]
                               |
                   +-----------+-----------+
                   |                       |
             (Waste Detected)        (No Waste / Dog / Stroller)
                   |                       |
                   v                       v
           [ Check Bin Fullness ]     [ Power Down Camera & Sleep ]
```

### Background Differencing vs. Lightweight Edge AI
* **Background Differencing / Pixel Diff:** Vulnerable to sunlight shifts, shadows, wet pavement reflections, and blowing leaves &rarr; High false positive rate outdoors.
* **Lightweight Edge AI (Selected):** Quantized MobileNetV2 / YOLO-nano model trained via Edge Impulse. Differentiates actual waste bags/boxes from animals or feet regardless of ambient lighting.

---

## 7. System Expansions (Internal Bin Sensor & Deterrent)

1. **Internal Container Fill Level Sensor:**
   * Downward-facing JSN-SR04T ultrasonic transducer mounted on the container lid.
   * Measures depth to trash surface (Depth &lt; 20 cm = Container Full).
2. **Interactive Acoustic Deterrent:**
   * If waste is detected *outside* while internal sensor reports available capacity, the device plays an audio prompt via the MAX98357A amplifier:
     > *"Bitte den Müll in die Tonne werfen. Es ist noch Platz!"*
3. **Telemetry & Compliance Logging:**
   * System records if the warning was heeded or ignored after a 5-minute cooldown.
   * Transmits timestamped payloads over MQTT / LoRaWAN:
     `city/bins/daneben/{bin_id}/status` &rarr; `{"event": "ILLEGAL_DUMPING", "bin_full": false, "warning_ignored": true}`

---

## 8. Project File Map & Generated Assets

```
Daneben Projekt/
├── docs/
│   ├── CONVERSATION_HISTORY.md                 <-- Full transcript and architectural record
│   ├── Project_Workflow_and_Market_Analysis.md <-- Business plan, market segments, SaaS model
│   └── AI_and_System_Expansions.md             <-- AI classification, acoustic deterrent, MQTT
├── hardware/
│   ├── daneben_enclosure.scad                  <-- Parametric 3D CAD model (OpenSCAD)
│   ├── Enclosure_and_Hardware.md               <-- IP67 specs, battery cartridge, PCB layout
│   ├── Parts_List.md                           <-- Complete Bill of Materials (BOM)
│   └── Daneben circuit board/                  <-- KiCad PCB schematics, layouts, and routing
│       ├── Daneben circuit board.kicad_pcb
│       ├── Daneben circuit board.kicad_sch
│       └── Daneben circuit board.kicad_pro
├── src/
│   ├── main.cpp                                <-- External sensor, debounce, AI, and MQTT firmware
│   └── internal_sensor.cpp                     <-- Internal fill detection and audio warning firmware
├── Enclosure_3D_Design_Report.pdf              <-- Conceptual 3D renders and exterior overview
├── Enclosure_3D_Design_Report_Detailed.pdf     <-- 2D orthographic blueprints with exact millimeter dimensions
└── README.md                                   <-- Project master summary and quickstart
```
