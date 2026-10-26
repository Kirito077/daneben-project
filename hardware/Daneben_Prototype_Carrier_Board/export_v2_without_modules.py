import pcbnew
import os
import subprocess

def export_and_render_without_modules():
    kicad_3d_base = "C:/Program Files/KiCad/9.0/share/kicad/3dmodels/Connector_PinSocket_2.54mm.3dshapes"
    pcb_dir = "hardware/Daneben_Prototype_Carrier_Board"
    main_pcb_file = os.path.join(pcb_dir, "Daneben_Prototype_Carrier_Board.kicad_pcb")
    out_pcb_file = os.path.join(pcb_dir, "Daneben_Carrier_Board_v2_Without_Modules.kicad_pcb")
    
    board = pcbnew.LoadBoard(main_pcb_file)
    print("Loaded main board:", main_pcb_file)
    
    # Footprints to replace daughterboard models with standard female pin sockets
    socket_map = {
        "J_AJ_OUT": os.path.join(kicad_3d_base, "PinSocket_1x04_P2.54mm_Vertical.wrl").replace("\\", "/"),
        "J_AJ_IN": os.path.join(kicad_3d_base, "PinSocket_1x04_P2.54mm_Vertical.wrl").replace("\\", "/"),
        "J_MCU_L": os.path.join(kicad_3d_base, "PinSocket_1x07_P2.54mm_Vertical.wrl").replace("\\", "/"),
        "J_MCU_R": os.path.join(kicad_3d_base, "PinSocket_1x07_P2.54mm_Vertical.wrl").replace("\\", "/"),
        "J_AMP": os.path.join(kicad_3d_base, "PinSocket_1x07_P2.54mm_Vertical.wrl").replace("\\", "/"),
    }
    
    for fp in board.GetFootprints():
        ref = fp.GetReference()
        if ref in socket_map:
            fp.Models().clear()
            m = pcbnew.FP_3DMODEL()
            m.m_Filename = socket_map[ref]
            # Standard vertical pin socket offset (aligned to pin 1)
            # In KiCad 3dshapes, origin is pad 1
            m.m_Offset = pcbnew.VECTOR3D(0, 0, 0)
            m.m_Rotation = pcbnew.VECTOR3D(0, 0, 0)
            m.m_Scale = pcbnew.VECTOR3D(1, 1, 1)
            fp.Models().push_back(m)
            print(f"Replaced {ref} 3D model with standard socket: {socket_map[ref]}")
            
    board.Save(out_pcb_file)
    print("Saved carrier board without daughterboard modules to:", out_pcb_file)
    
    # Also create a bare board PCB (all 3D models removed)
    bare_pcb_file = os.path.join(pcb_dir, "Daneben_Carrier_Board_v2_Bare_PCB.kicad_pcb")
    bare_board = pcbnew.LoadBoard(main_pcb_file)
    for fp in bare_board.GetFootprints():
        fp.Models().clear()
    bare_board.Save(bare_pcb_file)
    print("Saved bare PCB to:", bare_pcb_file)

if __name__ == "__main__":
    export_and_render_without_modules()
