import os
import uuid

sym_dir = r"C:\Program Files\KiCad\9.0\share\kicad\symbols"

def extract_symbol(lib_name, sym_name):
    path = os.path.join(sym_dir, lib_name + ".kicad_sym")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    start_tag = f'(symbol "{sym_name}"'
    idx = content.find(start_tag)
    if idx == -1:
        raise ValueError(f"Symbol {sym_name} not found in {lib_name}")
    depth = 0
    end_idx = idx
    for i in range(idx, len(content)):
        if content[i] == '(':
            depth += 1
        elif content[i] == ')':
            depth -= 1
            if depth == 0:
                end_idx = i + 1
                break
    sym_code = content[idx:end_idx]
    return sym_code.replace(f'(symbol "{sym_name}"', f'(symbol "{lib_name}:{sym_name}"', 1)

def gen_uuid():
    return str(uuid.uuid4())

def add_wire(x1, y1, x2, y2):
    return f"""\t(wire (pts (xy {x1:.2f} {y1:.2f}) (xy {x2:.2f} {y2:.2f}))
\t\t(stroke (width 0) (type default))
\t\t(uuid "{gen_uuid()}")
\t)\n"""

def add_label(name, x, y, angle=0):
    return f"""\t(label "{name}"
\t\t(at {x:.2f} {y:.2f} {angle})
\t\t(effects (font (size 1.27 1.27)))
\t\t(uuid "{gen_uuid()}")
\t)\n"""

def add_text(text, x, y, size=1.5, bold=False):
    bold_str = " (bold yes)" if bold else ""
    return f"""\t(text "{text}"
\t\t(at {x:.2f} {y:.2f} 0)
\t\t(effects (font (size {size} {size}){bold_str}))
\t\t(uuid "{gen_uuid()}")
\t)\n"""

def add_box(x1, y1, x2, y2):
    return f"""\t(polyline
\t\t(pts (xy {x1:.2f} {y1:.2f}) (xy {x2:.2f} {y1:.2f}) (xy {x2:.2f} {y2:.2f}) (xy {x1:.2f} {y2:.2f}) (xy {x1:.2f} {y1:.2f}))
\t\t(stroke (width 0.4) (type default))
\t\t(fill (type none))
\t\t(uuid "{gen_uuid()}")
\t)\n"""

def add_no_connect(x, y):
    return f"""\t(no_connect
\t\t(at {x:.2f} {y:.2f})
\t\t(uuid "{gen_uuid()}")
\t)\n"""

def add_sym(lib_id, ref, val, fp, x, y, angle=0):
    return f"""\t(symbol
\t\t(lib_id "{lib_id}")
\t\t(at {x:.2f} {y:.2f} {angle})
\t\t(unit 1)
\t\t(in_bom yes) (on_board yes)
\t\t(uuid "{gen_uuid()}")
\t\t(property "Reference" "{ref}" (at {x:.2f} {y-4.5:.2f} 0) (effects (font (size 1.27 1.27))))
\t\t(property "Value" "{val}" (at {x:.2f} {y+4.5:.2f} 0) (effects (font (size 1.27 1.27))))
\t\t(property "Footprint" "{fp}" (at {x:.2f} {y:.2f} 0) (effects (font (size 1.27 1.27)) (hide yes)))
\t)\n"""

def build_perfect_schematic():
    out_dir = "hardware/Daneben_Prototype_Carrier_Board"
    os.makedirs(out_dir, exist_ok=True)
    sch_file = os.path.join(out_dir, "Daneben_Prototype_Carrier_Board.kicad_sch")

    # Load exact symbols directly from official KiCad 9 library files
    symbols = []
    for lib, sym in [
        ("Connector_Generic", "Conn_01x02"),
        ("Connector_Generic", "Conn_01x04"),
        ("Connector_Generic", "Conn_01x06"),
        ("Connector_Generic", "Conn_01x07"),
        ("Device", "R"),
        ("Device", "LED"),
        ("Switch", "SW_Push")
    ]:
        symbols.append(extract_symbol(lib, sym))
    
    lib_symbols_block = "\t(lib_symbols\n" + "\n".join(["\t\t" + s for s in symbols]) + "\n\t)"

    sch = f"""(kicad_sch
\t(version 20250114)
\t(generator "eeschema")
\t(generator_version "9.0")
\t(uuid "{gen_uuid()}")
\t(paper "A3")
\t(title_block
\t\t(title "Daneben! Prototype Carrier Board (Modular Showcase Edition v2.0)")
\t\t(date "2026-10-26")
\t\t(rev "v2.0")
\t\t(company "Hochschule Niederrhein (HSNR) - Fachbereich Elektrotechnik & Informatik")
\t\t(comment 1 "Master Modular Carrier Board for Seeed Studio XIAO ESP32-S3 Sense")
\t\t(comment 2 "Dual AJ-SR04M Docks, Dedicated USB-C Power Entry, 12x12mm Calibration Controls")
\t)
{lib_symbols_block}
"""

    # Title Banner across top (Centered on A3 page)
    sch += add_text("DANEBEN! PROTOTYPE MODULAR CARRIER BOARD v2.0 - SCHEMATIC REVIEW", 30.0, 20.0, 2.5, True)
    sch += add_text("Architecture: Direct USB-C 5V Bus | XIAO ESP32-S3 Sense | Dual AJ-SR04M Zero-Friction Docks | MAX98357A I2S Audio | Dual Calibration Controls", 30.0, 26.0, 1.4, False)

    # =========================================================================
    # ROW 1 (TOP ROW): Y = 32.0 mm to Y = 142.0 mm
    # =========================================================================

    # -------------------------------------------------------------------------
    # BLOCK 1 (TOP-LEFT): PRIMARY POWER INTAKE & DISTRIBUTION
    # Boundary: X: 25.0 to 145.0 mm, Y: 32.0 to 142.0 mm
    # -------------------------------------------------------------------------
    sch += add_box(25.0, 32.0, 145.0, 142.0)
    sch += add_text("1. PRIMARY POWER INTAKE & DISTRIBUTION", 28.0, 38.0, 1.9, True)

    # J_USBC (Conn_01x06) at (50.80, 63.50). Pins at X = 50.80 - 5.08 = 45.72
    sch += add_sym("Connector_Generic:Conn_01x06", "J_USBC", "USB-C POWER IN (6P)", "Connector_USB:USB_C_Receptacle_HRO_TYPE-C-31-M-12", 50.80, 63.50)
    # Conn_01x06 pin dys: [5.08, 2.54, 0.0, -2.54, -5.08, -7.62] -> py = y - dy
    # Pin 1: VBUS_RAW (py = 58.42)
    sch += add_wire(35.56, 58.42, 45.72, 58.42)
    sch += add_label("VBUS_RAW", 35.56, 58.42, 180)
    # Pin 2: CC1 (py = 60.96)
    sch += add_wire(35.56, 60.96, 45.72, 60.96)
    sch += add_label("CC1", 35.56, 60.96, 180)
    # Pin 3 & Pin 4: Unused Data lines D- and D+ (marked no_connect at pin tips)
    sch += add_no_connect(45.72, 63.50)
    sch += add_no_connect(45.72, 66.04)
    # Pin 5: CC2 (py = 68.58)
    sch += add_wire(35.56, 68.58, 45.72, 68.58)
    sch += add_label("CC2", 35.56, 68.58, 180)
    # Pin 6: GND (py = 71.12)
    sch += add_wire(35.56, 71.12, 45.72, 71.12)
    sch += add_label("GND", 35.56, 71.12, 180)

    # CC1 & CC2 5.1k Pulldowns: Device:R at angle 90
    # Pin 1 at X - 3.81, Pin 2 at X + 3.81
    # R_CC1 at (73.66, 50.80, 90) -> Pin 1: (69.85, 50.80), Pin 2: (77.47, 50.80)
    sch += add_sym("Device:R", "R_CC1", "5.1k (CC1)", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 73.66, 50.80, 90)
    sch += add_wire(63.50, 50.80, 69.85, 50.80)
    sch += add_label("CC1", 63.50, 50.80, 180)
    sch += add_wire(77.47, 50.80, 83.82, 50.80)
    sch += add_label("GND", 83.82, 50.80, 0)

    # R_CC2 at (73.66, 68.58, 90) -> Pin 1: (69.85, 68.58), Pin 2: (77.47, 68.58)
    sch += add_sym("Device:R", "R_CC2", "5.1k (CC2)", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 73.66, 68.58, 90)
    sch += add_wire(63.50, 68.58, 69.85, 68.58)
    sch += add_label("CC2", 63.50, 68.58, 180)
    sch += add_wire(77.47, 68.58, 83.82, 68.58)
    sch += add_label("GND", 83.82, 68.58, 0)

    # SW_PWR (Conn_01x02) at (106.68, 58.42). Pins at X = 101.60.
    # Conn_01x02: Pin 1 at Y - 0 = 58.42, Pin 2 at Y - (-2.54) = 60.96
    sch += add_sym("Connector_Generic:Conn_01x02", "SW_PWR", "ON/OFF SWITCH", "Button_Switch_THT:SW_Slide_SPDT_Straight_CK_OS102011MS2Q", 106.68, 58.42)
    sch += add_wire(93.98, 58.42, 101.60, 58.42)
    sch += add_label("VBUS_RAW", 93.98, 58.42, 180)
    sch += add_wire(93.98, 60.96, 101.60, 60.96)
    sch += add_label("+5V", 93.98, 60.96, 180)

    # J_EXT_5V (Conn_01x02) at (106.68, 81.28). Pin 1 at 81.28, Pin 2 at 83.82
    sch += add_sym("Connector_Generic:Conn_01x02", "J_EXT_5V", "ALT 5V SCREW IN", "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal", 106.68, 81.28)
    sch += add_wire(93.98, 81.28, 101.60, 81.28)
    sch += add_label("+5V", 93.98, 81.28, 180)
    sch += add_wire(93.98, 83.82, 101.60, 83.82)
    sch += add_label("GND", 93.98, 83.82, 180)

    # R_PWR & LED_PWR (Green Power Indicator)
    # R_PWR at (121.92, 50.80, 90) -> Pin 1: (118.11, 50.80), Pin 2: (125.73, 50.80)
    # LED_PWR placed at (129.54, 50.80, 180) -> Pin 2 (Anode) is at 129.54 - 3.81 = 125.73 (direct pin contact!)
    # Pin 1 (Cathode) is at 129.54 + 3.81 = 133.35
    sch += add_sym("Device:R", "R_PWR", "1k", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 121.92, 50.80, 90)
    sch += add_wire(111.76, 50.80, 118.11, 50.80)
    sch += add_label("+5V", 111.76, 50.80, 180)
    sch += add_sym("Device:LED", "LED_PWR", "GREEN (PWR)", "LED_THT:LED_D3.0mm", 129.54, 50.80, 180)
    sch += add_wire(133.35, 50.80, 142.24, 50.80)
    sch += add_label("GND", 142.24, 50.80, 0)

    # J_OUT_5V (Conn_01x04) at (50.80, 109.22). Pins at X = 45.72
    # Conn_01x04 pin dys: [2.54, 0.0, -2.54, -5.08] -> py = y - dy
    sch += add_sym("Connector_Generic:Conn_01x04", "J_OUT_5V", "5V BUS (x4)", "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical", 50.80, 109.22)
    for dy in [2.54, 0.0, -2.54, -5.08]:
        py = 109.22 - dy
        sch += add_wire(35.56, py, 45.72, py)
        sch += add_label("+5V", 35.56, py, 180)

    # J_OUT_GND (Conn_01x06) at (106.68, 109.22). Pins at X = 101.60
    # Conn_01x06 pin dys: [5.08, 2.54, 0.0, -2.54, -5.08, -7.62] -> py = y - dy
    sch += add_sym("Connector_Generic:Conn_01x06", "J_OUT_GND", "GND BUS (x6)", "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical", 106.68, 109.22)
    for dy in [5.08, 2.54, 0.0, -2.54, -5.08, -7.62]:
        py = 109.22 - dy
        sch += add_wire(93.98, py, 101.60, py)
        sch += add_label("GND", 93.98, py, 180)

    sch += add_text("USB-C with 2x 5.1k CC pull-downs for 5V 3A negotiation.", 28.0, 134.0, 1.2, False)

    # -------------------------------------------------------------------------
    # BLOCK 2 (TOP-CENTER): SEEED STUDIO XIAO ESP32-S3 SENSE MCU CARRIER
    # Boundary: X: 155.0 to 275.0 mm, Y: 32.0 to 142.0 mm
    # -------------------------------------------------------------------------
    sch += add_box(155.0, 32.0, 275.0, 142.0)
    sch += add_text("2. SEEED STUDIO XIAO ESP32-S3 SENSE MCU", 158.0, 38.0, 1.9, True)

    # J_MCU_L (Conn_01x07) at (185.42, 81.28). Pins at X = 180.34
    # Conn_01x07 pin dys: [7.62, 5.08, 2.54, 0.0, -2.54, -5.08, -7.62] -> py = y - dy
    sch += add_sym("Connector_Generic:Conn_01x07", "J_MCU_L", "XIAO_LEFT (D0-D6)", "Connector_PinSocket_2.54mm:PinSocket_1x07_P2.54mm_Vertical", 185.42, 81.28)
    mcu_l_nets = ["TRIG_OUT", "ECHO_OUT", "TRIG_IN", "ECHO_IN", "BTN_CAL_OUT", "BTN_CAL_IN", "LED_CAL_OUT"]
    mcu_dys = [7.62, 5.08, 2.54, 0.0, -2.54, -5.08, -7.62]
    for net, dy in zip(mcu_l_nets, mcu_dys):
        py = 81.28 - dy
        sch += add_wire(167.64, py, 180.34, py)
        sch += add_label(net, 167.64, py, 180)

    # J_MCU_R (Conn_01x07) at (241.30, 81.28) angle 180. Pins at X = 241.30 + 5.08 = 246.38
    # When rotated 180, Pin 7 is at py = 81.28 - 7.62, Pin 6 at 81.28 - 5.08, ... Pin 1 at 81.28 + 7.62
    sch += add_sym("Connector_Generic:Conn_01x07", "J_MCU_R", "XIAO_RIGHT (D7-5V)", "Connector_PinSocket_2.54mm:PinSocket_1x07_P2.54mm_Vertical", 241.30, 81.28, 180)
    mcu_r_nets = ["LED_CAL_IN", "I2S_BCLK", "I2S_LRC", "I2S_DIN", "+3V3", "GND", "+5V"]
    for net, dy in zip(mcu_r_nets, mcu_dys):
        py = 81.28 - dy
        sch += add_wire(246.38, py, 259.08, py)
        sch += add_label(net, 259.08, py, 0)

    sch += add_text("Dual-Core 240MHz ESP32-S3 | 8MB PSRAM", 175.0, 118.0, 1.3, False)
    sch += add_text("Integrated OV2640 AI Camera Subsystem", 175.0, 124.0, 1.3, False)
    sch += add_text("Native USB-CDC Telemetry & Flashing", 177.0, 130.0, 1.3, False)

    # -------------------------------------------------------------------------
    # BLOCK 3 (TOP-RIGHT): I2S CLASS-D AUDIO AMPLIFIER (MAX98357A) & SPEAKER
    # Boundary: X: 285.0 to 408.0 mm, Y: 32.0 to 142.0 mm
    # -------------------------------------------------------------------------
    sch += add_box(285.0, 32.0, 408.0, 142.0)
    sch += add_text("3. I2S CLASS-D AUDIO AMPLIFIER (MAX98357A)", 288.0, 38.0, 1.9, True)

    # J_AMP at (325.12, 81.28). Pins at X = 320.04
    sch += add_sym("Connector_Generic:Conn_01x07", "J_AMP", "MAX98357A I2S AMP", "Connector_PinSocket_2.54mm:PinSocket_1x07_P2.54mm_Vertical", 325.12, 81.28)
    amp_nets = ["I2S_LRC", "I2S_BCLK", "I2S_DIN", "GND", "+5V", "GND", "+5V"]
    for net, dy in zip(amp_nets, mcu_dys):
        py = 81.28 - dy
        sch += add_wire(309.88, py, 320.04, py)
        sch += add_label(net, 309.88, py, 180)

    # J_AMP_OUT (Conn_01x02) at (355.60, 81.28) for the 2 speaker output pads of MAX98357A
    sch += add_sym("Connector_Generic:Conn_01x02", "J_AMP_OUT", "AMP_OUT PADS", "Connector_PinSocket_2.54mm:PinSocket_1x02_P2.54mm_Vertical", 355.60, 81.28)
    # J_SPK at (386.08, 81.28). Pins at X = 381.00
    sch += add_sym("Connector_Generic:Conn_01x02", "J_SPK", "8R SPEAKER SCREW", "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal", 386.08, 81.28)
    
    # Connect J_AMP_OUT (Pins at 350.52) directly to J_SPK (Pins at 381.00) with labels
    # Pin 1 at Y = 81.28, Pin 2 at Y = 81.28 - (-2.54) = 83.82
    sch += add_wire(350.52, 81.28, 381.00, 81.28)
    sch += add_label("SPK_POS", 365.76, 81.28, 0)
    sch += add_wire(350.52, 83.82, 381.00, 83.82)
    sch += add_label("SPK_NEG", 365.76, 83.82, 0)

    sch += add_text("3.2W Class-D Mono DAC/Amp", 335.0, 118.0, 1.3, False)
    sch += add_text("Direct Digital I2S Audio Bus (Zero Jitter)", 325.0, 124.0, 1.3, False)
    sch += add_text("2x M2.5 Standoff Mechanical Mounts", 335.0, 130.0, 1.3, False)

    # =========================================================================
    # ROW 2 (BOTTOM ROW): Y = 150.0 mm to Y = 265.0 mm
    # =========================================================================

    # -------------------------------------------------------------------------
    # BLOCK 4 (BOTTOM-LEFT): DUAL AJ-SR04M WATERPROOF ULTRASONIC DOCKS
    # Boundary: X: 25.0 to 160.0 mm, Y: 150.0 to 265.0 mm
    # -------------------------------------------------------------------------
    sch += add_box(25.0, 150.0, 160.0, 265.0)
    sch += add_text("4. DUAL AJ-SR04M SENSOR DOCKS (ZERO CABLE FRICTION)", 28.0, 156.0, 1.9, True)

    # J_AJ_OUT (Conn_01x04) at (66.04, 198.12). Pins at X = 60.96
    # Conn_01x04 pin dys: [2.54, 0.0, -2.54, -5.08] -> py = y - dy
    sch += add_sym("Connector_Generic:Conn_01x04", "J_AJ_OUT", "AJ-SR04M OUTSIDE (PAVEMENT)", "Connector_PinSocket_2.54mm:PinSocket_1x04_P2.54mm_Vertical", 66.04, 198.12)
    aj_out_nets = ["+5V", "TRIG_OUT", "ECHO_OUT", "GND"]
    aj_dys = [2.54, 0.0, -2.54, -5.08]
    for net, dy in zip(aj_out_nets, aj_dys):
        py = 198.12 - dy
        sch += add_wire(48.26, py, 60.96, py)
        sch += add_label(net, 48.26, py, 180)

    # J_AJ_IN (Conn_01x04) at (127.00, 198.12). Pins at X = 121.92
    sch += add_sym("Connector_Generic:Conn_01x04", "J_AJ_IN", "AJ-SR04M INSIDE (BIN DEPTH)", "Connector_PinSocket_2.54mm:PinSocket_1x04_P2.54mm_Vertical", 127.00, 198.12)
    aj_in_nets = ["+5V", "TRIG_IN", "ECHO_IN", "GND"]
    for net, dy in zip(aj_in_nets, aj_dys):
        py = 198.12 - dy
        sch += add_wire(109.22, py, 121.92, py)
        sch += add_label(net, 109.22, py, 180)

    sch += add_text("Each dock features 4x M2.5 mechanical standoffs.", 30.0, 230.0, 1.3, False)
    sch += add_text("Transducer jacks face left PCB edge directly into free air,", 30.0, 236.0, 1.3, False)
    sch += add_text("guaranteeing ZERO cable bending friction or crowding.", 30.0, 242.0, 1.3, False)

    # -------------------------------------------------------------------------
    # BLOCK 5 (BOTTOM-CENTER): SIZABLE 12x12mm CALIBRATION CONTROLS
    # Boundary: X: 170.0 to 295.0 mm, Y: 150.0 to 265.0 mm
    # -------------------------------------------------------------------------
    sch += add_box(170.0, 150.0, 295.0, 265.0)
    sch += add_text("5. SIZABLE 12x12mm CALIBRATION CONTROLS", 173.0, 156.0, 1.9, True)

    # SW_CAL_OUT at (195.58, 185.42). Pin 1 at X - 5.08 = 190.50, Pin 2 at X + 5.08 = 200.66
    sch += add_sym("Switch:SW_Push", "SW_CAL_OUT", "CAL_OUT (12x12mm)", "Button_Switch_THT:SW_PUSH-12mm", 195.58, 185.42)
    sch += add_wire(177.80, 185.42, 190.50, 185.42)
    sch += add_label("BTN_CAL_OUT", 177.80, 185.42, 180)
    sch += add_wire(200.66, 185.42, 208.28, 185.42)
    sch += add_label("GND", 208.28, 185.42, 0)

    # R_LED_OUT & LED_CAL_OUT at Y = 185.42
    # R_LED_OUT at (236.22, 185.42, 90) -> Pin 1: (232.41, 185.42), Pin 2: (240.03, 185.42)
    # LED_CAL_OUT at (243.84, 185.42, 180) -> Pin 2 (A) at (240.03, 185.42), Pin 1 (K) at (247.65, 185.42)
    sch += add_sym("Device:R", "R_LED_OUT", "1k", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 236.22, 185.42, 90)
    sch += add_wire(223.52, 185.42, 232.41, 185.42)
    sch += add_label("LED_CAL_OUT", 223.52, 185.42, 180)
    sch += add_sym("Device:LED", "LED_CAL_OUT", "BLUE (OUT_STAT)", "LED_THT:LED_D3.0mm", 243.84, 185.42, 180)
    sch += add_wire(247.65, 185.42, 259.08, 185.42)
    sch += add_label("GND", 259.08, 185.42, 0)

    # SW_CAL_IN at (195.58, 220.98)
    sch += add_sym("Switch:SW_Push", "SW_CAL_IN", "CAL_IN (12x12mm)", "Button_Switch_THT:SW_PUSH-12mm", 195.58, 220.98)
    sch += add_wire(177.80, 220.98, 190.50, 220.98)
    sch += add_label("BTN_CAL_IN", 177.80, 220.98, 180)
    sch += add_wire(200.66, 220.98, 208.28, 220.98)
    sch += add_label("GND", 208.28, 220.98, 0)

    # R_LED_IN & LED_CAL_IN at Y = 220.98
    sch += add_sym("Device:R", "R_LED_IN", "1k", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 236.22, 220.98, 90)
    sch += add_wire(223.52, 220.98, 232.41, 220.98)
    sch += add_label("LED_CAL_IN", 223.52, 220.98, 180)
    sch += add_sym("Device:LED", "LED_CAL_IN", "AMBER (IN_STAT)", "LED_THT:LED_D3.0mm", 243.84, 220.98, 180)
    sch += add_wire(247.65, 220.98, 259.08, 220.98)
    sch += add_label("GND", 259.08, 220.98, 0)

    sch += add_text("SW_CAL_OUT: 15-ping pavement reference distance calibration.", 175.0, 245.0, 1.2, False)
    sch += add_text("SW_CAL_IN: Dynamic container depth calibration (1m to 4m).", 175.0, 251.0, 1.2, False)

    # -------------------------------------------------------------------------
    # BLOCK 6 (BOTTOM-RIGHT): AUX EXPANSION & SPEC NOTES
    # Boundary: X: 305.0 to 408.0 mm, Y: 150.0 to 265.0 mm
    # -------------------------------------------------------------------------
    sch += add_box(305.0, 150.0, 408.0, 265.0)
    sch += add_text("6. AUX EXPANSION & SPEC NOTES", 308.0, 156.0, 1.9, True)

    # J_AUX (Conn_01x06) at (350.52, 198.12). Pins at X = 345.44
    # Conn_01x06 pin dys: [5.08, 2.54, 0.0, -2.54, -5.08, -7.62] -> py = y - dy
    sch += add_sym("Connector_Generic:Conn_01x06", "J_AUX", "AUX EXPANSION BUS", "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical", 350.52, 198.12)
    aux_nets = ["+3V3", "LED_CAL_OUT", "LED_CAL_IN", "BTN_CAL_OUT", "BTN_CAL_IN", "GND"]
    conn6_dys = [5.08, 2.54, 0.0, -2.54, -5.08, -7.62]
    for net, dy in zip(aux_nets, conn6_dys):
        py = 198.12 - dy
        sch += add_wire(335.28, py, 345.44, py)
        sch += add_label(net, 335.28, py, 180)

    sch += add_text("BOARD FABRICATION SPECIFICATION:", 310.0, 222.0, 1.3, True)
    sch += add_text("Dimensions: 135.0 mm x 95.0 mm", 310.0, 227.0, 1.2, False)
    sch += add_text("Layers: 2-Layer FR4 | 1.6 mm Thickness | 1 oz Cu", 310.0, 232.0, 1.2, False)
    sch += add_text("Mounting: 4x M3 Corner Standoffs (4.0 mm inset)", 310.0, 237.0, 1.2, False)
    sch += add_text("Module Docks: 10x M2.5 Standoff Mechanical Holes", 310.0, 242.0, 1.2, False)
    sch += add_text("Power Input: 5V DC via USB-C or Screw Terminal", 310.0, 247.0, 1.2, False)

    sch += """\t(sheet_instances
\t\t(path "/" (page "1"))
\t)
)"""

    with open(sch_file, "w", encoding="utf-8") as f:
        f.write(sch)

    print(f"SUCCESS: Generated perfectly centered, grid-aligned schematic at {sch_file}")

if __name__ == "__main__":
    build_perfect_schematic()
