import pcbnew
import os

def mm(val):
    return pcbnew.FromMM(val)

def build_modular_carrier_board():
    board = pcbnew.BOARD()
    
    # 1. Setup Layer names and basic board parameters
    design_settings = board.GetDesignSettings()
    
    # 2. Define Nets
    net_names = [
        "GND", "+5V", "+3V3",
        "TRIG_EXT", "ECHO_EXT", "ECHO_EXT_RAW",
        "TRIG_INT", "ECHO_INT", "ECHO_INT_RAW",
        "I2S_BCLK", "I2S_LRC", "I2S_DIN",
        "STATUS_LED", "BTN_TEST", "AUX_GPIO",
        "SPK_POS", "SPK_NEG"
    ]
    
    nets = {}
    for name in net_names:
        net = pcbnew.NETINFO_ITEM(board, name)
        board.Add(net)
        nets[name] = board.FindNet(name)
        
    print(f"Added {len(nets)} nets to board.")
    
    # 3. Create Board Outline on Edge.Cuts (95mm x 70mm with generous clearance)
    w_mm = 95.0
    h_mm = 70.0
    outline_pts = [
        (0.0, 0.0),
        (w_mm, 0.0),
        (w_mm, h_mm),
        (0.0, h_mm),
        (0.0, 0.0)
    ]
    
    for i in range(len(outline_pts) - 1):
        seg = pcbnew.PCB_SHAPE(board)
        seg.SetShape(pcbnew.SHAPE_T_SEGMENT)
        seg.SetLayer(pcbnew.Edge_Cuts)
        seg.SetWidth(mm(0.15))
        seg.SetStart(pcbnew.VECTOR2I(mm(outline_pts[i][0]), mm(outline_pts[i][1])))
        seg.SetEnd(pcbnew.VECTOR2I(mm(outline_pts[i+1][0]), mm(outline_pts[i+1][1])))
        board.Add(seg)
        
    print("Edge.Cuts outline created.")
    
    # 4. Footprint Loader Helper
    base_fp_dir = "C:/Program Files/KiCad/9.0/share/kicad/footprints/"
    
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
        found = False
        for pad in fp.Pads():
            if pad.GetNumber() == str(pad_num):
                pad.SetNet(nets[net_name])
                found = True
        if not found:
            print(f"Warning: Pad {pad_num} not found in {fp.GetReference()}")

    def get_pad_pos(fp, pad_num):
        for pad in fp.Pads():
            if pad.GetNumber() == str(pad_num):
                return pad.GetPosition()
        return None

    def add_track_pts(p1, p2, net_name, width=0.5, layer=pcbnew.F_Cu):
        tr = pcbnew.PCB_TRACK(board)
        tr.SetStart(p1)
        tr.SetEnd(p2)
        tr.SetWidth(mm(width))
        tr.SetLayer(layer)
        tr.SetNet(nets[net_name])
        board.Add(tr)

    # 5. Place Mounting Holes (M3 in corners, 5mm inset)
    load_fp("MountingHole.pretty", "MountingHole_3.2mm_M3", "H1", "M3", 5.0, 5.0)
    load_fp("MountingHole.pretty", "MountingHole_3.2mm_M3", "H2", "M3", 90.0, 5.0)
    load_fp("MountingHole.pretty", "MountingHole_3.2mm_M3", "H3", "M3", 5.0, 65.0)
    load_fp("MountingHole.pretty", "MountingHole_3.2mm_M3", "H4", "M3", 90.0, 65.0)

    # 6. Place MCU Sockets (Seeed XIAO ESP32-S3 Sense: 2x 1x7, spaced 15.24mm = 600 mil)
    # Left Header: D0..D6
    j_mcu_l = load_fp("Connector_PinSocket_2.54mm.pretty", "PinSocket_1x07_P2.54mm_Vertical", "J_MCU_L", "XIAO_LEFT", 38.0, 24.0)
    set_pad_net(j_mcu_l, "1", "AUX_GPIO")     # D0 / A0
    set_pad_net(j_mcu_l, "2", "BTN_TEST")     # D1 / A1
    set_pad_net(j_mcu_l, "3", "TRIG_EXT")     # D2 / A2
    set_pad_net(j_mcu_l, "4", "ECHO_EXT")     # D3 / A3
    set_pad_net(j_mcu_l, "5", "I2S_BCLK")    # D4 / SDA
    set_pad_net(j_mcu_l, "6", "I2S_LRC")     # D5 / SCL
    set_pad_net(j_mcu_l, "7", "I2S_DIN")     # D6 / TX

    # Attach 3D model of Seeed XIAO ESP32-S3 Sense plugged into socket
    m_xiao = pcbnew.FP_3DMODEL()
    m_xiao.m_Filename = "${KIPRJMOD}/3dmodels/Seeed_XIAO_ESP32S3_Sense.wrl"
    m_xiao.m_Offset = pcbnew.VECTOR3D(7.62, 7.62, 8.5)
    m_xiao.m_Scale = pcbnew.VECTOR3D(1.0, 1.0, 1.0)
    j_mcu_l.Models().push_back(m_xiao)


    # Right Header: D7..D10, 3V3, GND, 5V
    j_mcu_r = load_fp("Connector_PinSocket_2.54mm.pretty", "PinSocket_1x07_P2.54mm_Vertical", "J_MCU_R", "XIAO_RIGHT", 53.24, 24.0)
    set_pad_net(j_mcu_r, "1", "STATUS_LED")  # D7 / RX
    set_pad_net(j_mcu_r, "2", "TRIG_INT")    # D8
    set_pad_net(j_mcu_r, "3", "ECHO_INT")    # D9
    set_pad_net(j_mcu_r, "4", "GND")         # D10 (spare / GND)
    set_pad_net(j_mcu_r, "5", "+3V3")        # 3V3
    set_pad_net(j_mcu_r, "6", "GND")         # GND
    set_pad_net(j_mcu_r, "7", "+5V")         # 5V

    # 7. Place Power Inlet Section (Top-Left)
    j_pwr = load_fp("TerminalBlock_Phoenix.pretty", "TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal", "J_PWR_IN", "5V_GND", 12.0, 8.0)
    set_pad_net(j_pwr, "1", "+5V")
    set_pad_net(j_pwr, "2", "GND")

    j_pwr_aux = load_fp("Connector_PinHeader_2.54mm.pretty", "PinHeader_1x02_P2.54mm_Vertical", "J_PWR_AUX", "PWR_TAP", 24.0, 8.0)
    set_pad_net(j_pwr_aux, "1", "+5V")
    set_pad_net(j_pwr_aux, "2", "GND")

    # Power Indicator: R_PWR (330R) and LED_PWR (Green)
    r_pwr = load_fp("Resistor_THT.pretty", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", "R_PWR", "330R", 11.0, 17.0)
    set_pad_net(r_pwr, "1", "+3V3")
    set_pad_net(r_pwr, "2", "+3V3") # Anode current limiter

    led_pwr = load_fp("LED_THT.pretty", "LED_D5.0mm", "LED_PWR", "GREEN_3V3", 28.0, 17.0)
    set_pad_net(led_pwr, "1", "GND")   # Cathode
    set_pad_net(led_pwr, "2", "+3V3")  # Anode


    # 8. Place Modular Power Bus Outlets
    # 5V Outlet (1x4)
    j_out_5v = load_fp("Connector_PinHeader_2.54mm.pretty", "PinHeader_1x04_P2.54mm_Vertical", "J_OUT_5V", "5V_BUS", 9.0, 24.0)
    for p in ["1", "2", "3", "4"]:
        set_pad_net(j_out_5v, p, "+5V")
    add_track_pts(get_pad_pos(j_out_5v, "1"), get_pad_pos(j_out_5v, "4"), "+5V", 0.8)

    # 3.3V Outlet (1x4)
    j_out_3v3 = load_fp("Connector_PinHeader_2.54mm.pretty", "PinHeader_1x04_P2.54mm_Vertical", "J_OUT_3V3", "3V3_BUS", 16.0, 24.0)
    for p in ["1", "2", "3", "4"]:
        set_pad_net(j_out_3v3, p, "+3V3")
    add_track_pts(get_pad_pos(j_out_3v3, "1"), get_pad_pos(j_out_3v3, "4"), "+3V3", 0.6)

    # GND Bus (1x6)
    j_out_gnd = load_fp("Connector_PinHeader_2.54mm.pretty", "PinHeader_1x06_P2.54mm_Vertical", "J_OUT_GND", "GND_BUS", 23.0, 24.0)
    for p in ["1", "2", "3", "4", "5", "6"]:
        set_pad_net(j_out_gnd, p, "GND")
    add_track_pts(get_pad_pos(j_out_gnd, "1"), get_pad_pos(j_out_gnd, "6"), "GND", 0.8)

    # 9. Place Sensor Interfaces & Level Dividers (Horizontal 1x4 headers for clear clearance)
    # External Sensor (Presence / Pavement)
    j_ext = load_fp("Connector_PinHeader_2.54mm.pretty", "PinHeader_1x04_P2.54mm_Horizontal", "J_EXT", "EXT_SENSOR", 14.0, 58.0)
    set_pad_net(j_ext, "1", "+5V")
    set_pad_net(j_ext, "2", "TRIG_EXT")
    set_pad_net(j_ext, "3", "ECHO_EXT_RAW")
    set_pad_net(j_ext, "4", "GND")

    r_ext1 = load_fp("Resistor_THT.pretty", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", "R_EXT1", "1k", 9.0, 46.0)
    set_pad_net(r_ext1, "1", "ECHO_EXT_RAW")
    set_pad_net(r_ext1, "2", "ECHO_EXT")

    r_ext2 = load_fp("Resistor_THT.pretty", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", "R_EXT2", "2k", 23.0, 46.0)
    set_pad_net(r_ext2, "1", "ECHO_EXT")
    set_pad_net(r_ext2, "2", "GND")

    add_track_pts(get_pad_pos(r_ext1, "2"), get_pad_pos(r_ext2, "1"), "ECHO_EXT", 0.4)

    # Internal Sensor (Bin Capacity)
    j_int = load_fp("Connector_PinHeader_2.54mm.pretty", "PinHeader_1x04_P2.54mm_Horizontal", "J_INT", "INT_SENSOR", 40.0, 58.0)
    set_pad_net(j_int, "1", "+5V")
    set_pad_net(j_int, "2", "TRIG_INT")
    set_pad_net(j_int, "3", "ECHO_INT_RAW")
    set_pad_net(j_int, "4", "GND")

    r_int1 = load_fp("Resistor_THT.pretty", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", "R_INT1", "1k", 37.0, 46.0)
    set_pad_net(r_int1, "1", "ECHO_INT_RAW")
    set_pad_net(r_int1, "2", "ECHO_INT")

    r_int2 = load_fp("Resistor_THT.pretty", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", "R_INT2", "2k", 51.0, 46.0)
    set_pad_net(r_int2, "1", "ECHO_INT")
    set_pad_net(r_int2, "2", "GND")

    add_track_pts(get_pad_pos(r_int1, "2"), get_pad_pos(r_int2, "1"), "ECHO_INT", 0.4)

    # 10. Place Audio Amplifier (MAX98357A I2S Breakout Socket)
    j_amp = load_fp("Connector_PinSocket_2.54mm.pretty", "PinSocket_1x07_P2.54mm_Vertical", "J_AMP", "MAX98357A", 68.0, 16.0)
    set_pad_net(j_amp, "1", "I2S_LRC")   # LRC
    set_pad_net(j_amp, "2", "I2S_BCLK")  # BCLK
    set_pad_net(j_amp, "3", "I2S_DIN")   # DIN
    set_pad_net(j_amp, "4", "GND")       # GAIN tied to GND for standard 9dB
    set_pad_net(j_amp, "5", "+3V3")      # SD_MODE pulled high
    set_pad_net(j_amp, "6", "GND")       # GND
    set_pad_net(j_amp, "7", "+5V")       # VIN (5V power)

    # Attach 3D model of MAX98357A module plugged into socket
    m_amp = pcbnew.FP_3DMODEL()
    m_amp.m_Filename = "${KIPRJMOD}/3dmodels/MAX98357A_Module.wrl"
    m_amp.m_Offset = pcbnew.VECTOR3D(0.0, 7.62, 8.5)
    m_amp.m_Scale = pcbnew.VECTOR3D(1.0, 1.0, 1.0)
    j_amp.Models().push_back(m_amp)


    # Speaker Terminals (with ample spacing)
    j_spk = load_fp("TerminalBlock_Phoenix.pretty", "TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal", "J_SPK", "8R_SPK", 80.0, 18.0)
    set_pad_net(j_spk, "1", "SPK_POS")
    set_pad_net(j_spk, "2", "SPK_NEG")

    j_spk_hdr = load_fp("Connector_PinHeader_2.54mm.pretty", "PinHeader_1x02_P2.54mm_Vertical", "J_SPK_HDR", "SPK_TAP", 80.0, 26.0)
    set_pad_net(j_spk_hdr, "1", "SPK_POS")
    set_pad_net(j_spk_hdr, "2", "SPK_NEG")

    # 11. Place Modular Expansion Header (1x8)
    j_exp = load_fp("Connector_PinHeader_2.54mm.pretty", "PinHeader_1x08_P2.54mm_Vertical", "J_EXP", "EXPANSION", 84.0, 36.0)
    set_pad_net(j_exp, "1", "+5V")
    set_pad_net(j_exp, "2", "+3V3")
    set_pad_net(j_exp, "3", "GND")
    set_pad_net(j_exp, "4", "I2S_BCLK")   # SDA
    set_pad_net(j_exp, "5", "I2S_LRC")    # SCL
    set_pad_net(j_exp, "6", "I2S_DIN")    # TX
    set_pad_net(j_exp, "7", "STATUS_LED") # RX
    set_pad_net(j_exp, "8", "AUX_GPIO")   # GPIO0

    # 12. Diagnostics & Simulation Controls
    r_stat = load_fp("Resistor_THT.pretty", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", "R_STAT", "330R", 38.0, 10.0)
    set_pad_net(r_stat, "1", "STATUS_LED")
    set_pad_net(r_stat, "2", "STATUS_LED")

    led_stat = load_fp("LED_THT.pretty", "LED_D5.0mm", "LED_STATUS", "RED_ALERT", 53.0, 10.0)
    set_pad_net(led_stat, "1", "GND")
    set_pad_net(led_stat, "2", "STATUS_LED")

    # Simulation Test Trigger Button (SW_TEST)
    sw_test = load_fp("Button_Switch_THT.pretty", "SW_PUSH_6mm", "SW_TEST", "TEST_BTN", 68.0, 54.0)
    set_pad_net(sw_test, "1", "BTN_TEST")
    set_pad_net(sw_test, "2", "GND")

    r_test = load_fp("Resistor_THT.pretty", "R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal", "R_TEST", "10k", 68.0, 44.0)
    set_pad_net(r_test, "1", "+3V3")
    set_pad_net(r_test, "2", "BTN_TEST")

    # 13. Silkscreen Labels
    def add_text(text, x, y, size=1.0, layer=pcbnew.F_SilkS):
        txt = pcbnew.PCB_TEXT(board)
        txt.SetText(text)
        txt.SetLayer(layer)
        txt.SetTextSize(pcbnew.VECTOR2I(mm(size), mm(size)))
        txt.SetTextThickness(mm(0.18))
        txt.SetPosition(pcbnew.VECTOR2I(mm(x), mm(y)))
        board.Add(txt)

    # Board Title Silkscreen
    add_text("DANEBEN! PROTOTYPE CARRIER", 33.0, 4.0, 1.5)
    add_text("HSNR - MIKROCONTROLLER (5.SEM)", 34.0, 6.5, 0.9)

    add_text("PWR IN", 12.0, 4.5, 0.8)
    add_text("5V 3V3 GND", 14.0, 36.5, 0.8)

    add_text("SEEED XIAO S3", 41.0, 21.0, 0.9)
    add_text("USB-C ^", 43.5, 22.8, 0.85)

    add_text("EXT SENSOR", 12.0, 53.0, 0.8)
    add_text("INT SENSOR", 38.0, 53.0, 0.8)

    add_text("I2S AUDIO", 66.0, 10.0, 0.8)
    add_text("SPK 8R", 80.0, 14.5, 0.8)

    add_text("EXPANSION", 84.0, 33.0, 0.8)
    add_text("TEST BTN", 68.0, 62.5, 0.8)

    # 14. Save Board
    output_dir = "hardware/Daneben_Prototype_Carrier_Board"
    os.makedirs(output_dir, exist_ok=True)
    pcb_path = os.path.join(output_dir, "Daneben_Prototype_Carrier_Board.kicad_pcb")
    pcbnew.SaveBoard(pcb_path, board)
    print(f"SUCCESS: Saved KiCad PCB to: {pcb_path}")

if __name__ == "__main__":
    build_modular_carrier_board()
