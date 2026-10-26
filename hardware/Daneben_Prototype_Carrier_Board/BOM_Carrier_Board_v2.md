# Daneben! Prototype Carrier Board v2.0 — Bill of Materials (BOM)

> **Document Type:** Hardware Bill of Materials (Material & Component Specifications)  
> **PCB Revision:** Version 2.0 (130.0 mm &times; 90.0 mm &times; 1.6 mm, 2-Layer FR4)  
> **Course:** HSNR · 5. Semester · Mikrocontroller  

---

## 1. Electrical & Electromechanical Components

| Item | Designator | Qty | Component | Technical Specification | Package / Footprint | Material & Mounting Remarks |
| :---: | :--- | :---: | :--- | :--- | :--- | :--- |
| **1** | `U_MCU` | 1 | Microcontroller Module | Seeed Studio XIAO ESP32-S3 Sense (with OV2640) | Dual 1&times;7 Socket, 2.54 mm pitch | Pluggable daughterboard |
| **2** | `U_AJ_OUT`, `U_AJ_IN` | 2 | Ultrasonic Transceiver Module | AJ-SR04M / JSN-SR04T Board (25 kHz) | 1&times;4 Socket, 2.54 mm + 4&times; M2.5 holes | 41.5 &times; 28.5 mm PCB, external probe cable |
| **3** | `U_AMP` | 1 | Audio Amplifier Breakout | MAX98357A Class-D I2S Mono DAC/Amp | 1&times;7 Socket, 2.54 mm + 2&times; M2.5 holes | 19.0 &times; 18.0 mm PCB |
| **4** | `J_USBC` | 1 | USB Type-C Receptacle | 16-Pin, USB 2.0 / Power Only (5V / 3A) | `HRO_TYPE-C-31-M-12` (SMT/THT hybrid) | Stainless steel shield, horizontal |
| **5** | `C_BULK1` | 1 | Electrolytic Capacitor | 100 µF, 16V (or 25V), &plusmn;20% | Radial Can D6.3 mm, Pitch 2.5 mm | Aluminum electrolytic, polarized |
| **6** | `R_CC1`, `R_CC2` | 2 | Resistor | 5.1 kΩ, 0.25W, &plusmn;1% | Axial DIN0207 (or 0805 SMD) | Metal film |
| **7** | `R_PWR`, `R_LED_OUT`, `R_LED_IN` | 3 | Resistor | 1.0 kΩ, 0.25W, &plusmn;5% | Axial DIN0207 (or 0805 SMD) | Metal film |
| **8** | `SW_PWR` | 1 | Slide Switch | SPDT, 3-Pin, 50V 0.5A | Through-Hole, Pitch 2.54 mm | C&K OS102011 equivalent, vertical |
| **9** | `SW_CAL_OUT`, `SW_CAL_IN` | 2 | Tactile Pushbutton | SPST-NO, Momentary, 12 mm &times; 12 mm | Through-Hole, 4-Pin | Omron B3F-4050 equivalent, round cap |
| **10** | `LED_PWR` | 1 | LED (Green) | 3 mm Through-Hole, 2.1V, 20 mA | Radial 2-Pin, Pitch 2.54 mm | Diffused green epoxy lens |
| **11** | `LED_CAL_OUT` | 1 | LED (Blue) | 3 mm Through-Hole, 3.2V, 20 mA | Radial 2-Pin, Pitch 2.54 mm | Diffused blue epoxy lens |
| **12** | `LED_CAL_IN` | 1 | LED (Amber) | 3 mm Through-Hole, 2.0V, 20 mA | Radial 2-Pin, Pitch 2.54 mm | Diffused amber epoxy lens |
| **13** | `J_SPK`, `J_EXT_5V` | 2 | Screw Terminal Block | 2-Pin, 5.08 mm pitch, 300V / 10A | Through-Hole, Pitch 5.08 mm | PA66 green housing, captive M2.6 screws |
| **14** | `J_MCU_L`, `J_MCU_R` | 2 | Pin Socket Header | 1&times;7 Female, Single Row, 2.54 mm pitch | Through-Hole Vertical | Black PBT, gold-plated contacts |
| **15** | `J_AMP` | 1 | Pin Socket Header | 1&times;7 Female, Single Row, 2.54 mm pitch | Through-Hole Vertical | Black PBT, gold-plated contacts |
| **16** | `J_AJ_OUT`, `J_AJ_IN` | 2 | Pin Socket Header | 1&times;4 Female, Single Row, 2.54 mm pitch | Through-Hole Vertical | Black PBT, gold-plated contacts |
| **17** | `J_AUX` | 1 | Pin Header | 1&times;6 Male, Single Row, 2.54 mm pitch | Through-Hole Vertical | Breakaway male header, brass pins |
| **18** | `LS1` | 1 | Miniature Speaker | 8 Ω, 0.5W – 3W, 300 Hz – 10 kHz | Wire Lead Connection (to `J_SPK`) | Mylar cone / Dynamic driver, &oslash; 28–40 mm |

---

## 2. Mechanical Hardware & Raw Materials

| Item | Description | Qty | Specification | Material | Mounting Notes |
| :---: | :--- | :---: | :--- | :--- | :--- |
| **19** | Carrier PCB | 1 | 130.0 mm &times; 90.0 mm, 2-Layer | FR4 (1.6 mm thickness, 1 oz Cu) | Lead-free HASL / ENIG, green solder mask |
| **20** | Daughterboard Standoffs | 10 | M2.5 &times; 8.0 mm (M-F or F-F) | Nylon (or Brass) + M2.5 screws/nuts | 4&times; AJ-SR04M #1, 4&times; AJ-SR04M #2, 2&times; MAX98357A |
| **21** | Board Corner Standoffs | 4 | M3 &times; 12.0 mm (F-F) | Nylon (or Brass) + M3 screws | 4&times; corner chassis mounting holes |

---

## 3. Cost Summary (German Retail Reference)

| Category | Typical Unit Cost Range | Subtotal |
| :--- | :---: | :---: |
| **Core Modules (XIAO ESP32-S3 Sense, 2&times; AJ-SR04M, MAX98357A)** | €4.50 – €16.00 | ~€29.50 |
| **Onboard Passives, Connectors, Switches & LEDs (Items 4–17)** | €0.05 – €0.60 | ~€4.50 |
| **Speaker & Mechanical Hardware (Items 18–21)** | €1.00 – €3.00 | ~€4.90 |
| **Custom Carrier Board PCB (Item 19, small-batch)** | €2.50 – €3.50 | ~€3.00 |
| **Total Prototype Hardware Cost** | | **~€41.90** |
