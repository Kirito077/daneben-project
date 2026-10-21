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
  * **Presentations & Pitches (1-Minute Sales Pitch):**
    * [`Daneben_1Min_Sales_Pitch_Visual_Edition.pptx`](docs/Daneben_1Min_Sales_Pitch_Visual_Edition.pptx) ([🇩🇪 DE Version](docs/Daneben_1Min_Sales_Pitch_Visual_Edition_DE.pptx)) — **Visual Doodle Edition**: High-tempo 60-second pitch with animated vector illustrations, exploded 3D CAD hardware, and research citations.
    * [`Daneben_1Min_Sales_Pitch.pptx`](docs/Daneben_1Min_Sales_Pitch.pptx) ([🇩🇪 DE Version](docs/Daneben_1Min_Sales_Pitch_DE.pptx)) — **Standard Edition**: Clean white presentation with side-by-side analytical cards, labeled exploded hardware, and timed speaker notes.
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
  * 📁 **`Daneben circuit board/`** — Custom KiCad project files (`.kicad_pcb`, `.kicad_sch`, `.kicad_pro`) implementing the power management, ESP32-S3 processing, and sensor interfaces.
* 📁 **`src/`**
  * [`main.cpp`](src/main.cpp) — ESP32-S3 firmware: 2-stage distance debounce filter (8-second timer), Edge Impulse camera inference, and MQTT publishing.
  * [`internal_sensor.cpp`](src/internal_sensor.cpp) — Internal container fill level detection and MAX98357A I2S acoustic deterrent logic.

---

## ⚡ Quick Technical Specifications
* **MCU:** ESP32-S3 Sense (Dual-Core 240MHz, 8MB PSRAM, Wi-Fi / BLE, Camera interface).
* **Presence Sensor:** Multi-zone ToF (VL53L5CX) or JSN-SR04T Waterproof Ultrasonic.
* **Internal Sensor:** JSN-SR04T Waterproof Ultrasonic transducer under the container lid.
* **Power:** 2&times; 18650 LiFePO4 cells (3.2V nominal, 3000mAh) + 5V 1.5W Monocrystalline solar panel + CN3791 MPPT charger.
* **Enclosure Rating:** IP67 (Polycarbonate, 20° sloped roof, drip edge, silicone O-rings, borosilicate optical glass with UV adhesive, hydrophobic ePTFE acoustic membrane for speaker).
