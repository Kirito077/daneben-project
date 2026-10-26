import uuid
import os

def gen_uuid():
    return str(uuid.uuid4())

def build_complete_schematic():
    out_dir = "hardware/Daneben_Prototype_Carrier_Board"
    os.makedirs(out_dir, exist_ok=True)
    sch_file = os.path.join(out_dir, "Daneben_Prototype_Carrier_Board.kicad_sch")
    
    # Symbols library definitions:
    # Conn_01x02, Conn_01x04, Conn_01x06, Conn_01x07, Conn_01x08, Device:R, Device:LED, Switch:SW_Push
    
    sch = f"""(kicad_sch
	(version 20250114)
	(generator "eeschema")
	(generator_version "9.0")
	(uuid "{gen_uuid()}")
	(paper "A3")
	(title_block
		(title "Daneben! Prototype Carrier Board (Modular Showcase Edition)")
		(date "2026-10-22")
		(rev "v1.1")
		(company "Hochschule Niederrhein (HSNR) - Mikrocontroller")
		(comment 1 "Master Modular Carrier Board for Seeed Studio XIAO ESP32-S3 Sense")
		(comment 2 "Includes Power Bus, Dual Ultrasonic Level Shifters, I2S Audio Amp & Expansion")
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
		(symbol "Connector_Generic:Conn_01x08"
			(pin_names (offset 1.016))
			(in_bom yes) (on_board yes)
			(property "Reference" "J" (at 0 10.16 0) (effects (font (size 1.27 1.27))))
			(property "Value" "Conn_01x08" (at 0 -12.7 0) (effects (font (size 1.27 1.27))))
			(symbol "Conn_01x08_1_1"
				(rectangle (start -1.27 -10.16) (end 1.27 10.16) (stroke (width 0.254)) (fill (type background)))
				(pin passive line (at -5.08 8.89 0) (length 3.81) (name "Pin_1" (effects (font (size 1.27 1.27)))) (number "1"))
				(pin passive line (at -5.08 6.35 0) (length 3.81) (name "Pin_2" (effects (font (size 1.27 1.27)))) (number "2"))
				(pin passive line (at -5.08 3.81 0) (length 3.81) (name "Pin_3" (effects (font (size 1.27 1.27)))) (number "3"))
				(pin passive line (at -5.08 1.27 0) (length 3.81) (name "Pin_4" (effects (font (size 1.27 1.27)))) (number "4"))
				(pin passive line (at -5.08 -1.27 0) (length 3.81) (name "Pin_5" (effects (font (size 1.27 1.27)))) (number "5"))
				(pin passive line (at -5.08 -3.81 0) (length 3.81) (name "Pin_6" (effects (font (size 1.27 1.27)))) (number "6"))
				(pin passive line (at -5.08 -6.35 0) (length 3.81) (name "Pin_7" (effects (font (size 1.27 1.27)))) (number "7"))
				(pin passive line (at -5.08 -8.89 0) (length 3.81) (name "Pin_8" (effects (font (size 1.27 1.27)))) (number "8"))
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
    sch += add_text("DANEBEN! PROTOTYPE CARRIER BOARD (MODULAR SHOWCASE)", 30, 20, 3.5)
    sch += add_text("Hochschule Niederrhein - Mikrocontroller (5. Semester) - KiCad 9.0", 30, 28, 2.0)

    # Section 2: Power Inlet & Power Outlets Bus (Top Left)
    sch += add_text("1. POWER INLET & MODULAR POWER BUS", 30, 45, 2.2)
    sch += add_sym("Connector_Generic:Conn_01x02", "J_PWR_IN", "5V_GND_SCREW", "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal", 45, 60)
    sch += add_label("+5V", 35, 58.73, 180)
    sch += add_label("GND", 35, 61.27, 180)

    sch += add_sym("Connector_Generic:Conn_01x02", "J_PWR_AUX", "5V_GND_HEADER", "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical", 75, 60)
    sch += add_label("+5V", 65, 58.73, 180)
    sch += add_label("GND", 65, 61.27, 180)

    # Power Indicator (3.3V)
    sch += add_sym("Device:R", "R_PWR", "330R", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 100, 60)
    sch += add_label("+3V3", 100, 53, 90)
    sch += add_wire(100, 53, 100, 56.19)
    sch += add_sym("Device:LED", "LED_PWR", "GREEN_PWR", "LED_THT:LED_D5.0mm", 100, 72, 90)
    sch += add_wire(100, 63.81, 100, 68.19)
    sch += add_label("GND", 100, 78, 270)
    sch += add_wire(100, 75.81, 100, 78)

    # Power Outlets
    sch += add_sym("Connector_Generic:Conn_01x04", "J_OUT_5V", "5V_BUS_x4", "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical", 45, 95)
    for i, dy in enumerate([3.81, 1.27, -1.27, -3.81]):
        sch += add_label("+5V", 35, 95 - dy, 180)

    sch += add_sym("Connector_Generic:Conn_01x04", "J_OUT_3V3", "3V3_BUS_x4", "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical", 75, 95)
    for i, dy in enumerate([3.81, 1.27, -1.27, -3.81]):
        sch += add_label("+3V3", 65, 95 - dy, 180)

    sch += add_sym("Connector_Generic:Conn_01x06", "J_OUT_GND", "GND_BUS_x6", "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical", 105, 95)
    for i, dy in enumerate([6.35, 3.81, 1.27, -1.27, -3.81, -6.35]):
        sch += add_label("GND", 95, 95 - dy, 180)

    # Section 3: Seeed Studio XIAO ESP32-S3 Sense Carrier (Center)
    sch += add_text("2. SEEED STUDIO XIAO ESP32-S3 SENSE CARRIER", 150, 45, 2.2)
    sch += add_sym("Connector_Generic:Conn_01x07", "J_MCU_L", "XIAO_LEFT_PINS", "Connector_PinSocket_2.54mm:PinSocket_1x07_P2.54mm_Vertical", 170, 75)
    mcu_l_nets = ["AUX_GPIO", "BTN_TEST", "TRIG_EXT", "ECHO_EXT", "I2S_BCLK", "I2S_LRC", "I2S_DIN"]
    for i, dy in enumerate([7.62, 5.08, 2.54, 0, -2.54, -5.08, -7.62]):
        sch += add_label(mcu_l_nets[i], 160, 75 - dy, 180)

    sch += add_sym("Connector_Generic:Conn_01x07", "J_MCU_R", "XIAO_RIGHT_PINS", "Connector_PinSocket_2.54mm:PinSocket_1x07_P2.54mm_Vertical", 215, 75, 180)
    mcu_r_nets = ["STATUS_LED", "TRIG_INT", "ECHO_INT", "GND", "+3V3", "GND", "+5V"]
    for i, dy in enumerate([7.62, 5.08, 2.54, 0, -2.54, -5.08, -7.62]):
        sch += add_label(mcu_r_nets[i], 225, 75 - dy, 0)

    # Section 4: Dual Ultrasonic Sensors (External & Internal) with Level Dividers
    sch += add_text("3. ULTRASONIC SENSORS & 5V->3.3V LEVEL SHIFTERS", 30, 130, 2.2)
    # External Sensor
    sch += add_sym("Connector_Generic:Conn_01x04", "J_EXT", "EXT_PRESENCE_SENSOR", "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Horizontal", 50, 150)
    sch += add_label("+5V", 40, 150 - 3.81, 180)
    sch += add_label("TRIG_EXT", 40, 150 - 1.27, 180)
    sch += add_label("ECHO_EXT_RAW", 40, 150 + 1.27, 180)
    sch += add_label("GND", 40, 150 + 3.81, 180)

    # Divider R_EXT1 & R_EXT2
    sch += add_sym("Device:R", "R_EXT1", "1k", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 75, 150, 90)
    sch += add_label("ECHO_EXT_RAW", 68, 150, 180)
    sch += add_wire(68, 150, 71.19, 150)
    sch += add_sym("Device:R", "R_EXT2", "2k", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 90, 160)
    sch += add_wire(78.81, 150, 90, 150)
    sch += add_wire(90, 150, 90, 156.19)
    sch += add_label("ECHO_EXT", 90, 145, 90)
    sch += add_wire(90, 145, 90, 150)
    sch += add_label("GND", 90, 168, 270)
    sch += add_wire(90, 163.81, 90, 168)

    # Internal Sensor
    sch += add_sym("Connector_Generic:Conn_01x04", "J_INT", "INT_BIN_DEPTH_SENSOR", "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Horizontal", 140, 150)
    sch += add_label("+5V", 130, 150 - 3.81, 180)
    sch += add_label("TRIG_INT", 130, 150 - 1.27, 180)
    sch += add_label("ECHO_INT_RAW", 130, 150 + 1.27, 180)
    sch += add_label("GND", 130, 150 + 3.81, 180)

    # Divider R_INT1 & R_INT2
    sch += add_sym("Device:R", "R_INT1", "1k", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 165, 150, 90)
    sch += add_label("ECHO_INT_RAW", 158, 150, 180)
    sch += add_wire(158, 150, 161.19, 150)
    sch += add_sym("Device:R", "R_INT2", "2k", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 180, 160)
    sch += add_wire(168.81, 150, 180, 150)
    sch += add_wire(180, 150, 180, 156.19)
    sch += add_label("ECHO_INT", 180, 145, 90)
    sch += add_wire(180, 145, 180, 150)
    sch += add_label("GND", 180, 168, 270)
    sch += add_wire(180, 163.81, 180, 168)

    # Section 5: Audio Amplifier (MAX98357A) & Speaker Outputs
    sch += add_text("4. I2S CLASS-D AUDIO AMPLIFIER (MAX98357A)", 260, 45, 2.2)
    sch += add_sym("Connector_Generic:Conn_01x07", "J_AMP", "MAX98357A_HEADER", "Connector_PinSocket_2.54mm:PinSocket_1x07_P2.54mm_Vertical", 280, 75)
    amp_nets = ["I2S_LRC", "I2S_BCLK", "I2S_DIN", "GND", "+3V3", "GND", "+5V"]
    for i, dy in enumerate([7.62, 5.08, 2.54, 0, -2.54, -5.08, -7.62]):
        sch += add_label(amp_nets[i], 270, 75 - dy, 180)

    # Speaker Terminals
    sch += add_sym("Connector_Generic:Conn_01x02", "J_SPK", "8R_SPEAKER_SCREW", "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal", 340, 60)
    sch += add_label("SPK_POS", 330, 58.73, 180)
    sch += add_label("SPK_NEG", 330, 61.27, 180)

    sch += add_sym("Connector_Generic:Conn_01x02", "J_SPK_HDR", "8R_SPEAKER_TAP", "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical", 340, 80)
    sch += add_label("SPK_POS", 330, 78.73, 180)
    sch += add_label("SPK_NEG", 330, 81.27, 180)

    # Section 6: Modular Expansion Bus & Diagnostics
    sch += add_text("5. EXPANSION BUS & TEST SIMULATION", 260, 130, 2.2)
    sch += add_sym("Connector_Generic:Conn_01x08", "J_EXP", "EXPANSION_BUS", "Connector_PinHeader_2.54mm:PinHeader_1x08_P2.54mm_Vertical", 280, 155)
    exp_nets = ["+5V", "+3V3", "GND", "I2S_BCLK", "I2S_LRC", "I2S_DIN", "STATUS_LED", "AUX_GPIO"]
    for i, dy in enumerate([8.89, 6.35, 3.81, 1.27, -1.27, -3.81, -6.35, -8.89]):
        sch += add_label(exp_nets[i], 270, 155 - dy, 180)

    # Status LED
    sch += add_sym("Device:R", "R_STAT", "330R", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 330, 140, 90)
    sch += add_label("STATUS_LED", 320, 140, 180)
    sch += add_wire(320, 140, 326.19, 140)
    sch += add_sym("Device:LED", "LED_STATUS", "RED_ALERT", "LED_THT:LED_D5.0mm", 345, 140, 90)
    sch += add_wire(333.81, 140, 341.19, 140)
    sch += add_label("GND", 355, 140, 0)
    sch += add_wire(348.81, 140, 355, 140)

    # Test Button (SW_TEST) with Pull-up (R_TEST 10k)
    sch += add_sym("Device:R", "R_TEST", "10k", "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", 330, 165)
    sch += add_label("+3V3", 330, 158, 90)
    sch += add_wire(330, 158, 330, 161.19)
    sch += add_sym("Switch:SW_Push", "SW_TEST", "TEST_TRIGGER", "Button_Switch_THT:SW_PUSH_6mm", 330, 180)
    sch += add_wire(330, 168.81, 330, 180)
    sch += add_wire(330, 180, 324.92, 180)
    sch += add_label("BTN_TEST", 315, 180, 180)
    sch += add_wire(315, 180, 324.92, 180)
    sch += add_label("GND", 342, 180, 0)
    sch += add_wire(335.08, 180, 342, 180)

    sch += """\t(sheet_instances
		(path "/"
			(page "1")
		)
	)
)
"""
    with open(sch_file, "w", encoding="utf-8") as f:
        f.write(sch)
    print("SUCCESS: Generated complete schematic at", sch_file)

if __name__ == "__main__":
    build_complete_schematic()
