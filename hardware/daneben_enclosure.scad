// Daneben Projekt - Smart Waste Bin Sensor Enclosure
// Parametric CAD Model (Measurements in mm)
// Open this file in OpenSCAD (https://openscad.org/) to view, modify, and export to STL/STEP.

// --- Overall Dimensions ---
width = 120;
depth = 80;
height = 150;
roof_angle = 20;
wall_thickness = 3;

module enclosure() {
    difference() {
        // --- 1. Main Outer Body ---
        union() {
            // Base rectangular box
            cube([width, depth, height - 40]);
            
            // Sloped roof (20 degrees for water shedding and solar angle)
            translate([0, 0, height - 40])
            rotate([-roof_angle, 0, 0])
            cube([width, depth / cos(roof_angle), 40]);
            
            // Drip Edge Overhang (protects the sealing gasket)
            translate([-2, -2, height/2]) 
            cube([width+4, depth+4, 6]);
            
            // Rear Mounting Bracket curve (matches waste bin handle radius)
            translate([0, depth, 0])
            cube([width, 10, height]);
        }
        
        // --- 2. Hollow Interior ---
        translate([wall_thickness, wall_thickness, wall_thickness])
        cube([width-(wall_thickness*2), depth-(wall_thickness*2), height]);
        
        // --- 3. Solar Panel Recess (Top Roof) ---
        // Fits a standard 100x60mm mini solar panel
        translate([10, 10, height - 12])
        rotate([-roof_angle, 0, 0])
        cube([100, 60, 5]);

        // --- 4. Camera Window Hole (Bottom Face) ---
        // 20mm diameter, to be sealed with borosilicate glass and UV glue
        translate([width/3, depth/2, -5])
        cylinder(h=15, r=10, $fn=50);

        // --- 5. Distance Sensor Hole (Bottom Face) ---
        // 16mm diameter for an ultrasonic JSN-SR04T transducer
        translate([2*width/3, depth/2, -5])
        cylinder(h=15, r=8, $fn=50);
        
        // --- 6. Speaker / Audio Vents (Front Face) ---
        // Acoustic vents to be sealed with hydrophobic ePTFE (Gore-Tex) membrane inside
        for(i=[-15 : 6 : 15]) {
            translate([width/2 + i, -5, 25])
            rotate([-90, 0, 0])
            cylinder(h=15, r=1.5, $fn=20);
        }
        
        // --- 7. Mounting Strap Slots (Rear Bracket) ---
        // For heavy-duty steel bands or industrial zip-ties
        translate([10, depth+5, height - 30])
        cube([width-20, 15, 6]);
        
        translate([10, depth+5, 30])
        cube([width-20, 15, 6]);
        
        // --- 8. Battery Tube Hole (Side or Bottom) ---
        // For sliding in the 18650 cartridge
        translate([-5, depth/2, 20])
        rotate([0, 90, 0])
        cylinder(h=20, r=11, $fn=50);
    }
}

// Render the enclosure
enclosure();
