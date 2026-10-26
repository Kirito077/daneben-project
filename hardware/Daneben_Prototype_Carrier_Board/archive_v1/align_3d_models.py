import os
import re

SCALE = 0.393700787
def s(mm_val):
    return mm_val * SCALE

def update_xiao_model():
    # Board size: 17.5 mm (W) x 21.0 mm (L)
    # 7 pins run along Y: 6 intervals of 2.54 mm = 15.24 mm (from -7.62 to +7.62)
    # USB-C is at the top (Y = +9.0)
    # Rows are at X = -7.62 and X = +7.62
    vrml = f"""#VRML V2.0 utf8
# Seeed Studio XIAO ESP32-S3 Sense 3D Component Model
Transform {{
  children [
    # 1. Main Black Matte PCB
    Transform {{
      translation 0 0 {s(0.6)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.08 0.08 0.08
              specularColor 0.3 0.3 0.3
              shininess 0.2
            }}
          }}
          geometry Box {{
            size {s(17.5)} {s(21.0)} {s(1.2)}
          }}
        }}
      ]
    }}

    # 2. Gold Castellation Edge Pads Left
    Transform {{
      translation {-s(8.2)} 0 {s(0.6)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.85 0.72 0.35
              specularColor 0.9 0.8 0.4
              shininess 0.8
            }}
          }}
          geometry Box {{
            size {s(1.2)} {s(18.0)} {s(1.25)}
          }}
        }}
      ]
    }}

    # 3. Gold Castellation Edge Pads Right
    Transform {{
      translation {s(8.2)} 0 {s(0.6)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.85 0.72 0.35
              specularColor 0.9 0.8 0.4
              shininess 0.8
            }}
          }}
          geometry Box {{
            size {s(1.2)} {s(18.0)} {s(1.25)}
          }}
        }}
      ]
    }}

    # 4. USB-C Receptacle (Top Edge)
    Transform {{
      translation 0 {s(9.0)} {s(1.2 + 1.6)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.85 0.85 0.88
              specularColor 0.95 0.95 0.95
              shininess 0.9
            }}
          }}
          geometry Box {{
            size {s(8.9)} {s(7.3)} {s(3.2)}
          }}
        }}
      ]
    }}

    # 5. ESP32-S3 Metal RF Shield Can
    Transform {{
      translation 0 {-s(2.5)} {s(1.2 + 0.9)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.75 0.75 0.78
              specularColor 0.88 0.88 0.9
              shininess 0.7
            }}
          }}
          geometry Box {{
            size {s(12.0)} {s(10.0)} {s(1.8)}
          }}
        }}
      ]
    }}

    # 6. OV2640 Miniature Camera Module on Top
    Transform {{
      translation 0 {-s(3.0)} {s(1.2 + 1.8 + 1.5)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.12 0.12 0.12
              specularColor 0.2 0.2 0.2
            }}
          }}
          geometry Box {{
            size {s(5.0)} {s(5.0)} {s(3.0)}
          }}
        }}
      ]
    }}

    # 7. Optical Camera Glass Lens
    Transform {{
      translation 0 {-s(3.0)} {s(1.2 + 1.8 + 3.1)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.1 0.25 0.45
              specularColor 0.9 0.95 1.0
              shininess 0.95
              transparency 0.2
            }}
          }}
          geometry Cylinder {{
            radius {s(1.8)}
            height {s(0.5)}
          }}
        }}
      ]
    }}

    # 8. Gold Male Pin Headers (Extending 8.5mm downwards into socket)
    # Left Header Pins
    Transform {{
      translation {-s(7.62)} 0 {-s(4.25)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.85 0.72 0.35
              specularColor 0.9 0.8 0.4
              shininess 0.8
            }}
          }}
          geometry Box {{
            size {s(0.64)} {s(15.24)} {s(8.5)}
          }}
        }}
      ]
    }}

    # Right Header Pins
    Transform {{
      translation {s(7.62)} 0 {-s(4.25)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.85 0.72 0.35
              specularColor 0.9 0.8 0.4
              shininess 0.8
            }}
          }}
          geometry Box {{
            size {s(0.64)} {s(15.24)} {s(8.5)}
          }}
        }}
      ]
    }}
  ]
}}
"""
    path = "hardware/Daneben_Prototype_Carrier_Board/3dmodels/Seeed_XIAO_ESP32S3_Sense.wrl"
    with open(path, "w", encoding="utf-8") as f:
        f.write(vrml)
    print("Updated", path)


def update_amp_model():
    # MAX98357A Breakout: 17.5mm wide x 19.0mm long
    # 1x7 pin row is along the LEFT edge at X = -7.62mm
    # Pins span Y from -7.62 to +7.62
    vrml = f"""#VRML V2.0 utf8
# MAX98357A I2S Mono Audio Amp Module 3D Model
Transform {{
  children [
    # 1. Purple PCB Body (centered relative to pins)
    Transform {{
      translation {s(4.0)} 0 {s(0.8)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.38 0.15 0.55
              specularColor 0.4 0.2 0.6
              shininess 0.3
            }}
          }}
          geometry Box {{
            size {s(15.0)} {s(19.0)} {s(1.6)}
          }}
        }}
      ]
    }}

    # 2. MAX98357A QFN IC (Center)
    Transform {{
      translation {s(4.0)} 0 {s(1.6 + 0.5)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.1 0.1 0.1
              specularColor 0.2 0.2 0.2
              shininess 0.4
            }}
          }}
          geometry Box {{
            size {s(3.5)} {s(3.5)} {s(1.0)}
          }}
        }}
      ]
    }}

    # 3. SMD Inductors and capacitors
    Transform {{
      translation {s(8.0)} {s(3.5)} {s(1.6 + 0.6)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.2 0.2 0.22
              specularColor 0.3 0.3 0.35
            }}
          }}
          geometry Box {{
            size {s(3.0)} {s(3.0)} {s(1.2)}
          }}
        }}
      ]
    }}

    # 4. Gold Pin Header Pins (Along left edge at X=0, spanning Y=-7.62 to +7.62)
    Transform {{
      translation 0 0 {-s(4.25)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.85 0.72 0.35
              specularColor 0.9 0.8 0.4
              shininess 0.8
            }}
          }}
          geometry Box {{
            size {s(0.64)} {s(15.24)} {s(8.5)}
          }}
        }}
      ]
    }}
  ]
}}
"""
    path = "hardware/Daneben_Prototype_Carrier_Board/3dmodels/MAX98357A_Module.wrl"
    with open(path, "w", encoding="utf-8") as f:
        f.write(vrml)
    print("Updated", path)

def update_pcb_offsets():
    pcb_file = "hardware/Daneben_Prototype_Carrier_Board/Daneben_Prototype_Carrier_Board.kicad_pcb"
    with open(pcb_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Update XIAO offset to (7.62 7.62 8.5) or exact center
    # In J_MCU_L, Pad 1 is at (38.0, 24.0)
    # The pins run along Y from 0 to 15.24. Center is 7.62.
    content = re.sub(
        r'(\(model "\$\{KIPRJMOD\}/3dmodels/Seeed_XIAO_ESP32S3_Sense\.wrl"\s*\(offset\s*\(xyz\s*)[^\)]+(\)\))',
        r'\g<1>7.62 7.62 8.5\2',
        content
    )

    # Update MAX98357A offset: J_AMP has Pad 1 at (68.0, 16.0). Pins run along Y from 0 to 15.24.
    content = re.sub(
        r'(\(model "\$\{KIPRJMOD\}/3dmodels/MAX98357A_Module\.wrl"\s*\(offset\s*\(xyz\s*)[^\)]+(\)\))',
        r'\g<1>0 7.62 8.5\2',
        content
    )

    with open(pcb_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated offsets in PCB file")

if __name__ == "__main__":
    update_xiao_model()
    update_amp_model()
    update_pcb_offsets()
