import uuid
import os

def gen_uuid():
    return str(uuid.uuid4())

def build_v2_schematic():
    out_dir = "hardware/Daneben_Prototype_Carrier_Board"
    os.makedirs(out_dir, exist_ok=True)
    sch_file = os.path.join(out_dir, "Daneben_Prototype_Carrier_Board.kicad_sch")
    
    sch = f"""(kicad_sch
	(version 20250114)
	(generator "eeschema")
	(generator_version "9.0")
	(uuid "{gen_uuid()}")
	(paper "A3")
	(title_block
		(title "Daneben! Prototype Carrier Board (Modular Showcase Edition v2.0)")
		(date "2026-10-22")
		(rev "v2.0")
		(company "Hochschule Niederrhein (HSNR) - Mikrocontroller")
		(comment 1 "Master Modular Carrier Board: Dual AJ-SR04M Docks + Sizable Calibration Controls")
		(comment 2 "Dedicated USB-C Power Entry, MAX98357A I2S Audio, Full Mechanical Clearance")
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
		(property "Reference" "{ref}" (at {x} {y-4.0} 0) (effects (font (size 1.27 1.27))))
		(property "Value" "{val}" (at {x} {y+4.0} 0) (effects (font (size 1.27 1.27))))
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

    def add_text(txt, x, y, size=2.0):
        return f"""	(text "{txt}"
		(at {x} {y} 0)
		(effects (font (size {size} {size}) (bold yes)))
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

    # Section 1: Titles
    sch += add_text("DANEBEN! PROTOTYPE CARRIER BOARD (MODULAR SHOWCASE v2.0)", 30, 20, 3.2)
    sch += add_text("Hochschule Niederrhein - Mikrocontroller (5. Semester) - Dual AJ-SR04M & Sizable Calibration", 30, 28, 1.8)

    # 1. DEDICATED USB-C POWER ENTRY & DISTRIBUTION
    sch += add_text("1. DEDICATED USB-C POWER ENTRY & DISTRIBUTION", 30, 42, 2.2)
    # USB-C Connector (Conn_01x06)
    sch += add_sym("Connector_Generic:Conn_01x06", "J_USBC", "USB_C_PWR_5V", "Connector_USB:USB_C_Receptacle_HRO_TYPE-C-31-M-12", 45, 60)
    sch += add_label("VBUS_RAW", 35, 60 - 6.35, 180)
    sch += add_label("CC1", 35, 60 - 3.81, 180)
    sch += add_label("CC2", 35, 60 - 1.27, 180)
    sch += add_label("NC", 35, 60 + 1.27, 180)
    sch += add_label("NC", 35, 60 + 3.81, 180)
    sch += add_label("GND", 35, 60 + 6.35, 180)

    # 5.1k Pull-downs for USB-C PD negotiation
    sch += add_sym("Device:R", "R_CC1", "5.1k", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 65, 55, 90)
    sch += add_label("CC1", 58, 55, 180)
    sch += add_wire(58, 55, 61.19, 55)
    sch += add_label("GND", 72, 55, 0)
    sch += add_wire(68.81, 55, 72, 55)

    sch += add_sym("Device:R", "R_CC2", "5.1k", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 65, 65, 90)
    sch += add_label("CC2", 58, 65, 180)
    sch += add_wire(58, 65, 61.19, 65)
    sch += add_label("GND", 72, 65, 0)
    sch += add_wire(68.81, 65, 72, 65)

    # Power Switch
    sch += add_sym("Connector_Generic:Conn_01x02", "SW_PWR", "PWR_SWITCH", "Button_Switch_THT:SW_Slide_SPDT_Straight_CK_OS102011MS2Q", 90, 60)
    sch += add_label("VBUS_RAW", 80, 58.73, 180)
    sch += add_label("+5V", 80, 61.27, 180)

    # Power Indicator LED
    sch += add_sym("Device:R", "R_PWR", "1k", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 115, 55)
    sch += add_label("+5V", 115, 48, 90)
    sch += add_wire(115, 48, 115, 51.19)
    sch += add_sym("Device:LED", "LED_PWR", "GREEN_PWR", "LED_THT:LED_D3.0mm", 115, 67, 90)
    sch += add_wire(115, 58.81, 115, 63.19)
    sch += add_label("GND", 115, 73, 270)
    sch += add_wire(115, 70.81, 115, 73)

    # Alternate Screw Terminal 5V
    sch += add_sym("Connector_Generic:Conn_01x02", "J_EXT_5V", "ALT_5V_SCREW", "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal", 90, 80)
    sch += add_label("+5V", 80, 78.73, 180)
    sch += add_label("GND", 80, 81.27, 180)

    # 5V and GND Power Outlets
    sch += add_sym("Connector_Generic:Conn_01x04", "J_OUT_5V", "5V_BUS_x4", "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical", 45, 95)
    for i, dy in enumerate([3.81, 1.27, -1.27, -3.81]):
        sch += add_label("+5V", 35, 95 - dy, 180)

    sch += add_sym("Connector_Generic:Conn_01x06", "J_OUT_GND", "GND_BUS_x6", "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical", 85, 95)
    for i, dy in enumerate([6.35, 3.81, 1.27, -1.27, -3.81, -6.35]):
        sch += add_label("GND", 75, 95 - dy, 180)

    # 2. SEEED STUDIO XIAO ESP32-S3 SENSE CARRIER
    sch += add_text("2. SEEED STUDIO XIAO ESP32-S3 SENSE CARRIER", 150, 42, 2.2)
    sch += add_sym("Connector_Generic:Conn_01x07", "J_MCU_L", "XIAO_LEFT_PINS", "Connector_PinSocket_2.54mm:PinSocket_1x07_P2.54mm_Vertical", 170, 75)
    mcu_l_nets = ["TRIG_OUT", "ECHO_OUT", "TRIG_IN", "ECHO_IN", "BTN_CAL_OUT", "BTN_CAL_IN", "LED_CAL_OUT"]
    for i, dy in enumerate([7.62, 5.08, 2.54, 0, -2.54, -5.08, -7.62]):
        sch += add_label(mcu_l_nets[i], 160, 75 - dy, 180)

    sch += add_sym("Connector_Generic:Conn_01x07", "J_MCU_R", "XIAO_RIGHT_PINS", "Connector_PinSocket_2.54mm:PinSocket_1x07_P2.54mm_Vertical", 215, 75, 180)
    mcu_r_nets = ["LED_CAL_IN", "I2S_BCLK", "I2S_LRC", "I2S_DIN", "+3V3", "GND", "+5V"]
    for i, dy in enumerate([7.62, 5.08, 2.54, 0, -2.54, -5.08, -7.62]):
        sch += add_label(mcu_r_nets[i], 225, 75 - dy, 0)

    # 3. DUAL AJ-SR04M WATERPROOF ULTRASONIC DOCKS
    sch += add_text("3. AJ-SR04M WATERPROOF ULTRASONIC SENSOR DOCKS (ZERO CABLE FRICTION)", 30, 130, 2.2)
    # Outside Sensor Dock (Pavement / Floor)
    sch += add_sym("Connector_Generic:Conn_01x04", "J_AJ_OUT", "AJ-SR04M_OUTSIDE_DOCK", "Connector_PinSocket_2.54mm:PinSocket_1x04_P2.54mm_Vertical", 50, 150)
    sch += add_label("+5V", 40, 150 - 3.81, 180)
    sch += add_label("TRIG_OUT", 40, 150 - 1.27, 180)
    sch += add_label("ECHO_OUT", 40, 150 + 1.27, 180)
    sch += add_label("GND", 40, 150 + 3.81, 180)

    # Inside Sensor Dock (Bin Depth / Fill Level)
    sch += add_sym("Connector_Generic:Conn_01x04", "J_AJ_IN", "AJ-SR04M_INSIDE_DOCK", "Connector_PinSocket_2.54mm:PinSocket_1x04_P2.54mm_Vertical", 100, 150)
    sch += add_label("+5V", 90, 150 - 3.81, 180)
    sch += add_label("TRIG_IN", 90, 150 - 1.27, 180)
    sch += add_label("ECHO_IN", 90, 150 + 1.27, 180)
    sch += add_label("GND", 90, 150 + 3.81, 180)

    # 4. SIZABLE DUAL CALIBRATION BUTTONS & STATUS LEDS
    sch += add_text("4. SIZABLE 12x12mm CALIBRATION CONTROLS (OUTSIDE & INSIDE)", 150, 130, 2.2)
    # Outside Calibration Button (SW_CAL_OUT)
    sch += add_sym("Switch:SW_Push", "SW_CAL_OUT", "CAL_OUTSIDE_12x12", "Button_Switch_THT:SW_PUSH-12mm", 170, 150)
    sch += add_label("BTN_CAL_OUT", 160, 150, 180)
    sch += add_wire(160, 150, 164.92, 150)
    sch += add_label("GND", 180, 150, 0)
    sch += add_wire(175.08, 150, 180, 150)

    # Outside Calibration Status LED
    sch += add_sym("Device:R", "R_LED_OUT", "1k", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 205, 150, 90)
    sch += add_label("LED_CAL_OUT", 195, 150, 180)
    sch += add_wire(195, 150, 201.19, 150)
    sch += add_sym("Device:LED", "LED_CAL_OUT", "BLUE_OUT_STAT", "LED_THT:LED_D3.0mm", 220, 150, 90)
    sch += add_wire(208.81, 150, 216.19, 150)
    sch += add_label("GND", 230, 150, 0)
    sch += add_wire(223.81, 150, 230, 150)

    # Inside Calibration Button (SW_CAL_IN)
    sch += add_sym("Switch:SW_Push", "SW_CAL_IN", "CAL_INSIDE_12x12", "Button_Switch_THT:SW_PUSH-12mm", 170, 175)
    sch += add_label("BTN_CAL_IN", 160, 175, 180)
    sch += add_wire(160, 175, 164.92, 175)
    sch += add_label("GND", 180, 175, 0)
    sch += add_wire(175.08, 175, 180, 175)

    # Inside Calibration Status LED
    sch += add_sym("Device:R", "R_LED_IN", "1k", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 205, 175, 90)
    sch += add_label("LED_CAL_IN", 195, 175, 180)
    sch += add_wire(195, 175, 201.19, 175)
    sch += add_sym("Device:LED", "LED_CAL_IN", "AMBER_IN_STAT", "LED_THT:LED_D3.0mm", 220, 175, 90)
    sch += add_wire(208.81, 175, 216.19, 175)
    sch += add_label("GND", 230, 175, 0)
    sch += add_wire(223.81, 175, 230, 175)

    # 5. MAX98357A I2S AUDIO AMPLIFIER & SPEAKER
    sch += add_text("5. I2S CLASS-D AUDIO AMPLIFIER (MAX98357A) & SPEAKER", 260, 42, 2.2)
    sch += add_sym("Connector_Generic:Conn_01x07", "J_AMP", "MAX98357A_HEADER", "Connector_PinSocket_2.54mm:PinSocket_1x07_P2.54mm_Vertical", 280, 75)
    amp_nets = ["I2S_LRC", "I2S_BCLK", "I2S_DIN", "GND", "NC", "GND", "+5V"]
    for i, dy in enumerate([7.62, 5.08, 2.54, 0, -2.54, -5.08, -7.62]):
        sch += add_label(amp_nets[i], 270, 75 - dy, 180)

    # Speaker Terminals
    sch += add_sym("Connector_Generic:Conn_01x02", "J_SPK", "8R_SPEAKER_SCREW", "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal", 340, 60)
    sch += add_label("SPK_POS", 330, 58.73, 180)
    sch += add_label("SPK_NEG", 330, 61.27, 180)

    # 6. MODULAR EXPANSION BUS
    sch += add_text("6. MODULAR EXPANSION BUS", 260, 130, 2.2)
    sch += add_sym("Connector_Generic:Conn_01x06", "J_AUX", "AUX_EXPANSION", "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical", 280, 155)
    aux_nets = ["+3V3", "LED_CAL_OUT", "LED_CAL_IN", "BTN_CAL_OUT", "BTN_CAL_IN", "GND"]
    for i, dy in enumerate([6.35, 3.81, 1.27, -1.27, -3.81, -6.35]):
        sch += add_label(aux_nets[i], 270, 155 - dy, 180)

    sch += """\t(sheet_instances
		(path "/"
			(page "1")
		)
	)
)
"""
    with open(sch_file, "w", encoding="utf-8") as f:
        f.write(sch)
    print("SUCCESS: Generated complete v2 schematic at", sch_file)

if __name__ == "__main__":
    build_v2_schematic()
