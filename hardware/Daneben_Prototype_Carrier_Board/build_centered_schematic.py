import uuid
import os

def gen_uuid():
    return str(uuid.uuid4())

def build_centered_schematic():
    out_dir = "hardware/Daneben_Prototype_Carrier_Board"
    os.makedirs(out_dir, exist_ok=True)
    sch_file = os.path.join(out_dir, "Daneben_Prototype_Carrier_Board.kicad_sch")
    
    # Standard KiCad 9 library symbols:
    # Conn_01x02, Conn_01x04, Conn_01x06, Conn_01x07, Device:R, Device:LED, Switch:SW_Push
    sch = f"""(kicad_sch
	(version 20250114)
	(generator "eeschema")
	(generator_version "9.0")
	(uuid "{gen_uuid()}")
	(paper "A3")
	(title_block
		(title "Daneben! Prototype Carrier Board (Modular Showcase Edition v2.0)")
		(date "2026-10-26")
		(rev "v2.0")
		(company "Hochschule Niederrhein (HSNR) - Fachbereich Elektrotechnik & Informatik")
		(comment 1 "Modulares Traegerboard fuer Seeed Studio XIAO ESP32-S3 Sense")
		(comment 2 "Duales AJ-SR04M Docking, USB-C Power Entry, 12x12mm Kalibrierungstaster, I2S Audio")
	)
	(lib_symbols
		(symbol "Connector_Generic:Conn_01x02"
			(pin_names (offset 1.016))
			(in_bom yes) (on_board yes)
			(property "Reference" "J" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Conn_01x02" (at 0 -5.08 0) (effects (font (size 1.27 1.27))))
			(symbol "Conn_01x02_1_1"
				(rectangle (start -1.27 -2.54) (end 1.27 2.54) (stroke (width 0.254)) (fill (type background)))
				(pin passive line (at -5.08 1.27 0) (length 3.81) (name "Pin_1" (effects (font (size 1.27 1.27)))) (number "1"))
				(pin passive line (at -5.08 -1.27 0) (length 3.81) (name "Pin_2" (effects (font (size 1.27 1.27)))) (number "2"))
			)
		)
		(symbol "Connector_Generic:Conn_01x04"
			(pin_names (offset 1.016))
			(in_bom yes) (on_board yes)
			(property "Reference" "J" (at 0 5.08 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Conn_01x04" (at 0 -7.62 0) (effects (font (size 1.27 1.27))))
			(symbol "Conn_01x04_1_1"
				(rectangle (start -1.27 -5.08) (end 1.27 5.08) (stroke (width 0.254)) (fill (type background)))
				(pin passive line (at -5.08 3.81 0) (length 3.81) (name "Pin_1" (effects (font (size 1.27 1.27)))) (number "1"))
				(pin passive line (at -5.08 1.27 0) (length 3.81) (name "Pin_2" (effects (font (size 1.27 1.27)))) (number "2"))
				(pin passive line (at -5.08 -1.27 0) (length 3.81) (name "Pin_3" (effects (font (size 1.27 1.27)))) (number "3"))
				(pin passive line (at -5.08 -3.81 0) (length 3.81) (name "Pin_4" (effects (font (size 1.27 1.27)))) (number "4"))
			)
		)
		(symbol "Connector_Generic:Conn_01x06"
			(pin_names (offset 1.016))
			(in_bom yes) (on_board yes)
			(property "Reference" "J" (at 0 7.62 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Conn_01x06" (at 0 -10.16 0) (effects (font (size 1.27 1.27))))
			(symbol "Conn_01x06_1_1"
				(rectangle (start -1.27 -7.62) (end 1.27 7.62) (stroke (width 0.254)) (fill (type background)))
				(pin passive line (at -5.08 6.35 0) (length 3.81) (name "Pin_1" (effects (font (size 1.27 1.27)))) (number "1"))
				(pin passive line (at -5.08 3.81 0) (length 3.81) (name "Pin_2" (effects (font (size 1.27 1.27)))) (number "2"))
				(pin passive line (at -5.08 1.27 0) (length 3.81) (name "Pin_3" (effects (font (size 1.27 1.27)))) (number "3"))
				(pin passive line (at -5.08 -1.27 0) (length 3.81) (name "Pin_4" (effects (font (size 1.27 1.27)))) (number "4"))
				(pin passive line (at -5.08 -3.81 0) (length 3.81) (name "Pin_5" (effects (font (size 1.27 1.27)))) (number "5"))
				(pin passive line (at -5.08 -6.35 0) (length 3.81) (name "Pin_6" (effects (font (size 1.27 1.27)))) (number "6"))
			)
		)
		(symbol "Connector_Generic:Conn_01x07"
			(pin_names (offset 1.016))
			(in_bom yes) (on_board yes)
			(property "Reference" "J" (at 0 8.89 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Conn_01x07" (at 0 -11.43 0) (effects (font (size 1.27 1.27))))
			(symbol "Conn_01x07_1_1"
				(rectangle (start -1.27 -8.89) (end 1.27 8.89) (stroke (width 0.254)) (fill (type background)))
				(pin passive line (at -5.08 7.62 0) (length 3.81) (name "Pin_1" (effects (font (size 1.27 1.27)))) (number "1"))
				(pin passive line (at -5.08 5.08 0) (length 3.81) (name "Pin_2" (effects (font (size 1.27 1.27)))) (number "2"))
				(pin passive line (at -5.08 2.54 0) (length 3.81) (name "Pin_3" (effects (font (size 1.27 1.27)))) (number "3"))
				(pin passive line (at -5.08 0 0) (length 3.81) (name "Pin_4" (effects (font (size 1.27 1.27)))) (number "4"))
				(pin passive line (at -5.08 -2.54 0) (length 3.81) (name "Pin_5" (effects (font (size 1.27 1.27)))) (number "5"))
				(pin passive line (at -5.08 -5.08 0) (length 3.81) (name "Pin_6" (effects (font (size 1.27 1.27)))) (number "6"))
				(pin passive line (at -5.08 -7.62 0) (length 3.81) (name "Pin_7" (effects (font (size 1.27 1.27)))) (number "7"))
			)
		)
		(symbol "Device:R"
			(pin_names (offset 0))
			(in_bom yes) (on_board yes)
			(property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))
			(property "Value" "R" (at -2.032 0 90) (effects (font (size 1.27 1.27))))
			(symbol "R_1_1"
				(rectangle (start -1.016 -2.54) (end 1.016 2.54) (stroke (width 0.254)) (fill (type none)))
				(pin passive line (at 0 3.81 270) (length 1.27) (name "~") (number "1"))
				(pin passive line (at 0 -3.81 90) (length 1.27) (name "~") (number "2"))
			)
		)
		(symbol "Device:LED"
			(pin_names (offset 1.016))
			(in_bom yes) (on_board yes)
			(property "Reference" "D" (at 1.27 2.54 0) (effects (font (size 1.27 1.27))))
			(property "Value" "LED" (at 1.27 -2.54 0) (effects (font (size 1.27 1.27))))
			(symbol "LED_1_1"
				(polyline (pts (xy -1.27 -1.27) (xy -1.27 1.27) (xy 1.27 0) (xy -1.27 -1.27)) (stroke (width 0.254)) (fill (type background)))
				(polyline (pts (xy 1.27 -1.27) (xy 1.27 1.27)) (stroke (width 0.254)))
				(pin passive line (at -3.81 0 0) (length 2.54) (name "A") (number "2"))
				(pin passive line (at 3.81 0 180) (length 2.54) (name "K") (number "1"))
			)
		)
		(symbol "Switch:SW_Push"
			(pin_names (offset 1.016))
			(in_bom yes) (on_board yes)
			(property "Reference" "SW" (at 0 2.54 0) (effects (font (size 1.27 1.27))))
			(property "Value" "SW_Push" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))
			(symbol "SW_Push_1_1"
				(circle (center -2.032 0) (radius 0.508) (stroke (width 0.254)))
				(circle (center 2.032 0) (radius 0.508) (stroke (width 0.254)))
				(polyline (pts (xy -2.54 1.27) (xy 2.54 1.27)) (stroke (width 0.254)))
				(polyline (pts (xy 0 1.27) (xy 0 3.048)) (stroke (width 0.254)))
				(pin passive line (at -5.08 0 0) (length 2.54) (name "1") (number "1"))
				(pin passive line (at 5.08 0 180) (length 2.54) (name "2") (number "2"))
			)
		)
	)
"""

    def add_sym(lib_id, ref, val, fp, x, y, angle=0):
        return f"""	(symbol
		(lib_id "{lib_id}")
		(at {x} {y} {angle})
		(unit 1)
		(in_bom yes) (on_board yes)
		(uuid "{gen_uuid()}")
		(property "Reference" "{ref}" (at {x} {y-4.5} 0) (effects (font (size 1.27 1.27))))
		(property "Value" "{val}" (at {x} {y+4.5} 0) (effects (font (size 1.27 1.27))))
		(property "Footprint" "{fp}" (at {x} {y} 0) (effects (font (size 1.27 1.27)) (hide yes)))
	)
"""

    def add_label(name, x, y, angle=0):
        return f"""	(label "{name}"
		(at {x} {y} {angle})
		(effects (font (size 1.27 1.27)))
		(uuid "{gen_uuid()}")
	)
"""

    def add_text(txt, x, y, size=2.0, bold=True):
        b = "yes" if bold else "no"
        return f"""	(text "{txt}"
		(at {x} {y} 0)
		(effects (font (size {size} {size}) (bold {b})))
		(uuid "{gen_uuid()}")
	)
"""

    def add_wire(x1, y1, x2, y2):
        return f"""	(wire
		(pts (xy {x1} {y1}) (xy {x2} {y2}))
		(stroke (width 0) (type default))
		(uuid "{gen_uuid()}")
	)
"""

    def add_box(x1, y1, x2, y2):
        return f"""	(polyline
		(pts (xy {x1} {y1}) (xy {x2} {y1}) (xy {x2} {y2}) (xy {x1} {y2}) (xy {x1} {y1}))
		(stroke (width 0.3) (type dash))
		(uuid "{gen_uuid()}")
	)
"""

    # =========================================================================
    # SHEET HEADER (CENTERED AT TOP)
    # A3 Sheet is 420mm x 297mm. Center X = 210mm.
    # =========================================================================
    sch += add_text("DANEBEN! SMART WASTE TELEMATICS — MODULAR CARRIER BOARD v2.0", 210, 16, 3.2, True)
    sch += add_text("Hochschule Niederrhein (HSNR) · 5. Semester · Mikrocontroller · Master Electrical Schematic", 210, 22, 1.8, False)

    # =========================================================================
    # ROW 1 (TOP ROW): Y = 30 mm to Y = 138 mm
    # =========================================================================

    # -------------------------------------------------------------------------
    # BLOCK 1 (TOP-LEFT): DEDICATED USB-C POWER ENTRY & POWER DISTRIBUTION
    # Boundary: X: 25 to 142 mm, Y: 30 to 138 mm
    # -------------------------------------------------------------------------
    sch += add_box(25, 30, 142, 138)
    sch += add_text("BLOCK 1: DEDICATED USB-C POWER ENTRY & DISTRIBUTION", 28, 36, 1.9, True)

    # USB-C Connector (J_USBC)
    sch += add_sym("Connector_Generic:Conn_01x06", "J_USBC", "USB-C (5V/3A)", "Connector_USB:USB_C_Receptacle_HRO_TYPE-C-31-M-12", 50, 60)
    sch += add_label("VBUS_RAW", 40, 60 - 6.35, 180)
    sch += add_label("CC1", 40, 60 - 3.81, 180)
    sch += add_label("CC2", 40, 60 - 1.27, 180)
    sch += add_label("NC", 40, 60 + 1.27, 180)
    sch += add_label("NC", 40, 60 + 3.81, 180)
    sch += add_label("GND", 40, 60 + 6.35, 180)

    # 5.1k CC1 Pull-Down Resistor
    sch += add_sym("Device:R", "R_CC1", "5.1k (CC1)", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 74, 52, 90)
    sch += add_label("CC1", 66, 52, 180)
    sch += add_wire(66, 52, 70.19, 52)
    sch += add_label("GND", 82, 52, 0)
    sch += add_wire(77.81, 52, 82, 52)

    # 5.1k CC2 Pull-Down Resistor
    sch += add_sym("Device:R", "R_CC2", "5.1k (CC2)", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 74, 66, 90)
    sch += add_label("CC2", 66, 66, 180)
    sch += add_wire(66, 66, 70.19, 66)
    sch += add_label("GND", 82, 66, 0)
    sch += add_wire(77.81, 66, 82, 66)

    # Power Slide Switch (SW_PWR)
    sch += add_sym("Connector_Generic:Conn_01x02", "SW_PWR", "ON/OFF SWITCH", "Button_Switch_THT:SW_Slide_SPDT_Straight_CK_OS102011MS2Q", 104, 58)
    sch += add_label("VBUS_RAW", 94, 58 - 1.27, 180)
    sch += add_label("+5V", 94, 58 + 1.27, 180)

    # Bulk Capacitor C_BULK1 (100uF) & Power Indicator LED (LED_PWR)
    sch += add_sym("Device:R", "R_PWR", "1k", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 128, 52)
    sch += add_label("+5V", 128, 45, 90)
    sch += add_wire(128, 45, 128, 48.19)
    sch += add_sym("Device:LED", "LED_PWR", "GREEN (PWR)", "LED_THT:LED_D3.0mm", 128, 64, 90)
    sch += add_wire(128, 55.81, 128, 60.19)
    sch += add_label("GND", 128, 70, 270)
    sch += add_wire(128, 67.81, 128, 70)

    # Alternate Screw Terminal 5V (J_EXT_5V)
    sch += add_sym("Connector_Generic:Conn_01x02", "J_EXT_5V", "ALT 5V SCREW IN", "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal", 104, 80)
    sch += add_label("+5V", 94, 80 - 1.27, 180)
    sch += add_label("GND", 94, 80 + 1.27, 180)

    # 5V Power Distribution Bus (J_OUT_5V)
    sch += add_sym("Connector_Generic:Conn_01x04", "J_OUT_5V", "5V BUS OUT (x4)", "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical", 50, 108)
    for i, dy in enumerate([3.81, 1.27, -1.27, -3.81]):
        sch += add_label("+5V", 40, 108 - dy, 180)

    # GND Distribution Bus (J_OUT_GND)
    sch += add_sym("Connector_Generic:Conn_01x06", "J_OUT_GND", "GND BUS (x6)", "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical", 104, 108)
    for i, dy in enumerate([6.35, 3.81, 1.27, -1.27, -3.81, -6.35]):
        sch += add_label("GND", 94, 108 - dy, 180)

    # -------------------------------------------------------------------------
    # BLOCK 2 (TOP-CENTER): SEEED STUDIO XIAO ESP32-S3 SENSE CARRIER
    # Boundary: X: 152 to 275 mm, Y: 30 to 138 mm
    # -------------------------------------------------------------------------
    sch += add_box(152, 30, 275, 138)
    sch += add_text("BLOCK 2: SEEED STUDIO XIAO ESP32-S3 SENSE MCU", 155, 36, 1.9, True)

    # Left Row (J_MCU_L)
    sch += add_sym("Connector_Generic:Conn_01x07", "J_MCU_L", "XIAO_LEFT (D0-D6)", "Connector_PinSocket_2.54mm:PinSocket_1x07_P2.54mm_Vertical", 182, 80)
    mcu_l_nets = ["TRIG_OUT", "ECHO_OUT", "TRIG_IN", "ECHO_IN", "BTN_CAL_OUT", "BTN_CAL_IN", "LED_CAL_OUT"]
    for i, dy in enumerate([7.62, 5.08, 2.54, 0, -2.54, -5.08, -7.62]):
        sch += add_label(mcu_l_nets[i], 168, 80 - dy, 180)
        sch += add_wire(168, 80 - dy, 176.92, 80 - dy)

    # Right Row (J_MCU_R)
    sch += add_sym("Connector_Generic:Conn_01x07", "J_MCU_R", "XIAO_RIGHT (D7-5V)", "Connector_PinSocket_2.54mm:PinSocket_1x07_P2.54mm_Vertical", 242, 80, 180)
    mcu_r_nets = ["LED_CAL_IN", "I2S_BCLK", "I2S_LRC", "I2S_DIN", "+3V3", "GND", "+5V"]
    for i, dy in enumerate([7.62, 5.08, 2.54, 0, -2.54, -5.08, -7.62]):
        sch += add_label(mcu_r_nets[i], 256, 80 - dy, 0)
        sch += add_wire(247.08, 80 - dy, 256, 80 - dy)

    # Text description inside MCU block
    sch += add_text("Dual-Core 240MHz ESP32-S3 | 8MB PSRAM", 175, 118, 1.3, False)
    sch += add_text("Top-mounted OV2640 AI Camera Subsystem", 173, 124, 1.3, False)
    sch += add_text("Native USB-CDC for Telemetry & Flashing", 175, 130, 1.3, False)

    # -------------------------------------------------------------------------
    # BLOCK 3 (TOP-RIGHT): MAX98357A I2S AUDIO AMPLIFIER & SPEAKER
    # Boundary: X: 285 to 408 mm, Y: 30 to 138 mm
    # -------------------------------------------------------------------------
    sch += add_box(285, 30, 408, 138)
    sch += add_text("BLOCK 3: I2S AUDIO AMPLIFIER & SPEAKER", 288, 36, 1.9, True)

    # MAX98357A Socket (J_AMP)
    sch += add_sym("Connector_Generic:Conn_01x07", "J_AMP", "MAX98357A I2S AMP", "Connector_PinSocket_2.54mm:PinSocket_1x07_P2.54mm_Vertical", 325, 78)
    amp_nets = ["I2S_LRC", "I2S_BCLK", "I2S_DIN", "GND", "NC", "GND", "+5V"]
    for i, dy in enumerate([7.62, 5.08, 2.54, 0, -2.54, -5.08, -7.62]):
        sch += add_label(amp_nets[i], 312, 78 - dy, 180)
        sch += add_wire(312, 78 - dy, 319.92, 78 - dy)

    # Speaker Screw Terminal (J_SPK)
    sch += add_sym("Connector_Generic:Conn_01x02", "J_SPK", "8R SPEAKER SCREW", "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal", 380, 70)
    sch += add_label("SPK_POS", 368, 70 - 1.27, 180)
    sch += add_wire(368, 70 - 1.27, 374.92, 70 - 1.27)
    sch += add_label("SPK_NEG", 368, 70 + 1.27, 180)
    sch += add_wire(368, 70 + 1.27, 374.92, 70 + 1.27)

    sch += add_text("3.2W Class-D Mono DAC/Amp", 335, 118, 1.3, False)
    sch += add_text("Direct Digital I2S Audio Bus (No DAC jitter)", 325, 124, 1.3, False)
    sch += add_text("2x M2.5 Rigid Standoff Mounts", 340, 130, 1.3, False)

    # =========================================================================
    # ROW 2 (BOTTOM ROW): Y = 148 mm to Y = 265 mm
    # =========================================================================

    # -------------------------------------------------------------------------
    # BLOCK 4 (BOTTOM-LEFT): DUAL AJ-SR04M WATERPROOF ULTRASONIC DOCKS
    # Boundary: X: 25 to 160 mm, Y: 148 to 265 mm
    # -------------------------------------------------------------------------
    sch += add_box(25, 148, 160, 265)
    sch += add_text("BLOCK 4: DUAL AJ-SR04M SENSOR DOCKS (ZERO CABLE FRICTION)", 28, 154, 1.9, True)

    # Outside Sensor Dock (J_AJ_OUT)
    sch += add_sym("Connector_Generic:Conn_01x04", "J_AJ_OUT", "AJ-SR04M OUTSIDE (PAVEMENT)", "Connector_PinSocket_2.54mm:PinSocket_1x04_P2.54mm_Vertical", 65, 190)
    sch += add_label("+5V", 52, 190 - 3.81, 180)
    sch += add_wire(52, 190 - 3.81, 59.92, 190 - 3.81)
    sch += add_label("TRIG_OUT", 52, 190 - 1.27, 180)
    sch += add_wire(52, 190 - 1.27, 59.92, 190 - 1.27)
    sch += add_label("ECHO_OUT", 52, 190 + 1.27, 180)
    sch += add_wire(52, 190 + 1.27, 59.92, 190 + 1.27)
    sch += add_label("GND", 52, 190 + 3.81, 180)
    sch += add_wire(52, 190 + 3.81, 59.92, 190 + 3.81)

    # Inside Sensor Dock (J_AJ_IN)
    sch += add_sym("Connector_Generic:Conn_01x04", "J_AJ_IN", "AJ-SR04M INSIDE (BIN DEPTH)", "Connector_PinSocket_2.54mm:PinSocket_1x04_P2.54mm_Vertical", 125, 190)
    sch += add_label("+5V", 112, 190 - 3.81, 180)
    sch += add_wire(112, 190 - 3.81, 119.92, 190 - 3.81)
    sch += add_label("TRIG_IN", 112, 190 - 1.27, 180)
    sch += add_wire(112, 190 - 1.27, 119.92, 190 - 1.27)
    sch += add_label("ECHO_IN", 112, 190 + 1.27, 180)
    sch += add_wire(112, 190 + 1.27, 119.92, 190 + 1.27)
    sch += add_label("GND", 112, 190 + 3.81, 180)
    sch += add_wire(112, 190 + 3.81, 119.92, 190 + 3.81)

    sch += add_text("Each dock features 4x M2.5 mechanical standoffs.", 30, 230, 1.3, False)
    sch += add_text("Transducer jacks face left PCB edge directly into free air,", 30, 236, 1.3, False)
    sch += add_text("guaranteeing ZERO cable bending friction or crowding.", 30, 242, 1.3, False)

    # -------------------------------------------------------------------------
    # BLOCK 5 (BOTTOM-CENTER): SIZABLE 12x12mm CALIBRATION CONTROLS
    # Boundary: X: 170 to 295 mm, Y: 148 to 265 mm
    # -------------------------------------------------------------------------
    sch += add_box(170, 148, 295, 265)
    sch += add_text("BLOCK 5: SIZABLE CALIBRATION CONTROLS", 173, 154, 1.9, True)

    # Outside Calibration Button (SW_CAL_OUT) & LED (LED_CAL_OUT)
    sch += add_sym("Switch:SW_Push", "SW_CAL_OUT", "CAL_OUT (12x12mm)", "Button_Switch_THT:SW_PUSH-12mm", 195, 185)
    sch += add_label("BTN_CAL_OUT", 182, 185, 180)
    sch += add_wire(182, 185, 189.92, 185)
    sch += add_label("GND", 208, 185, 0)
    sch += add_wire(200.08, 185, 208, 185)

    sch += add_sym("Device:R", "R_LED_OUT", "1k", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 240, 185, 90)
    sch += add_label("LED_CAL_OUT", 228, 185, 180)
    sch += add_wire(228, 185, 236.19, 185)
    sch += add_sym("Device:LED", "LED_CAL_OUT", "BLUE (OUT_STAT)", "LED_THT:LED_D3.0mm", 260, 185, 90)
    sch += add_wire(243.81, 185, 256.19, 185)
    sch += add_label("GND", 274, 185, 0)
    sch += add_wire(263.81, 185, 274, 185)

    # Inside Calibration Button (SW_CAL_IN) & LED (LED_CAL_IN)
    sch += add_sym("Switch:SW_Push", "SW_CAL_IN", "CAL_IN (12x12mm)", "Button_Switch_THT:SW_PUSH-12mm", 195, 215)
    sch += add_label("BTN_CAL_IN", 182, 215, 180)
    sch += add_wire(182, 215, 189.92, 215)
    sch += add_label("GND", 208, 215, 0)
    sch += add_wire(200.08, 215, 208, 215)

    sch += add_sym("Device:R", "R_LED_IN", "1k", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 240, 215, 90)
    sch += add_label("LED_CAL_IN", 228, 215, 180)
    sch += add_wire(228, 215, 236.19, 215)
    sch += add_sym("Device:LED", "LED_CAL_IN", "AMBER (IN_STAT)", "LED_THT:LED_D3.0mm", 260, 215, 90)
    sch += add_wire(243.81, 215, 256.19, 215)
    sch += add_label("GND", 274, 215, 0)
    sch += add_wire(263.81, 215, 274, 215)

    sch += add_text("SW_CAL_OUT: 15-ping pavement distance reference calibration.", 175, 245, 1.2, False)
    sch += add_text("SW_CAL_IN: Dynamic container depth calibration (1m to 4m).", 175, 251, 1.2, False)

    # -------------------------------------------------------------------------
    # BLOCK 6 (BOTTOM-RIGHT): AUXILIARY EXPANSION BUS & HARDWARE SPEC
    # Boundary: X: 305 to 408 mm, Y: 148 to 265 mm
    # -------------------------------------------------------------------------
    sch += add_box(305, 148, 408, 265)
    sch += add_text("BLOCK 6: AUX EXPANSION & CHASSIS", 308, 154, 1.9, True)

    sch += add_sym("Connector_Generic:Conn_01x06", "J_AUX", "AUX EXPANSION BUS", "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical", 345, 195)
    aux_nets = ["+3V3", "LED_CAL_OUT", "LED_CAL_IN", "BTN_CAL_OUT", "BTN_CAL_IN", "GND"]
    for i, dy in enumerate([6.35, 3.81, 1.27, -1.27, -3.81, -6.35]):
        sch += add_label(aux_nets[i], 330, 195 - dy, 180)
        sch += add_wire(330, 195 - dy, 339.92, 195 - dy)

    sch += add_text("4x M3 Corner Mounting Holes", 315, 232, 1.3, False)
    sch += add_text("Board Size: 130.0 mm x 90.0 mm", 315, 238, 1.3, False)
    sch += add_text("FR4 2-Layer 1.6mm / 1oz Copper", 315, 244, 1.3, False)

    sch += """\t(sheet_instances
		(path "/"
			(page "1")
		)
	)
)
"""
    with open(sch_file, "w", encoding="utf-8") as f:
        f.write(sch)
    print("SUCCESS: Generated centered v2 schematic at", sch_file)

if __name__ == "__main__":
    build_centered_schematic()
