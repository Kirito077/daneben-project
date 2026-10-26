import pcbnew
import os
import math

def mm(val):
    return pcbnew.FromMM(val)

def build_v2_pcb():
    board = pcbnew.BOARD()
    
    # 1. Nets
    net_names = [
        "GND", "+5V", "VBUS_RAW", "+3V3",
        "TRIG_OUT", "ECHO_OUT",
        "TRIG_IN", "ECHO_IN",
        "BTN_CAL_OUT", "BTN_CAL_IN",
        "LED_CAL_OUT", "LED_CAL_IN",
        "I2S_BCLK", "I2S_LRC", "I2S_DIN",
        "SPK_POS", "SPK_NEG",
        "CC1", "CC2"
    ]
    
    nets = {}
    for name in net_names:
        net = pcbnew.NETINFO_ITEM(board, name)
        board.Add(net)
        nets[name] = board.FindNet(name)
        
    print(f"Initialized {len(nets)} nets.")
    
    # 2. Board Outline (130mm x 90mm with R=4mm rounded corners)
    w_mm = 130.0
    h_mm = 90.0
    r_mm = 4.0
    
    # Line segments
    lines = [
        ((r_mm, 0.0), (w_mm - r_mm, 0.0)),
        ((w_mm, r_mm), (w_mm, h_mm - r_mm)),
        ((w_mm - r_mm, h_mm), (r_mm, h_mm)),
        ((0.0, h_mm - r_mm), (0.0, r_mm))
    ]
    for p1, p2 in lines:
        seg = pcbnew.PCB_SHAPE(board)
        seg.SetShape(pcbnew.SHAPE_T_SEGMENT)
        seg.SetLayer(pcbnew.Edge_Cuts)
        seg.SetWidth(mm(0.15))
        seg.SetStart(pcbnew.VECTOR2I(mm(p1[0]), mm(p1[1])))
        seg.SetEnd(pcbnew.VECTOR2I(mm(p2[0]), mm(p2[1])))
        board.Add(seg)
        
    # Corner arcs (or straight 45 deg chamfers for clean outline)
    chamfers = [
        ((0.0, r_mm), (r_mm, 0.0)),
        ((w_mm - r_mm, 0.0), (w_mm, r_mm)),
        ((w_mm, h_mm - r_mm), (w_mm - r_mm, h_mm)),
        ((r_mm, h_mm), (0.0, h_mm - r_mm))
    ]
    for p1, p2 in chamfers:
        seg = pcbnew.PCB_SHAPE(board)
        seg.SetShape(pcbnew.SHAPE_T_SEGMENT)
        seg.SetLayer(pcbnew.Edge_Cuts)
        seg.SetWidth(mm(0.15))
        seg.SetStart(pcbnew.VECTOR2I(mm(p1[0]), mm(p1[1])))
        seg.SetEnd(pcbnew.VECTOR2I(mm(p2[0]), mm(p2[1])))
        board.Add(seg)
        
    print("Edge.Cuts outline created (130mm x 90mm).")
    
    # 3. Footprint Loader Helper
    base_fp_dir = "C:/Program Files/KiCad/9.0/share/kicad/footprints/"
    models_dir = os.path.abspath("hardware/Daneben_Prototype_Carrier_Board/3dmodels").replace("\\", "/")
    
    def load_fp(lib, name, ref, val, x, y, angle=0):
        fp = pcbnew.FootprintLoad(base_fp_dir + lib, name)
        if not fp:
            raise RuntimeError(f"Failed to load footprint {lib}/{name}")
        fp.SetReference(ref)
        fp.SetValue(val)
        fp.SetPosition(pcbnew.VECTOR2I(mm(x), mm(y)))
        if angle != 0:
            fp.SetOrientation(pcbnew.EDA_ANGLE(angle, pcbnew.DEGREES_T))
        board.Add(fp)
        return fp

    def set_pad_net(fp, pad_num, net_name):
        for pad in fp.Pads():
            if pad.GetNumber() == str(pad_num):
                pad.SetNet(nets[net_name])

    def get_pad_pos(fp, pad_num):
        for pad in fp.Pads():
            if pad.GetNumber() == str(pad_num):
                return pad.GetPosition()
        return fp.GetPosition()

    def add_3d_model(fp, model_rel_path, offset_mm, rot_deg=(0,0,0), scale=(1,1,1)):
        # Clear existing models
        fp.Models().clear()
        m = pcbnew.FP_3DMODEL()
        m.m_Filename = f"{models_dir}/{model_rel_path}"
        # Set offset, rotation, scale
        m.m_Offset = pcbnew.VECTOR3D(offset_mm[0], offset_mm[1], offset_mm[2])
        m.m_Rotation = pcbnew.VECTOR3D(rot_deg[0], rot_deg[1], rot_deg[2])
        m.m_Scale = pcbnew.VECTOR3D(scale[0], scale[1], scale[2])
        fp.Models().push_back(m)

    # 4. Corner M3 Mounting Holes
    for ref, x, y in [("H1", 5.0, 5.0), ("H2", 125.0, 5.0), ("H3", 5.0, 85.0), ("H4", 125.0, 85.0)]:
        load_fp("MountingHole.pretty", "MountingHole_3.2mm_M3_Pad", ref, "M3_HOLE", x, y)

    # 5. AJ-SR04M Outside Ultrasonic Sensor Dock (Top Left)
    # 4 Standoff holes for AJ-SR04M #1 (M2.5)
    load_fp("MountingHole.pretty", "MountingHole_2.7mm_M2.5_Pad", "H_AJ1_1", "M2.5_STANDOFF", 5.5, 13.5)
    load_fp("MountingHole.pretty", "MountingHole_2.7mm_M2.5_Pad", "H_AJ1_2", "M2.5_STANDOFF", 42.5, 13.5)
    load_fp("MountingHole.pretty", "MountingHole_2.7mm_M2.5_Pad", "H_AJ1_3", "M2.5_STANDOFF", 5.5, 36.5)
    load_fp("MountingHole.pretty", "MountingHole_2.7mm_M2.5_Pad", "H_AJ1_4", "M2.5_STANDOFF", 42.5, 36.5)

    # 4-Pin Socket Header for AJ-SR04M #1
    fp_aj_out = load_fp("Connector_PinSocket_2.54mm.pretty", "PinSocket_1x04_P2.54mm_Vertical", "J_AJ_OUT", "AJ_SR04M_OUT", 41.5, 25.0)
    set_pad_net(fp_aj_out, "1", "+5V")
    set_pad_net(fp_aj_out, "2", "TRIG_OUT")
    set_pad_net(fp_aj_out, "3", "ECHO_OUT")
    set_pad_net(fp_aj_out, "4", "GND")
    # Attach 3D Model of AJ-SR04M Module
    add_3d_model(fp_aj_out, "AJ_SR04M_Module.wrl", (-17.75, 0.0, 8.5), (0, 0, 0))

    # 6. AJ-SR04M Inside Ultrasonic Sensor Dock (Bottom Left)
    # 4 Standoff holes for AJ-SR04M #2 (M2.5)
    load_fp("MountingHole.pretty", "MountingHole_2.7mm_M2.5_Pad", "H_AJ2_1", "M2.5_STANDOFF", 5.5, 53.5)
    load_fp("MountingHole.pretty", "MountingHole_2.7mm_M2.5_Pad", "H_AJ2_2", "M2.5_STANDOFF", 42.5, 53.5)
    load_fp("MountingHole.pretty", "MountingHole_2.7mm_M2.5_Pad", "H_AJ2_3", "M2.5_STANDOFF", 5.5, 76.5)
    load_fp("MountingHole.pretty", "MountingHole_2.7mm_M2.5_Pad", "H_AJ2_4", "M2.5_STANDOFF", 42.5, 76.5)

    # 4-Pin Socket Header for AJ-SR04M #2
    fp_aj_in = load_fp("Connector_PinSocket_2.54mm.pretty", "PinSocket_1x04_P2.54mm_Vertical", "J_AJ_IN", "AJ_SR04M_IN", 41.5, 65.0)
    set_pad_net(fp_aj_in, "1", "+5V")
    set_pad_net(fp_aj_in, "2", "TRIG_IN")
    set_pad_net(fp_aj_in, "3", "ECHO_IN")
    set_pad_net(fp_aj_in, "4", "GND")
    # Attach 3D Model of AJ-SR04M Module
    add_3d_model(fp_aj_in, "AJ_SR04M_Module.wrl", (-17.75, 0.0, 8.5), (0, 0, 0))

    # 7. Seeed Studio XIAO ESP32-S3 Sense (Top Center)
    fp_mcu_l = load_fp("Connector_PinSocket_2.54mm.pretty", "PinSocket_1x07_P2.54mm_Vertical", "J_MCU_L", "XIAO_L", 57.0, 23.62)
    fp_mcu_r = load_fp("Connector_PinSocket_2.54mm.pretty", "PinSocket_1x07_P2.54mm_Vertical", "J_MCU_R", "XIAO_R", 72.24, 23.62)
    
    set_pad_net(fp_mcu_l, "1", "TRIG_OUT")
    set_pad_net(fp_mcu_l, "2", "ECHO_OUT")
    set_pad_net(fp_mcu_l, "3", "TRIG_IN")
    set_pad_net(fp_mcu_l, "4", "ECHO_IN")
    set_pad_net(fp_mcu_l, "5", "BTN_CAL_OUT")
    set_pad_net(fp_mcu_l, "6", "BTN_CAL_IN")
    set_pad_net(fp_mcu_l, "7", "LED_CAL_OUT")

    set_pad_net(fp_mcu_r, "1", "LED_CAL_IN")
    set_pad_net(fp_mcu_r, "2", "I2S_BCLK")
    set_pad_net(fp_mcu_r, "3", "I2S_LRC")
    set_pad_net(fp_mcu_r, "4", "I2S_DIN")
    set_pad_net(fp_mcu_r, "5", "+3V3")
    set_pad_net(fp_mcu_r, "6", "GND")
    set_pad_net(fp_mcu_r, "7", "+5V")

    # Attach 3D Model of XIAO ESP32-S3 Sense
    add_3d_model(fp_mcu_l, "Seeed_XIAO_ESP32S3_Sense.wrl", (7.62, 0.0, 8.5), (0, 0, 0))

    # 8. Dedicated USB-C Power Entry & Distribution (Bottom Center)
    fp_usbc = load_fp("Connector_USB.pretty", "USB_C_Receptacle_HRO_TYPE-C-31-M-12", "J_USBC", "USB_C_PWR", 65.0, 87.5)
    for p in ["A4", "A9", "B4", "B9"]:
        set_pad_net(fp_usbc, p, "VBUS_RAW")
    for p in ["A1", "A12", "B1", "B12", "S1"]:
        set_pad_net(fp_usbc, p, "GND")
    set_pad_net(fp_usbc, "A5", "CC1")
    set_pad_net(fp_usbc, "B5", "CC2")
    add_3d_model(fp_usbc, "USB_C_Receptacle.wrl", (0.0, 0.0, 1.6), (0, 0, 0))

    # 5.1k CC Resistors
    fp_r_cc1 = load_fp("Resistor_THT.pretty", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", "R_CC1", "5.1k", 57.0, 81.0)
    set_pad_net(fp_r_cc1, "1", "CC1")
    set_pad_net(fp_r_cc1, "2", "GND")

    fp_r_cc2 = load_fp("Resistor_THT.pretty", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", "R_CC2", "5.1k", 73.0, 81.0)
    set_pad_net(fp_r_cc2, "1", "CC2")
    set_pad_net(fp_r_cc2, "2", "GND")

    # Power Slide Switch
    fp_sw_pwr = load_fp("Button_Switch_THT.pretty", "SW_Slide_SPDT_Straight_CK_OS102011MS2Q", "SW_PWR", "PWR_SWITCH", 54.0, 71.0)
    set_pad_net(fp_sw_pwr, "1", "VBUS_RAW")
    set_pad_net(fp_sw_pwr, "2", "+5V")
    set_pad_net(fp_sw_pwr, "3", "VBUS_RAW")

    # Power Indicator LED (Green) & Resistor
    fp_led_pwr = load_fp("LED_THT.pretty", "LED_D3.0mm", "LED_PWR", "GREEN_PWR", 76.0, 71.0)
    set_pad_net(fp_led_pwr, "2", "+5V")
    set_pad_net(fp_led_pwr, "1", "GND")

    # Bulk Capacitor 100uF
    fp_c_bulk = load_fp("Capacitor_THT.pretty", "CP_Radial_D6.3mm_P2.50mm", "C_BULK1", "100uF", 65.0, 68.0)
    set_pad_net(fp_c_bulk, "1", "+5V")
    set_pad_net(fp_c_bulk, "2", "GND")

    # Alternate 5V Screw Terminal
    fp_ext_pwr = load_fp("TerminalBlock_Phoenix.pretty", "TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal", "J_EXT_5V", "ALT_5V_IN", 52.0, 84.0)
    set_pad_net(fp_ext_pwr, "1", "+5V")
    set_pad_net(fp_ext_pwr, "2", "GND")
    add_3d_model(fp_ext_pwr, "TerminalBlock_2P.wrl", (0.0, 0.0, 0.0), (0, 0, 0))

    # 9. MAX98357A I2S Class D Audio Amplifier (Top Right)
    # Standoff holes for MAX98357A
    load_fp("MountingHole.pretty", "MountingHole_2.7mm_M2.5_Pad", "H_AMP1", "M2.5_STANDOFF", 114.0, 16.0)
    load_fp("MountingHole.pretty", "MountingHole_2.7mm_M2.5_Pad", "H_AMP2", "M2.5_STANDOFF", 114.0, 31.24)

    fp_amp = load_fp("Connector_PinSocket_2.54mm.pretty", "PinSocket_1x07_P2.54mm_Vertical", "J_AMP", "MAX98357A", 95.0, 23.62)
    set_pad_net(fp_amp, "1", "I2S_LRC")
    set_pad_net(fp_amp, "2", "I2S_BCLK")
    set_pad_net(fp_amp, "3", "I2S_DIN")
    set_pad_net(fp_amp, "4", "GND")
    set_pad_net(fp_amp, "5", "GND")
    set_pad_net(fp_amp, "6", "GND")
    set_pad_net(fp_amp, "7", "+5V")
    add_3d_model(fp_amp, "MAX98357A_Module.wrl", (7.62, 0.0, 8.5), (0, 0, 0))

    # Speaker Screw Terminal
    fp_spk = load_fp("TerminalBlock_Phoenix.pretty", "TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal", "J_SPK", "SPEAKER_OUT", 105.0, 8.5)
    set_pad_net(fp_spk, "1", "SPK_POS")
    set_pad_net(fp_spk, "2", "SPK_NEG")
    add_3d_model(fp_spk, "TerminalBlock_2P.wrl", (0.0, 0.0, 0.0), (0, 0, 0))

    # 10. Sizable Dual Calibration Push Buttons & Status LEDs
    # Button 1: Outside Calibration (12x12mm Pushbutton)
    fp_cal_out = load_fp("Button_Switch_THT.pretty", "SW_PUSH-12mm", "SW_CAL_OUT", "CAL_OUTSIDE", 96.0, 48.0)
    set_pad_net(fp_cal_out, "1", "BTN_CAL_OUT")
    set_pad_net(fp_cal_out, "2", "GND")
    add_3d_model(fp_cal_out, "Tactile_Switch_12x12mm_Blue.wrl", (0.0, 0.0, 0.0), (0, 0, 0))

    # Status LED Outside (Blue)
    fp_led_out = load_fp("LED_THT.pretty", "LED_D3.0mm", "LED_CAL_OUT", "BLUE_OUT_STAT", 114.0, 48.0)
    set_pad_net(fp_led_out, "2", "LED_CAL_OUT")
    set_pad_net(fp_led_out, "1", "GND")

    # Button 2: Inside Calibration (12x12mm Pushbutton)
    fp_cal_in = load_fp("Button_Switch_THT.pretty", "SW_PUSH-12mm", "SW_CAL_IN", "CAL_INSIDE", 96.0, 68.0)
    set_pad_net(fp_cal_in, "1", "BTN_CAL_IN")
    set_pad_net(fp_cal_in, "2", "GND")
    add_3d_model(fp_cal_in, "Tactile_Switch_12x12mm_Amber.wrl", (0.0, 0.0, 0.0), (0, 0, 0))

    # Status LED Inside (Amber)
    fp_led_in = load_fp("LED_THT.pretty", "LED_D3.0mm", "LED_CAL_IN", "AMBER_IN_STAT", 114.0, 68.0)
    set_pad_net(fp_led_in, "2", "LED_CAL_IN")
    set_pad_net(fp_led_in, "1", "GND")

    # 11. Modular Expansion Header (Bottom Right)
    fp_aux = load_fp("Connector_PinHeader_2.54mm.pretty", "PinHeader_1x06_P2.54mm_Vertical", "J_AUX", "AUX_EXPANSION", 102.0, 84.0, 90)
    set_pad_net(fp_aux, "1", "+3V3")
    set_pad_net(fp_aux, "2", "LED_CAL_OUT")
    set_pad_net(fp_aux, "3", "LED_CAL_IN")
    set_pad_net(fp_aux, "4", "BTN_CAL_OUT")
    set_pad_net(fp_aux, "5", "BTN_CAL_IN")
    set_pad_net(fp_aux, "6", "GND")

    # 12. Silkscreen Labels & Text Instructions
    def add_silk_text(txt, x, y, size=1.5, layer=pcbnew.F_SilkS):
        t = pcbnew.PCB_TEXT(board)
        t.SetText(txt)
        t.SetLayer(layer)
        t.SetTextSize(pcbnew.VECTOR2I(mm(size), mm(size)))
        t.SetPosition(pcbnew.VECTOR2I(mm(x), mm(y)))
        board.Add(t)

    add_silk_text("DANEBEN! CARRIER BOARD v2.0", 55.0, 5.0, 2.0)
    add_silk_text("HSNR - MIKROCONTROLLER (5. SEMESTER)", 53.0, 9.0, 1.2)
    
    # AJ-SR04M Dock 1 Silk Box & Arrow
    add_silk_text("AJ-SR04M OUTSIDE (GEHWEG)", 10.0, 11.5, 1.3)
    add_silk_text("<-- TRANSDUCER CABLE EXIT (ZERO FRICTION)", 4.0, 38.5, 1.1)

    # AJ-SR04M Dock 2 Silk Box & Arrow
    add_silk_text("AJ-SR04M INSIDE (TONNE)", 10.0, 51.5, 1.3)
    add_silk_text("<-- TRANSDUCER CABLE EXIT (ZERO FRICTION)", 4.0, 78.5, 1.1)

    # Calibration Buttons Silk Labels
    add_silk_text("[CALIBRATE OUTSIDE (FLOOR)]", 82.0, 41.5, 1.2)
    add_silk_text("OUT_STAT", 110.0, 44.0, 1.0)
    add_silk_text("[CALIBRATE INSIDE (BIN DEPTH)]", 82.0, 61.5, 1.2)
    add_silk_text("IN_STAT", 110.0, 64.0, 1.0)

    # Power and USB Labels
    add_silk_text("USB-C PWR IN (5V)", 58.0, 83.0, 1.1)
    add_silk_text("PWR_SW", 49.0, 68.0, 1.0)
    add_silk_text("PWR_ON", 72.0, 68.0, 1.0)

    # 13. Route Copper Tracks
    def route_track(pos1, pos2, net_name, width_mm=0.35, layer=pcbnew.F_Cu):
        t = pcbnew.PCB_TRACK(board)
        t.SetStart(pos1)
        t.SetEnd(pos2)
        t.SetWidth(mm(width_mm))
        t.SetLayer(layer)
        t.SetNet(nets[net_name])
        board.Add(t)

    # Connect signal lines
    signals = [
        (get_pad_pos(fp_mcu_l, "1"), get_pad_pos(fp_aj_out, "2"), "TRIG_OUT"),
        (get_pad_pos(fp_mcu_l, "2"), get_pad_pos(fp_aj_out, "3"), "ECHO_OUT"),
        (get_pad_pos(fp_mcu_l, "3"), get_pad_pos(fp_aj_in, "2"), "TRIG_IN"),
        (get_pad_pos(fp_mcu_l, "4"), get_pad_pos(fp_aj_in, "3"), "ECHO_IN"),
        (get_pad_pos(fp_mcu_l, "5"), get_pad_pos(fp_cal_out, "1"), "BTN_CAL_OUT"),
        (get_pad_pos(fp_mcu_l, "6"), get_pad_pos(fp_cal_in, "1"), "BTN_CAL_IN"),
        (get_pad_pos(fp_mcu_l, "7"), get_pad_pos(fp_led_out, "2"), "LED_CAL_OUT"),
        (get_pad_pos(fp_mcu_r, "1"), get_pad_pos(fp_led_in, "2"), "LED_CAL_IN"),
        (get_pad_pos(fp_mcu_r, "2"), get_pad_pos(fp_amp, "2"), "I2S_BCLK"),
        (get_pad_pos(fp_mcu_r, "3"), get_pad_pos(fp_amp, "1"), "I2S_LRC"),
        (get_pad_pos(fp_mcu_r, "4"), get_pad_pos(fp_amp, "3"), "I2S_DIN"),
    ]
    for p1, p2, net_name in signals:
        route_track(p1, p2, net_name)

    # Power tracks (Heavy 0.8mm)
    pwr_tracks = [
        (get_pad_pos(fp_sw_pwr, "2"), get_pad_pos(fp_mcu_r, "7"), "+5V"),
        (get_pad_pos(fp_sw_pwr, "2"), get_pad_pos(fp_amp, "7"), "+5V"),
        (get_pad_pos(fp_sw_pwr, "2"), get_pad_pos(fp_aj_out, "1"), "+5V"),
        (get_pad_pos(fp_sw_pwr, "2"), get_pad_pos(fp_aj_in, "1"), "+5V"),
        (get_pad_pos(fp_sw_pwr, "2"), get_pad_pos(fp_c_bulk, "1"), "+5V"),
        (get_pad_pos(fp_sw_pwr, "2"), get_pad_pos(fp_ext_pwr, "1"), "+5V"),
        (get_pad_pos(fp_usbc, "A4"), get_pad_pos(fp_sw_pwr, "1"), "VBUS_RAW"),
    ]
    for p1, p2, net_name in pwr_tracks:
        route_track(p1, p2, net_name, width_mm=0.8)

    # 14. Save Board
    out_file = "hardware/Daneben_Prototype_Carrier_Board/Daneben_Prototype_Carrier_Board.kicad_pcb"
    board.Save(out_file)
    print("SUCCESS: Saved v2 carrier PCB to", out_file)

if __name__ == "__main__":
    build_v2_pcb()
