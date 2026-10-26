import os
import uuid
import math

def gen_uuid():
    return str(uuid.uuid4())

SCALE = 0.393700787

def s(val):
    return val * SCALE

def generate_vrml_models(models_dir):
    os.makedirs(models_dir, exist_ok=True)
    
    # 1. Seeed Studio XIAO ESP32-S3 Sense
    xiao_path = os.path.join(models_dir, "Seeed_XIAO_ESP32S3_Sense.wrl")
    with open(xiao_path, "w", encoding="utf-8") as f:
        f.write(f"""#VRML V2.0 utf8
# Seeed Studio XIAO ESP32-S3 Sense 3D Model
Transform {{
  children [
    # Main PCB
    Transform {{
      translation 0 0 {s(0.6)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.08 0.08 0.08
              specularColor 0.2 0.2 0.2
            }}
          }}
          geometry Box {{ size {s(17.5)} {s(21.0)} {s(1.2)} }}
        }}
      ]
    }}
    # Castellated Pads Left
    Transform {{
      translation {-s(8.2)} 0 {s(0.6)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{ diffuseColor 0.85 0.72 0.2 }}
          }}
          geometry Box {{ size {s(1.1)} {s(17.8)} {s(1.25)} }}
        }}
      ]
    }}
    # Castellated Pads Right
    Transform {{
      translation {s(8.2)} 0 {s(0.6)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{ diffuseColor 0.85 0.72 0.2 }}
          }}
          geometry Box {{ size {s(1.1)} {s(17.8)} {s(1.25)} }}
        }}
      ]
    }}
    # Metal RF Shield
    Transform {{
      translation 0 {-s(2.5)} {s(1.2 + 0.9)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.82 0.82 0.84
              specularColor 0.9 0.9 0.9
              shininess 0.7
            }}
          }}
          geometry Box {{ size {s(14.0)} {s(12.0)} {s(1.8)} }}
        }}
      ]
    }}
    # USB-C Receptacle Top
    Transform {{
      translation 0 {s(9.0)} {s(1.2 + 1.5)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.75 0.75 0.78
              specularColor 0.8 0.8 0.8
            }}
          }}
          geometry Box {{ size {s(8.9)} {s(6.5)} {s(3.0)} }}
        }}
      ]
    }}
    # Camera Module Top
    Transform {{
      translation 0 {-s(1.0)} {s(1.2 + 1.8 + 2.0)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{ diffuseColor 0.12 0.12 0.12 }}
          }}
          geometry Box {{ size {s(8.5)} {s(8.5)} {s(3.5)} }}
        }},
        Transform {{
          translation 0 0 {s(2.0)}
          children [
            Shape {{
              appearance Appearance {{
                material Material {{
                  diffuseColor 0.05 0.05 0.08
                  specularColor 0.8 0.8 0.9
                  shininess 0.9
                }}
              }}
              geometry Cylinder {{ radius {s(3.2)} height {s(1.5)} }}
            }}
          ]
        }}
      ]
    }}
  ]
}}
""")

    # 2. MAX98357A I2S Amplifier Module
    amp_path = os.path.join(models_dir, "MAX98357A_Module.wrl")
    with open(amp_path, "w", encoding="utf-8") as f:
        f.write(f"""#VRML V2.0 utf8
# MAX98357A I2S Audio Amp Breakout Board
Transform {{
  children [
    # Purple PCB
    Transform {{
      translation 0 0 {s(0.8)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.45 0.12 0.65
              specularColor 0.3 0.1 0.4
            }}
          }}
          geometry Box {{ size {s(19.0)} {s(18.0)} {s(1.6)} }}
        }}
      ]
    }}
    # QFN IC
    Transform {{
      translation 0 0 {s(1.6 + 0.4)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{ diffuseColor 0.1 0.1 0.1 }}
          }}
          geometry Box {{ size {s(3.0)} {s(3.0)} {s(0.8)} }}
        }}
      ]
    }}
    # Header Pins along left edge (X = -7.62)
    Transform {{
      translation {-s(7.62)} 0 {-s(2.0)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{ diffuseColor 0.85 0.75 0.2 }}
          }}
          geometry Box {{ size {s(0.64)} {s(15.24)} {s(5.0)} }}
        }}
      ]
    }}
  ]
}}
""")

    # 3. AJ-SR04M Waterproof Ultrasonic Sensor Module
    aj_path = os.path.join(models_dir, "AJ_SR04M_Module.wrl")
    with open(aj_path, "w", encoding="utf-8") as f:
        f.write(f"""#VRML V2.0 utf8
# AJ-SR04M / JSN-SR04T Waterproof Ultrasonic Sensor Board
# Size: 41.5mm x 28.5mm x 1.6mm PCB
Transform {{
  children [
    # 1. Main Deep Blue PCB
    Transform {{
      translation 0 0 {s(0.8)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.05 0.22 0.55
              specularColor 0.2 0.3 0.6
              shininess 0.3
            }}
          }}
          geometry Box {{ size {s(41.5)} {s(28.5)} {s(1.6)} }}
        }}
      ]
    }}
    # 2. Cylindrical Metal Transducer Socket on Left Edge (where probe cable plugs in)
    Transform {{
      translation {-s(15.5)} 0 {s(1.6 + 4.5)}
      rotation 0 1 0 1.5708
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.82 0.82 0.85
              specularColor 0.95 0.95 0.95
              shininess 0.8
            }}
          }}
          geometry Cylinder {{ radius {s(4.5)} height {s(9.5)} }}
        }},
        # Cable Boot / Strain relief exiting to the left
        Transform {{
          translation 0 {-s(9.0)} 0
          children [
            Shape {{
              appearance Appearance {{
                material Material {{ diffuseColor 0.1 0.1 0.1 }}
              }}
              geometry Cylinder {{ radius {s(3.2)} height {s(8.0)} }}
            }},
            # Heavy shielded probe wire running outward
            Transform {{
              translation 0 {-s(8.0)} 0
              children [
                Shape {{
                  appearance Appearance {{
                    material Material {{ diffuseColor 0.15 0.15 0.15 }}
                  }}
                  geometry Cylinder {{ radius {s(2.2)} height {s(12.0)} }}
                }}
              ]
            }}
          ]
        }}
      ]
    }}
    # 3. Microcontroller / Signal Processing ASIC
    Transform {{
      translation {s(2.0)} 0 {s(1.6 + 0.7)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{ diffuseColor 0.12 0.12 0.12 }}
          }}
          geometry Box {{ size {s(10.0)} {s(6.0)} {s(1.4)} }}
        }}
      ]
    }}
    # 4. High-Q Ultrasonic Transformer Coil
    Transform {{
      translation {s(5.0)} {s(8.0)} {s(1.6 + 2.5)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.7 0.7 0.72
              specularColor 0.8 0.8 0.8
            }}
          }}
          geometry Box {{ size {s(7.0)} {s(7.0)} {s(5.0)} }}
        }}
      ]
    }}
    # 5. 4-Pin Header on Right Edge (facing carrier socket)
    Transform {{
      translation {s(18.0)} 0 {-s(2.5)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{ diffuseColor 0.85 0.75 0.2 }}
          }}
          geometry Box {{ size {s(0.64)} {s(7.62)} {s(6.0)} }}
        }}
      ]
    }}
    # 6. M2.5 Standoff Mounting Corner Pads
    Transform {{
      translation {-s(18.5)} {-s(11.5)} {s(0.8)}
      children [
        Shape {{
          appearance Appearance {{ material Material {{ diffuseColor 0.8 0.7 0.2 }} }}
          geometry Cylinder {{ radius {s(2.5)} height {s(1.65)} }}
        }}
      ]
    }},
    Transform {{
      translation {s(18.5)} {-s(11.5)} {s(0.8)}
      children [
        Shape {{
          appearance Appearance {{ material Material {{ diffuseColor 0.8 0.7 0.2 }} }}
          geometry Cylinder {{ radius {s(2.5)} height {s(1.65)} }}
        }}
      ]
    }},
    Transform {{
      translation {-s(18.5)} {s(11.5)} {s(0.8)}
      children [
        Shape {{
          appearance Appearance {{ material Material {{ diffuseColor 0.8 0.7 0.2 }} }}
          geometry Cylinder {{ radius {s(2.5)} height {s(1.65)} }}
        }}
      ]
    }},
    Transform {{
      translation {s(18.5)} {s(11.5)} {s(0.8)}
      children [
        Shape {{
          appearance Appearance {{ material Material {{ diffuseColor 0.8 0.7 0.2 }} }}
          geometry Cylinder {{ radius {s(2.5)} height {s(1.65)} }}
        }}
      ]
    }}
  ]
}}
""")

    # 4. Sizable 12x12mm Tactile Pushbuttons
    for name, diffuse, cap_height in [
        ("Tactile_Switch_12x12mm_Blue.wrl", "0.15 0.45 0.95", 4.0),
        ("Tactile_Switch_12x12mm_Amber.wrl", "0.95 0.65 0.1", 4.0),
        ("Tactile_Switch_12x12mm_Red.wrl", "0.85 0.15 0.15", 4.0)
    ]:
        btn_path = os.path.join(models_dir, name)
        with open(btn_path, "w", encoding="utf-8") as f:
            f.write(f"""#VRML V2.0 utf8
# Sizable 12mm x 12mm Tactile Pushbutton Switch
Transform {{
  children [
    # Black base body
    Transform {{
      translation 0 0 {s(2.0)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{ diffuseColor 0.1 0.1 0.1 }}
          }}
          geometry Box {{ size {s(12.0)} {s(12.0)} {s(4.0)} }}
        }}
      ]
    }}
    # Metal top plate
    Transform {{
      translation 0 0 {s(4.15)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.75 0.75 0.78
              specularColor 0.8 0.8 0.8
            }}
          }}
          geometry Box {{ size {s(12.0)} {s(12.0)} {s(0.3)} }}
        }}
      ]
    }}
    # Sizable Round Plunger Button Cap
    Transform {{
      translation 0 0 {s(4.3 + cap_height / 2.0)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor {diffuse}
              specularColor 0.5 0.5 0.5
              shininess 0.4
            }}
          }}
          geometry Cylinder {{ radius {s(3.4)} height {s(cap_height)} }}
        }}
      ]
    }}
  ]
}}
""")

    # 5. USB-C Onboard Receptacle
    usbc_path = os.path.join(models_dir, "USB_C_Receptacle.wrl")
    with open(usbc_path, "w", encoding="utf-8") as f:
        f.write(f"""#VRML V2.0 utf8
# USB Type-C Female Receptacle
Transform {{
  children [
    # Metal Shell
    Transform {{
      translation 0 0 {s(1.6)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.82 0.82 0.85
              specularColor 0.9 0.9 0.9
              shininess 0.8
            }}
          }}
          geometry Box {{ size {s(8.9)} {s(7.2)} {s(3.2)} }}
        }}
      ]
    }}
    # Black Inner Tongue
    Transform {{
      translation 0 {s(2.0)} {s(1.6)}
      children [
        Shape {{
          appearance Appearance {{ material Material {{ diffuseColor 0.05 0.05 0.05 }} }}
          geometry Box {{ size {s(6.5)} {s(3.5)} {s(0.7)} }}
        }}
      ]
    }}
  ]
}}
""")

    # 6. 2-Pin Screw Terminal
    term_path = os.path.join(models_dir, "TerminalBlock_2P.wrl")
    with open(term_path, "w", encoding="utf-8") as f:
        f.write(f"""#VRML V2.0 utf8
# 2-Pin 5.08mm Pitch Screw Terminal Block
Transform {{
  children [
    # Blue/Green Plastic Housing
    Transform {{
      translation 0 0 {s(5.0)}
      children [
        Shape {{
          appearance Appearance {{
            material Material {{
              diffuseColor 0.1 0.35 0.65
              specularColor 0.2 0.3 0.4
            }}
          }}
          geometry Box {{ size {s(10.16)} {s(8.5)} {s(10.0)} }}
        }}
      ]
    }}
    # Screws
    Transform {{
      translation {-s(2.54)} 0 {s(10.1)}
      children [
        Shape {{
          appearance Appearance {{ material Material {{ diffuseColor 0.8 0.8 0.8 }} }}
          geometry Cylinder {{ radius {s(1.5)} height {s(0.3)} }}
        }}
      ]
    }},
    Transform {{
      translation {s(2.54)} 0 {s(10.1)}
      children [
        Shape {{
          appearance Appearance {{ material Material {{ diffuseColor 0.8 0.8 0.8 }} }}
          geometry Cylinder {{ radius {s(1.5)} height {s(0.3)} }}
        }}
      ]
    }}
  ]
}}
""")

    print("Generated all updated VRML 3D models in", models_dir)

if __name__ == "__main__":
    generate_vrml_models("hardware/Daneben_Prototype_Carrier_Board/3dmodels")
