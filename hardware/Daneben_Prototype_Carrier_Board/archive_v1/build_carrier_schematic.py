import uuid
import os

def gen_uuid():
    return str(uuid.uuid4())

def generate_schematic():
    out_dir = "hardware/Daneben_Prototype_Carrier_Board"
    os.makedirs(out_dir, exist_ok=True)
    sch_file = os.path.join(out_dir, "Daneben_Prototype_Carrier_Board.kicad_sch")
    
    sch_content = f"""(kicad_sch
	(version 20250114)
	(generator "eeschema")
	(generator_version "9.0")
	(uuid "{gen_uuid()}")
	(paper "A3")
	(title_block
		(title "Daneben! Prototype Carrier Board (Modular Showcase Edition)")
		(date "2026-10-22")
		(rev "v1.0")
		(company "Hochschule Niederrhein (HSNR) - Mikrocontroller")
		(comment 1 "Houses Seeed Studio XIAO ESP32-S3 Sense, Sensors, Audio Amp, Power & Expansion Outlets")
	)
	(lib_symbols
	)
	(sheet_instances
		(path "/"
			(page "1")
		)
	)
)
"""
    with open(sch_file, "w", encoding="utf-8") as f:
        f.write(sch_content)
    print("SUCCESS: Generated schematic file at", sch_file)

if __name__ == "__main__":
    generate_schematic()
