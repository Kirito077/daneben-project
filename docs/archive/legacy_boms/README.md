# Archived Legacy Bills of Materials (BOM)

This directory contains legacy, superseded, and duplicate Bill of Materials (BOM) files that have been phased out to keep the project repository clean, authoritative, and uncluttered.

---

## 📦 Active, Production BOM Files

All current procurement work and hardware evaluations MUST reference the two official BOM files located in [`docs/`](../):

1. **[`Daneben_Hardware_BoM_Core.xlsx`](../Daneben_Hardware_BoM_Core.xlsx)** ([📄 PDF Version](../Daneben_Hardware_BoM_Core.pdf))
   * **Scope:** The 4 core electronic subsystems (Seeed Studio XIAO ESP32-S3 Sense, 2× JSN-SR04T waterproof ultrasonic modules, MAX98357A I2S amplifier, 3W mini speaker).
   * **Layout:** Clean, standard Excel grid format exported to a single-page landscape PDF with primary and alternative German vendors (Farnell, Funduino, Reichelt, BerryBase).

2. **[`Daneben_Hardware_BoM_Full.xlsx`](../Daneben_Hardware_BoM_Full.xlsx)** ([📄 PDF Version](../Daneben_Hardware_BoM_Full.pdf))
   * **Scope:** Full 12-item prototype hardware bill of materials (Core compute, dual sensors, solar MPPT, 18650 cell, optical glass, waterproof acoustic membrane, stainless mounting bands).
   * **Layout:** Clean, standard Excel grid format exported to a single-page landscape PDF with subtotals, VAT gross totals (€67.77), and prototype notices.

---

## 🗄️ Archived Files in this Directory

| File Name | Format | Status / Reason for Archiving |
| :--- | :--- | :--- |
| `Daneben_Hardware_BoM.html` | Interactive HTML | **Phased Out**: Overly colorful web format with CSS badges, replaced by native Microsoft Excel format per project standards. |
| `Daneben_Hardware_BoM_pw.pdf` | PDF (Playwright export) | **Phased Out**: Rendered export of the obsolete colorful HTML template. |
| `Daneben_Hardware_BoM.xlsx` | Excel `.xlsx` | **Superseded / Duplicate**: Intermediate working file, replaced and cleanly split into `_Core.xlsx` and `_Full.xlsx`. |
| `Daneben_Hardware_BoM.pdf` | PDF | **Superseded / Duplicate**: Intermediate working file, replaced by `Daneben_Hardware_BoM_Full.pdf`. |
