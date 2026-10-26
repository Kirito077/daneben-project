# Daneben! — Smart Waste Bin Detection System

**Course:** Mikro-controller (5. Semester) · Hochschule Niederrhein (HSNR)  
**Antigravity Project:** `daneben-project` (`C:\Users\ekwug\.gemini\antigravity\projects\daneben-project`)  
**Workspace:** `C:\Users\ekwug\OneDrive\Documents\Deutschland\HSNR\Studium\5.Semester\Mikro-contoller\Daneben Projekt`  

---

## 📌 Project Overview
"Daneben!" is a solar-powered, retrofittable IoT Edge AI system mounted on municipal waste bins. It monitors the surrounding pavement for illegally dumped waste (bags, boxes), ignores pedestrians to preserve privacy (GDPR compliance), prompts users with acoustic messages if space remains inside the container, and reports fill/dumping status live to sanitation departments via MQTT / LoRaWAN.

---

## 📂 Repository Structure

* 📁 **`docs/`**
  * **Presentations & Pitches (1-Minute Sales Pitch & Condensed Editions):**
    * [`Daneben_Condensed_Pitch_Visual_DE_AutoNarrated_1Min.pptx`](docs/Daneben_Condensed_Pitch_Visual_DE_AutoNarrated_1Min.pptx) — **Auto-Narrated 6-Slide Pitch (Visual Edition, 54s Total)**: Fully autonomous presentation with embedded studio-quality German neural voice narration (`de-DE-KillianNeural`). When started (**F5**), it speaks the entire presentation out loud and auto-advances through all 6 slides in **exactly 54 seconds** (strictly inside 1 minute) without touching the keyboard or mouse.
    * [`Daneben_Condensed_Pitch_DE_AutoNarrated_1Min.pptx`](docs/Daneben_Condensed_Pitch_DE_AutoNarrated_1Min.pptx) — **Auto-Narrated 6-Slide Pitch (Standard Edition, 54s Total)**: Standard analytical edition with identical embedded auto-narration and 54-second automatic slide timings.
    * [`Daneben_Condensed_Pitch_Visual_DE.pptx`](docs/Daneben_Condensed_Pitch_Visual_DE.pptx) ([🇬🇧 EN Version](docs/Daneben_Condensed_Pitch_Visual_EN.pptx)) — **Condensed 6-Slide Pitch (Visual Doodle Edition)**: Streamlined 6-slide deck combining Problem 1 (side-dumping) & Problem 2 (blind fleet routes) side-by-side with vector doodles and stat callouts, omitting the CCTV/market gap slide, preserving the exploded 3D CAD production hardware architecture with native editable callouts, omitting the Geschäftsmodell, and concluding with the "Let's keep the city clean!" wrap-up slide.
    * [`Daneben_Condensed_Pitch_DE.pptx`](docs/Daneben_Condensed_Pitch_DE.pptx) ([🇬🇧 EN Version](docs/Daneben_Condensed_Pitch_EN.pptx)) — **Condensed 6-Slide Pitch (Standard Edition)**: Clean analytical 6-slide presentation with structured cards, exploded CAD hardware, municipal ROI, and closing mission slide.
    * [`Daneben_1Min_Sales_Pitch_Visual_Edition.pptx`](docs/Daneben_1Min_Sales_Pitch_Visual_Edition.pptx) ([🇩🇪 DE Version](docs/Daneben_1Min_Sales_Pitch_Visual_Edition_DE.pptx)) — **Visual Doodle Edition (Full Pitch - 9 Slides)**: Complete 9-slide pitch with animated vector illustrations, exploded 3D CAD hardware, business model, and closing slogan.
    * [`Daneben_Pitch_Visual_Edition_DE_ohne_Geschaeftsmodell.pptx`](docs/Daneben_Pitch_Visual_Edition_DE_ohne_Geschaeftsmodell.pptx) ([🇬🇧 EN Version](docs/Daneben_Pitch_Visual_Edition_EN_no_business_model.pptx)) — **Academic Edition (Ohne Hardware & Geschäftsmodell - 7 Slides)**: Streamlined 7-slide version omitting both the exploded hardware and business model slides.
    * [`Daneben_1Min_Sales_Pitch.pptx`](docs/Daneben_1Min_Sales_Pitch.pptx) ([🇩🇪 DE Version](docs/Daneben_1Min_Sales_Pitch_DE.pptx)) — **Standard Edition (Full Pitch - 9 Slides)**: Clean white 9-slide presentation with side-by-side analytical cards, labeled exploded hardware, business model, and timed speaker notes.
    * [`Daneben_Pitch_DE_ohne_Geschaeftsmodell.pptx`](docs/Daneben_Pitch_DE_ohne_Geschaeftsmodell.pptx) ([🇬🇧 EN Version](docs/Daneben_Pitch_EN_no_business_model.pptx)) — **Standard Technical Edition (Ohne Hardware & Geschäftsmodell - 7 Slides)**: 7-slide standard presentation without exploded hardware or startup business case.
    * [`Daneben_1Min_Pitch_Script_EN.pdf`](docs/Daneben_1Min_Pitch_Script_EN.pdf) ([🇩🇪 DE Version](docs/Daneben_1Min_Pitch_Script_DE.pdf)) — **Spoken Pitch Scripts**: Precise 60-second word-for-word presentation delivery script with timed stage directions (0–15s Hook, 15–30s Problem, 30–45s Solution, 45–60s CTA).
  * **Bill of Materials (BOM) — Official Production Specifications:**
    * [`Daneben_Hardware_BoM_Full.pdf`](docs/Daneben_Hardware_BoM_Full.pdf) ([📊 Excel .xlsx](docs/Daneben_Hardware_BoM_Full.xlsx)) — **Full System BOM**: Complete 13-item production specification (compute, dual sensors, audio amp, speaker, solar MPPT, Li-ion cell, Carrier Board v2 PCB, calibration & interface hardware kit, optical window, membrane vents) in clean Excel grid layout (€70.77 gross parts total).
    * [`Daneben_Hardware_BoM_Prototype.pdf`](docs/Daneben_Hardware_BoM_Prototype.pdf) ([📊 Excel .xlsx](docs/Daneben_Hardware_BoM_Prototype.xlsx)) — **Benchtop Prototype BOM**: Focused 11-item BOM containing only the core electronics and Carrier Board v2.0 electrical components (ESP32-S3 Sense, dual ultrasonic sensors, I2S amp, speaker, custom carrier PCB, 2× tactile calibration buttons, 3× status LEDs, SPDT power switch, USB-C 5V power input, screw terminals, socket headers; mechanical fasteners excluded) (€40.75 gross parts total).
    * [`Daneben_Hardware_BoM_Core.pdf`](docs/Daneben_Hardware_BoM_Core.pdf) ([📊 Excel .xlsx](docs/Daneben_Hardware_BoM_Core.xlsx)) — **Core Electronics BOM**: Focused specification for the 4 primary electronic subsystems (ESP32-S3 Sense, 2× JSN-SR04T waterproof ultrasonic, MAX98357A I2S amp, 3W speaker) with Farnell & Funduino primary vendor sourcing (€33.25 gross parts total).
    * 📁 [`docs/archive/legacy_boms/`](docs/archive/legacy_boms/) — Archived legacy HTML and duplicate BOM iterations.
  * **Visual Architecture & Mindmaps:**
    * [`Daneben_Operational_Flowchart.pdf`](docs/Daneben_Operational_Flowchart.pdf) & [`.html`](docs/Daneben_Operational_Flowchart.html) — Complete operational flowchart mapping every state to its hardware component and software functionality.
    * [`Daneben_Project_Mindmap.pdf`](docs/Daneben_Project_Mindmap.pdf) & [`.html`](docs/Daneben_Project_Mindmap.html) — Presentation-ready visual Mind Map (Landscape PDF & interactive dashboard).
    * [`Project_Mindmap.md`](docs/Project_Mindmap.md) — Raw Markdown/Mermaid Mind Map chart.
  * **Technical Reports & Blueprints:**
    * [`Enclosure_3D_Design_Report_Detailed.pdf`](docs/Enclosure_3D_Design_Report_Detailed.pdf) — 2D Orthographic Blueprint (Front, Side, Top views) with exact millimeter dimensions, waterproofing details, and exploded 3D renders.
    * [`Enclosure_3D_Design_Report.pdf`](docs/Enclosure_3D_Design_Report.pdf) — Conceptual 3D external and exploded visualizations.
  * **Engineering Documentation & Analysis:**
    * [`CONVERSATION_HISTORY.md`](docs/CONVERSATION_HISTORY.md) — Complete transcript and architectural evolution of all discussions, trade-offs (RoboDog vs. Daneben), and engineering decisions.
    * [`Project_Workflow_and_Market_Analysis.md`](docs/Project_Workflow_and_Market_Analysis.md) — Problem statement, market analysis (municipalities, smart cities, housing), SaaS revenue model, and 5-year lifespan calculation.
    * [`AI_and_System_Expansions.md`](docs/AI_and_System_Expansions.md) — Comparison between pixel-differencing and Edge AI (Edge Impulse), internal container capacity sensing, and smart fleet telemetry.
* 📁 **`hardware/`**
  * [`daneben_enclosure.scad`](hardware/daneben_enclosure.scad) — Parametric 3D CAD model for OpenSCAD.
  * [`daneben_enclosure.stl`](hardware/daneben_enclosure.stl) — Compiled 3D mesh model ready to open directly in **Autodesk Inventor** or Windows 3D Viewer.
  * [`Enclosure_and_Hardware.md`](hardware/Enclosure_and_Hardware.md) — IP67 sealing strategy, 20° sloped roof, drip edges, and isolated battery cartridge system.
  * [`Parts_List.md`](hardware/Parts_List.md) — Technical Bill of Materials (BOM) with unit costs at scale (~$29.50 BOM).
  * [`Procurement_Parts_List.md`](hardware/Procurement_Parts_List.md) — Complete purchasing list with **exact dimensions, specs, and 3 fast-shipping store links** per component (Amazon.de, BerryBase, Reichelt).
  * [`Budget_Showcase_Prototype_Template.md`](hardware/Budget_Showcase_Prototype_Template.md) — Low-cost (~€28) tabletop demonstration template for student presentations and live demo evaluations.
  * 📁 **[`Daneben_Prototype_Carrier_Board/`](hardware/Daneben_Prototype_Carrier_Board/)** — Complete KiCad 9 modular prototype carrier board project (`.kicad_pcb`, `.kicad_sch`, `.kicad_pro`, PDF/SVG exports, and generator scripts) with integrated power rails, sensor sockets, audio header, and modular expansion buses.
  * 📁 **`Daneben circuit board/`** — Original KiCad project files (`.kicad_pcb`, `.kicad_sch`, `.kicad_pro`) implementing the power management, ESP32-S3 processing, and sensor interfaces.
* 📁 **`src/`**
  * [`main.cpp`](src/main.cpp) — ESP32-S3 firmware: 2-stage distance debounce filter (8-second timer), Edge Impulse camera inference, and MQTT publishing.
  * [`internal_sensor.cpp`](src/internal_sensor.cpp) — Internal container fill level telematics (stationary upper collar angled mount, 0–100% continuous tracking with trigonometric depth correction) and MAX98357A I2S acoustic deterrent logic.
  * [`calibration.h`](src/calibration.h) — Dual tactile button calibration engine: interactive baseline zeroing, threshold configuration, EEPROM/NVS persistent storage, and status LED telemetry.

---

## ⚡ Quick Technical Specifications
* **MCU:** ESP32-S3 Sense (Dual-Core 240MHz, 8MB PSRAM, Wi-Fi / BLE, Camera interface).
* **Presence Sensor:** Multi-zone ToF (VL53L5CX) or JSN-SR04T Waterproof Ultrasonic (angled 45° at pavement).
* **Internal Sensor:** JSN-SR04T Waterproof Ultrasonic transducer mounted on the fixed upper collar/inner rim angled downward (~25°) toward the central trash cone (eliminates moving wires across swinging lids, prevents snagging during municipal emptying, and delivers continuous 0–100% capacity tracking).
* **Power:** 2&times; 18650 LiFePO4 cells (3.2V nominal, 3000mAh) + 5V 1.5W Monocrystalline solar panel + CN3791 MPPT charger.
* **Enclosure Rating:** IP67 (Polycarbonate, 20° sloped roof, drip edge, silicone O-rings, borosilicate optical glass with UV adhesive, hydrophobic ePTFE acoustic membrane for speaker).
