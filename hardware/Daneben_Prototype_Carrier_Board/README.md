# "Daneben!" — Modular Prototype Carrier Board Version 2.0 (KiCad 9)

> **Purpose:** Custom modular carrier board designed to house all electronic subsystems of the "Daneben!" system for student showcases, laboratory testing, and benchtop demonstration without messy floating wires.  
> **Course / Academic Context:** Hochschule Niederrhein (HSNR) · 5. Semester · Mikro-controller  
> **KiCad Version:** 9.0.4  
> **Dimensions:** 130.0 mm &times; 90.0 mm (FR4 2-Layer, 1.6 mm thickness, 4&times; M3 mounting holes, R=4.0 mm rounded corners)  
> **Active Production Version:** Version 2.0 (Historical V1 files archived in [`archive_v1/`](file:///c:/Users/ekwug/OneDrive/Documents/Deutschland/HSNR/Studium/5.Semester/Mikro-contoller/Daneben%20Projekt/hardware/Daneben_Prototype_Carrier_Board/archive_v1/))

---

## 1. Subsystem Architecture & Features (v2.0)

This board acts as a central modular motherboard, providing standardized sockets, mechanical standoff mounts, dedicated power conditioning, and hardware calibration controls:

```
+-----------------------------------------------------------------------------------------------------------------------+
| [H1: M3]                                                                                                     [H2: M3] |
|                                                                                                                       |
|  +---------------------------------------+      +-------------------------------+      +----------------------------+ |
|  |     AJ-SR04M DOCK 1 (OUTSIDE / FLOOR) |      |      SEEED XIAO ESP32-S3      |      |     I2S AUDIO & SPEAKER    | |
|  |                                       |      |             SENSE             |      |                            | |
|  | [Transducer Jack Exits Left <---]     |      |                               |      | [J_AMP: MAX98357A Socket]  | |
|  |                                       |      |  [J_MCU_L]         [J_MCU_R]  |      |  (2x M2.5 Standoff Holes)  | |
|  | [4x M2.5 Standoff Mounting Holes]     |      |  D0: TRIG_OUT      D7: IN_STAT|      |                            | |
|  | [J_AJ_OUT: 4-Pin Socket (5V/Trig/Echo/GND)]  |  D1: ECHO_OUT      D8: BCLK   |      | [J_SPK: 2-Pin Screw Term]  | |
|  +---------------------------------------+      |  D2: TRIG_IN       D9: LRC    |      |  (SPK+ / SPK- Differential)| |
|                                                 |  D3: ECHO_IN       D10: DIN   |      +----------------------------+ |
|                                                 |  D4: BTN_CAL_OUT   3V3: +3V3  |                                     |
|  +---------------------------------------+      |  D5: BTN_CAL_IN    GND: GND   |      +----------------------------+ |
|  |     AJ-SR04M DOCK 2 (INSIDE / DEPTH)  |      |  D6: OUT_STAT      5V: +5V    |      |     SIZABLE CALIBRATION    | |
|  |                                       |      +-------------------------------+      |     CONTROLS (12x12mm)     | |
|  | [Transducer Jack Exits Left <---]     |                                             |                            | |
|  |                                       |      +-------------------------------+      | [SW_CAL_OUT: 12x12mm Blue] | |
|  | [4x M2.5 Standoff Mounting Holes]     |      |   DEDICATED USB-C POWER ENTRY |      |  (Floor Distance Reference)| |
|  | [J_AJ_IN: 4-Pin Socket (5V/Trig/Echo/GND)]   |                               |      | [LED_CAL_OUT: Blue Status] | |
|  +---------------------------------------+      | [J_USBC: Type-C Port (5V)]    |      |                            | |
|                                                 | [R_CC1 / R_CC2: 5.1k PD]      |      | [SW_CAL_IN: 12x12mm Amber] | |
|                                                 | [SW_PWR: On/Off Slide Switch] |      |  (Bin Depth 1m-4m NVS Cal) | |
|                                                 | [C_BULK1: 100uF Bulk Reservoir]      | [LED_CAL_IN: Amber Status] | |
|                                                 | [J_EXT_5V: Screw Terminal In] |      +----------------------------+ |
|                                                 | [LED_PWR: Green Power LED]    |                                     |
|                                                 +-------------------------------+      [J_AUX: 1x6 Expansion Header]  |
| [H3: M3]                                                                                                     [H4: M3] |
+-----------------------------------------------------------------------------------------------------------------------+
```

---

## 2. Key Engineering Improvements in v2.0

### 2.1 Zero-Friction AJ-SR04M Waterproof Transducer Docks
* **Mechanical Stability:** Each AJ-SR04M sensor board is fastened to the carrier board using **4&times; M2.5 standoff screws**, eliminating wiggling, loose contacts, and vibrations.
* **Cable Clearance:** Both modules have their cylindrical metal transducer connectors positioned directly along the left PCB edge, pointing into free air. When the thick shielded transducer cables are attached, they exit outward with **zero bending friction or mechanical obstruction**.

### 2.2 Dedicated Onboard USB-C Power Entry
* Standard USB Type-C receptacle (`J_USBC`) on the bottom board edge with two 5.1 kΩ pull-down resistors (`R_CC1`, `R_CC2`) on CC1 and CC2. Automatically negotiates clean 5V (up to 3A) from modern USB-PD power banks and phone chargers.
* Onboard slide switch (`SW_PWR`) and green power LED (`LED_PWR`).
* 100 µF bulk capacitor (`C_BULK1`) buffers the sudden current draws of the MAX98357A Class-D amplifier.

### 2.3 Sizable 12&times;12 mm Dual Calibration Pushbuttons
* Whisbins and municipal waste bins vary widely in geometry (standard 120L/240L bins are ~1.0m deep, whereas large commercial or underground containers can be 2.0m to 4.0m deep).
* **`SW_CAL_OUT` (Outside / Floor Reference):** Runs 15 ultrasonic pings, averages baseline floor distance, and persists it into non-volatile storage (`Preferences` / NVS).
* **`SW_CAL_IN` (Inside / Bin Depth Reference):** One-click empty-bin calibration that auto-scales full percentage (0–100%) dynamically for any container depth.
* Driven by [`src/calibration.h`](file:///c:/Users/ekwug/OneDrive/Documents/Deutschland/HSNR/Studium/5.Semester/Mikro-contoller/Daneben%20Projekt/src/calibration.h).

---

## 3. How to View in KiCad 3D Viewer

1. Open [`Daneben_Prototype_Carrier_Board.kicad_pro`](file:///c:/Users/ekwug/OneDrive/Documents/Deutschland/HSNR/Studium/5.Semester/Mikro-contoller/Daneben%20Projekt/hardware/Daneben_Prototype_Carrier_Board/Daneben_Prototype_Carrier_Board.kicad_pro) in KiCad.
2. Open the PCB Editor (`Daneben_Prototype_Carrier_Board.kicad_pcb`).
3. Press **`Alt + 3`** (or go to **View &rarr; 3D Viewer**).
4. Real-time 3D models will display with exact millimeter alignment for the AJ-SR04M modules, Seeed XIAO Sense, MAX98357A, USB-C jack, and 12x12mm switches.

---

## 4. File Manifest

### Active Production Files (Version 2.0):
* [`Daneben_Prototype_Carrier_Board.kicad_pro`](file:///c:/Users/ekwug/OneDrive/Documents/Deutschland/HSNR/Studium/5.Semester/Mikro-contoller/Daneben%20Projekt/hardware/Daneben_Prototype_Carrier_Board/Daneben_Prototype_Carrier_Board.kicad_pro): Main project.
* [`Daneben_Prototype_Carrier_Board.kicad_sch`](file:///c:/Users/ekwug/OneDrive/Documents/Deutschland/HSNR/Studium/5.Semester/Mikro-contoller/Daneben%20Projekt/hardware/Daneben_Prototype_Carrier_Board/Daneben_Prototype_Carrier_Board.kicad_sch): Full master schematic.
* [`Daneben_Prototype_Carrier_Board.kicad_pcb`](file:///c:/Users/ekwug/OneDrive/Documents/Deutschland/HSNR/Studium/5.Semester/Mikro-contoller/Daneben%20Projekt/hardware/Daneben_Prototype_Carrier_Board/Daneben_Prototype_Carrier_Board.kicad_pcb): Complete routed 130x90mm PCB.
* [`carrier_board_schematic.pdf`](file:///c:/Users/ekwug/OneDrive/Documents/Deutschland/HSNR/Studium/5.Semester/Mikro-contoller/Daneben%20Projekt/hardware/Daneben_Prototype_Carrier_Board/carrier_board_schematic.pdf): Master schematic PDF.
* [`carrier_board_pcb_layout.pdf`](file:///c:/Users/ekwug/OneDrive/Documents/Deutschland/HSNR/Studium/5.Semester/Mikro-contoller/Daneben%20Projekt/hardware/Daneben_Prototype_Carrier_Board/carrier_board_pcb_layout.pdf): PCB fabrication layout PDF.
* [`carrier_board_v2_3d_isometric.png`](file:///c:/Users/ekwug/OneDrive/Documents/Deutschland/HSNR/Studium/5.Semester/Mikro-contoller/Daneben%20Projekt/hardware/Daneben_Prototype_Carrier_Board/carrier_board_v2_3d_isometric.png): High-res 3D isometric render.
* [`carrier_board_v2_3d_top.png`](file:///c:/Users/ekwug/OneDrive/Documents/Deutschland/HSNR/Studium/5.Semester/Mikro-contoller/Daneben%20Projekt/hardware/Daneben_Prototype_Carrier_Board/carrier_board_v2_3d_top.png): High-res 3D top-down render.
* [`carrier_board_v2_3d_front_angle.png`](file:///c:/Users/ekwug/OneDrive/Documents/Deutschland/HSNR/Studium/5.Semester/Mikro-contoller/Daneben%20Projekt/hardware/Daneben_Prototype_Carrier_Board/carrier_board_v2_3d_front_angle.png): High-res 3D front-angle render.
* [`build_v2_pcb.py`](file:///c:/Users/ekwug/OneDrive/Documents/Deutschland/HSNR/Studium/5.Semester/Mikro-contoller/Daneben%20Projekt/hardware/Daneben_Prototype_Carrier_Board/build_v2_pcb.py): Automated board generator.
* [`build_v2_schematic.py`](file:///c:/Users/ekwug/OneDrive/Documents/Deutschland/HSNR/Studium/5.Semester/Mikro-contoller/Daneben%20Projekt/hardware/Daneben_Prototype_Carrier_Board/build_v2_schematic.py): Automated schematic generator.
* [`generate_v2_3d_models.py`](file:///c:/Users/ekwug/OneDrive/Documents/Deutschland/HSNR/Studium/5.Semester/Mikro-contoller/Daneben%20Projekt/hardware/Daneben_Prototype_Carrier_Board/generate_v2_3d_models.py): Automated VRML 3D models generator.

### Archived Files:
* [`archive_v1/`](file:///c:/Users/ekwug/OneDrive/Documents/Deutschland/HSNR/Studium/5.Semester/Mikro-contoller/Daneben%20Projekt/hardware/Daneben_Prototype_Carrier_Board/archive_v1/): Contains all legacy Carrier Board Version 1.0 files and test scripts.
