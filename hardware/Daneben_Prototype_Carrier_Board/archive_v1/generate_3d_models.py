import os

def create_xiao_3d_model(filepath):
    # Scale: 1 mm = 1.0 / 2.54 = 0.393700787 units in VRML
    SCALE = 0.393700787
    
    def s(mm_val):
        return mm_val * SCALE

    vrml_content = f"""#VRML V2.0 utf8
# Seeed Studio XIAO ESP32-S3 Sense 3D Component Model
# Dimensions: 17.5mm x 21.0mm x 1.2mm PCB + USB-C + RF Shield + Camera Module

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
              diffuseColor 0.82 0.82 0.85
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

    # 7. Optical Camera Glass Lens (Cylinder)
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
      translation {-s(7.62)} 0 {-s(4.0)}
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
            size {s(0.64)} {s(15.24)} {s(8.0)}
          }}
        }}
      ]
    }}

    # Right Header Pins
    Transform {{
      translation {s(7.62)} 0 {-s(4.0)}
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
            size {s(0.64)} {s(15.24)} {s(8.0)}
          }}
        }}
      ]
    }}
  ]
}}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(vrml_content)
    print("Created 3D model for XIAO S3 Sense at:", filepath)


def create_amp_3d_model(filepath):
    SCALE = 0.393700787
    def s(mm_val):
        return mm_val * SCALE

    vrml_content = f"""#VRML V2.0 utf8
# MAX98357A I2S 3W Class D Audio Amplifier Module 3D Model
# Dimensions: 17.5mm x 19.0mm x 1.6mm Purple PCB + QFN IC + SMD Passives

Transform {{
  children [
    # 1. Purple PCB Body
    Transform {{
      translation 0 0 {s(0.8)}
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
            size {s(17.5)} {s(19.0)} {s(1.6)}
          }}
        }}
      ]
    }}

    # 2. MAX98357A QFN IC (Center)
    Transform {{
      translation 0 0 {s(1.6 + 0.5)}
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

    # 3. SMD Inductor / Filter Components
    Transform {{
      translation {s(4.0)} {s(3.0)} {s(1.6 + 0.6)}
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

    # 4. Gold Pin Header Pins (Bottom)
    Transform {{
      translation 0 {-s(7.0)} {-s(4.0)}
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
            size {s(15.24)} {s(0.64)} {s(8.0)}
          }}
        }}
      ]
    }}
  ]
}}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(vrml_content)
    print("Created 3D model for MAX98357A at:", filepath)


if __name__ == "__main__":
    out_dir = "hardware/Daneben_Prototype_Carrier_Board/3dmodels"
    os.makedirs(out_dir, exist_ok=True)
    create_xiao_3d_model(os.path.join(out_dir, "Seeed_XIAO_ESP32S3_Sense.wrl"))
    create_amp_3d_model(os.path.join(out_dir, "MAX98357A_Module.wrl"))
