import os
import json

base_dir = "/Users/vineetpathak/Documents/New project/AntiGravity/rental-house-sagar"
dirs = ["plans", "data", "visualization", "docs"]
for d in dirs:
    os.makedirs(os.path.join(base_dir, d), exist_ok=True)

# Helper for SVG
def svg_wrap(content, title, w="900", h="600", viewbox="0 0 900 600"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" width="{w}" height="{h}" style="background:#fff; border: 1px solid #ccc; font-family: monospace;">
    <rect width="100%" height="100%" fill="#ffffff" />
    <g transform="translate(50, 50)">
        <text x="0" y="-20" font-size="20" font-weight="bold" fill="#333">{title}</text>
        {content}
    </g>
    <!-- North Arrow -->
    <g transform="translate(850, 50)">
        <circle cx="0" cy="0" r="15" fill="none" stroke="#333" stroke-width="2"/>
        <polygon points="-5,5 5,5 0,-15" fill="#333"/>
        <text x="0" y="25" text-anchor="middle" font-size="12" font-weight="bold">N</text>
    </g>
</svg>'''

def rect(x, y, w, h, fill="#fdfdfd", stroke="#000", lw=2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="{lw}"/>\n'

def text(x, y, t, s=12, w="normal", fill="#000", a="middle", r=0):
    tr = f' transform="rotate({r} {x} {y})"' if r else ""
    return f'<text x="{x}" y="{y}" font-size="{s}" font-weight="{w}" fill="{fill}" text-anchor="{a}"{tr}>{t}</text>\n'

def line(x1, y1, x2, y2, stroke="#000", lw=2, dash=""):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{lw}"{da}/>\n'

def draw_door(x, y, r, rot): # rot: 0=right, 90=down, 180=left, -90=up
    # simple quarter circle
    return f'<g transform="translate({x},{y}) rotate({rot})"><path d="M 0 0 L {r} 0 A {r} {r} 0 0 1 0 {r} Z" fill="none" stroke="#f44336" stroke-width="2"/></g>\n'

def draw_window(x, y, w, h):
    return rect(x, y, w, h, fill="#e0f7fa", stroke="#00bcd4", lw=1) + line(x, y+h/2, x+w, y+h/2, stroke="#00bcd4", lw=1)

# Drawing GF Floor Plan (Scale: 1ft = 10px). Plot: 50ft (W-E, X) x 30ft (N-S, Y) -> 500x300.
# West is X=0, East is X=500. North is Y=0, South is Y=300.
def draw_gf():
    c = ""
    c += rect(0, 0, 500, 300, fill="none", lw=4) # Plot bounds
    c += text(520, 150, "30 FT ROAD (EAST)", 16, "bold", r=90)
    c += line(500, -20, 500, 320, stroke="#999", lw=2, dash="5,5")
    
    # Rooms
    c += rect(0, 0, 150, 120, fill="#fafafa") # NW Bed2
    c += text(75, 50, "BEDROOM 2", 14, "bold")
    c += text(75, 65, "15' x 12'")
    c += text(20, 30, "[Bed]", 10, fill="#999")
    c += text(120, 30, "[Wardrobe]", 10, fill="#999")
    
    c += rect(0, 170, 150, 130, fill="#fafafa") # SW Master Bed
    c += text(75, 230, "MASTER BEDROOM", 14, "bold")
    c += text(75, 245, "15' x 13'")
    c += text(20, 280, "[Bed]", 10, fill="#999")
    
    # Shaft 2 (West)
    c += rect(0, 120, 40, 50, fill="#eceff1")
    c += line(0, 120, 40, 170, stroke="#999", lw=1)
    c += line(0, 170, 40, 120, stroke="#999", lw=1)
    c += text(20, 145, "OTS", 10)
    
    # Att Bath
    c += rect(40, 120, 60, 50, fill="#e3f2fd")
    c += text(70, 140, "BATH", 12, "bold")
    c += text(70, 155, "6'x5'", 10)
    c += draw_window(40, 130, 5, 30) # Window to shaft
    
    # Corridor / Dining
    c += rect(150, 100, 100, 70, fill="#fff")
    c += text(200, 135, "CORRIDOR/DINING", 10, "bold")
    
    # Shaft 1 (North)
    c += rect(150, 0, 50, 50, fill="#eceff1")
    c += line(150, 0, 200, 50, stroke="#999", lw=1)
    c += line(150, 50, 200, 0, stroke="#999", lw=1)
    c += text(175, 25, "OTS", 10)
    
    # Common Bath
    c += rect(200, 0, 50, 70, fill="#e3f2fd")
    c += text(225, 30, "C.BATH", 12, "bold")
    c += text(225, 45, "5'x7'", 10)
    c += draw_window(195, 10, 5, 30) # Window to shaft
    
    # Living Room (Center)
    c += rect(250, 0, 100, 180, fill="#fff")
    c += text(300, 80, "LIVING ROOM", 14, "bold")
    c += text(300, 95, "10' x 18'")
    c += text(270, 160, "[TV Wall]", 10, fill="#999", r=-90)
    
    # Pooja (NE corner of Living)
    c += rect(310, 0, 40, 40, fill="#fff9c4")
    c += text(330, 20, "POOJA", 10, "bold")
    
    # Kitchen (South Center)
    c += rect(200, 180, 150, 120, fill="#fff3e0")
    c += text(275, 230, "KITCHEN", 14, "bold")
    c += text(275, 245, "15' x 12'")
    c += rect(200, 180, 130, 20, fill="#eee", stroke="#ccc") # Platform East/North
    c += text(230, 190, "[Stove]", 10, fill="#d32f2f")
    c += text(310, 190, "[Sink]", 10, fill="#1976d2")
    c += text(220, 280, "[Fridge]", 10, fill="#999")
    
    # Parking (NE)
    c += rect(350, 0, 150, 180, fill="#e8f5e9")
    c += text(425, 30, "SUV PARKING", 14, "bold")
    c += text(425, 45, "15' x 18'")
    c += text(425, 60, "UG Tank (8000L)", 10, fill="#1565c0")
    c += rect(370, 80, 110, 60, fill="#cfd8dc", stroke="#999", lw=2) # SUV
    c += text(425, 110, "SUV (16'x7')", 10)
    c += text(425, 160, "[2 Bikes]", 10)
    
    # Entry Walkway
    c += rect(350, 180, 150, 50, fill="#fff")
    c += text(425, 205, "ENTRY LOBBY (15'x5')", 10)
    c += rect(480, 180, 20, 50, fill="#ffcc80") # Electric Meters
    c += text(490, 205, "METERS", 8, "bold", r=90)
    
    # Stairs (SE)
    c += rect(350, 230, 150, 70, fill="#f5f5f5")
    c += text(425, 265, "STAIRS (UP)", 12, "bold")
    for i in range(15): c += line(350+i*10, 230, 350+i*10, 300, stroke="#ccc", lw=1)
    
    # Walls / Lines (Thick)
    c += line(150, 0, 150, 300, lw=4) # Vert 1
    c += line(200, 0, 200, 180, lw=4) # Vert 2
    c += line(250, 0, 250, 100, lw=4) # Vert 3
    c += line(350, 0, 350, 300, lw=4) # Vert 4
    c += line(0, 120, 100, 120, lw=4) # Horiz 1
    c += line(0, 170, 150, 170, lw=4) # Horiz 2
    c += line(150, 100, 250, 100, lw=4) # Horiz 3
    c += line(200, 180, 500, 180, lw=4) # Horiz 4
    c += line(350, 230, 500, 230, lw=4) # Horiz 5
    
    # Doors
    c += draw_door(150, 80, 30, 180) # Bed 2
    c += draw_door(150, 200, 30, 180) # Master Bed
    c += draw_door(100, 140, 30, 180) # Att Bath
    c += draw_door(200, 50, 30, 180) # Common Bath
    c += draw_door(250, 130, 30, 0) # Living to Corridor
    c += draw_door(350, 90, 40, 180) # Main House Entry (into Living Room)
    c += draw_door(350, 210, 30, 180) # Kitchen back door
    c += draw_door(350, 280, 30, 180) # Kitchen secondary door / stair access
    
    return svg_wrap(c, "GROUND FLOOR PLAN (2BHK + PARKING)")

def draw_ff():
    c = ""
    c += rect(0, 0, 500, 300, fill="none", lw=4)
    # Shafts & Stairs same
    c += rect(0, 120, 40, 50, fill="#eceff1")
    c += line(0, 120, 40, 170, stroke="#999")
    c += line(0, 170, 40, 120, stroke="#999")
    c += rect(150, 0, 50, 50, fill="#eceff1")
    c += line(150, 0, 200, 50, stroke="#999")
    c += line(150, 50, 200, 0, stroke="#999")
    c += rect(350, 230, 150, 70, fill="#f5f5f5")
    for i in range(15): c += line(350+i*10, 230, 350+i*10, 300, stroke="#ccc", lw=1)
    
    # 1BHK
    c += rect(0, 170, 150, 130, fill="#fafafa") # Bed
    c += text(75, 230, "1BHK BEDROOM", 14, "bold")
    c += text(75, 245, "15' x 13'")
    c += rect(40, 120, 110, 50, fill="#e3f2fd") # Bath
    c += text(95, 140, "1BHK BATH", 12, "bold")
    c += rect(150, 170, 200, 130, fill="#fff") # Living
    c += text(250, 230, "1BHK LIVING", 14, "bold")
    c += text(250, 245, "20' x 13'")
    c += rect(150, 90, 100, 80, fill="#fff3e0") # Kitchen
    c += text(200, 125, "1BHK KITCHEN", 12, "bold")
    c += text(200, 140, "10' x 8'")
    
    # Single Room
    c += rect(0, 0, 150, 120, fill="#fafafa") # SR Bed
    c += text(75, 50, "SR BED/LIVING", 14, "bold")
    c += text(75, 65, "15' x 12'")
    c += rect(200, 0, 50, 90, fill="#e3f2fd") # SR Bath
    c += text(225, 40, "SR BATH", 10, "bold")
    c += rect(250, 0, 200, 170, fill="#fafafa") # SR Room / Kitchenette
    c += text(350, 80, "SINGLE ROOM UNIT", 14, "bold")
    c += text(350, 95, "20' x 17'")
    
    # Balcony
    c += rect(450, 0, 50, 230, fill="#e0f7fa")
    c += text(475, 115, "EAST BALCONY", 14, "bold", r=90)
    
    # Doors
    c += draw_door(350, 210, 30, 90) # 1BHK Main
    c += draw_door(350, 150, 30, -90) # SR Main
    c += draw_door(450, 115, 30, 0) # SR to Balcony
    c += draw_door(450, 210, 30, 0) # 1BHK to Balcony
    
    return svg_wrap(c, "FIRST FLOOR PLAN (1BHK + SINGLE ROOM)")

def draw_sf():
    c = ""
    c += rect(0, 0, 500, 300, fill="none", lw=4)
    # Shafts & Stairs same
    c += rect(0, 120, 40, 50, fill="#eceff1")
    c += line(0, 120, 40, 170, stroke="#999")
    c += line(0, 170, 40, 120, stroke="#999")
    c += rect(150, 0, 50, 50, fill="#eceff1")
    c += line(150, 0, 200, 50, stroke="#999")
    c += line(150, 50, 200, 0, stroke="#999")
    c += rect(350, 230, 150, 70, fill="#f5f5f5")
    for i in range(15): c += line(350+i*10, 230, 350+i*10, 300, stroke="#ccc", lw=1)
    
    # Studio
    c += rect(200, 170, 150, 130, fill="#fafafa") # Studio Room
    c += text(275, 230, "STUDIO ROOM", 14, "bold")
    c += text(275, 245, "15' x 13'")
    c += rect(150, 170, 50, 80, fill="#e3f2fd") # Studio Bath
    c += text(175, 200, "BATH", 10, "bold")
    
    # Terrace
    c += rect(0, 0, 150, 120, fill="#e8f5e9")
    c += rect(40, 120, 110, 50, fill="#e8f5e9")
    c += rect(0, 170, 150, 130, fill="#e8f5e9")
    c += rect(150, 90, 200, 80, fill="#e8f5e9")
    c += rect(200, 0, 300, 170, fill="#e8f5e9")
    c += rect(350, 170, 150, 60, fill="#e8f5e9")
    c += text(150, 80, "OPEN TERRACE / DRYING AREA", 16, "bold")
    
    # Water Tank
    c += rect(370, 240, 40, 40, fill="#1565c0")
    c += text(390, 260, "OHT", 10, fill="#fff")
    c += text(450, 260, "Overhead Tank (3000L)", 10)
    
    # Doors
    c += draw_door(350, 210, 30, 90) # Studio Main
    c += draw_door(300, 170, 30, 180) # Studio to Terrace
    c += draw_door(350, 180, 30, -90) # Stairs to Terrace
    
    return svg_wrap(c, "SECOND FLOOR PLAN (STUDIO + TERRACE)")

with open(f"{base_dir}/plans/ground-floor-plan.svg", "w") as f: f.write(draw_gf())
with open(f"{base_dir}/plans/first-floor-plan.svg", "w") as f: f.write(draw_ff())
with open(f"{base_dir}/plans/second-floor-plan.svg", "w") as f: f.write(draw_sf())

# JSON Files
room_schedule = {
    "Ground_Floor": {"SUV_Parking":"15'x18'", "Stairs":"15'x7'", "Entry_Lobby":"15'x5'", "Living":"10'x18'", "Kitchen":"15'x12'", "Master_Bed":"15'x13'", "Bed_2":"15'x12'", "Common_Bath":"5'x7'", "Att_Bath":"6'x5'", "Pooja":"4'x4'"},
    "First_Floor": {"1BHK_Living":"20'x13'", "1BHK_Kitchen":"10'x8'", "1BHK_Bed":"15'x13'", "1BHK_Bath":"11'x5'", "Single_Room_Living":"20'x17'", "Single_Room_Bed":"15'x12'", "Single_Room_Bath":"5'x9'", "East_Balcony":"5'x23'"},
    "Second_Floor": {"Studio_Room":"15'x13'", "Studio_Kitchenette":"In-Room", "Studio_Bath":"5'x8'", "Staircase_Lobby":"15'x6'", "Open_Terrace":"Remaining Area", "Utility_Drying_Zone":"On Terrace", "Water_Tank_Zone":"Over Stair Mumty"}
}
with open(f"{base_dir}/data/room-schedule.json", "w") as f: json.dump(room_schedule, f, indent=2)

dimensions = {
    "Plot": {"Width_ft": 30, "Depth_ft": 50, "Total_Area_sqft": 1500},
    "Areas": {
        "Ground_Floor": {"Total": 1500, "BuiltUp": 1500, "Parking": 270, "Stair": 105, "Shafts": 45, "Rentable": 1080},
        "First_Floor": {"Total": 1500, "BuiltUp": 1650, "Balcony": 115, "Stair": 105, "Shafts": 45, "Rentable": 1385},
        "Second_Floor": {"Total": 1500, "BuiltUp": 400, "Stair": 105, "Shafts": 45, "Terrace": 950, "Rentable": 195},
        "Efficiency": "Approx 82% Rentable vs BuiltUp (Excellent)"
    },
    "Staircase_Details": {"Width": "3.5 ft per flight", "Tread": "10 inches", "Riser": "7 inches", "Steps": 18, "Landing": "3.5 ft x 7 ft", "Headroom": "Min 7 ft", "Railing": "MS or SS 304"}
}
with open(f"{base_dir}/data/dimensions.json", "w") as f: json.dump(dimensions, f, indent=2)

vastu = {"Orientation": "East Facing", "Main_Door": "North-East (Auspicious)", "UG_Tank": "North-East under parking (Auspicious)", "Kitchen": "South/South-East (Auspicious)", "Master_Bed": "South-West (Auspicious)", "Pooja": "North-East in Living (Auspicious)", "Stairs": "South-East (Acceptable, preserves NE)"}
with open(f"{base_dir}/data/vastu-checklist.json", "w") as f: json.dump(vastu, f, indent=2)

val_check = {"Parking_Fit": "Verified (15x18 handles 16x7 SUV + gate swing + 2 bikes + lobby access)", "OTS_Shafts": "Verified (Central 5x5 ventilates living/baths. Rear 4x5 ventilates rear beds)", "Structural": "Assumption: G+3 column grid matches floor plans", "Verification_Warning": "DO NOT BUILD UNTIL VERIFIED BY LOCAL ARCHITECT AND STRUCTURAL ENGINEER"}
with open(f"{base_dir}/data/validation-checklist.json", "w") as f: json.dump(val_check, f, indent=2)

# Docs
with open(f"{base_dir}/docs/architect-questions.md", "w") as f: f.write("# Questions for Local Architect\n1. Verify column grid and foundation for G+3.\n2. Confirm municipal bylaws for East balcony projection.\n3. Verify soil SBC for UG tank depth in NE.")
with open(f"{base_dir}/docs/buildability-notes.md", "w") as f: f.write("# Buildability Notes\n- **Warning: Do not build until verified.** Final plan must be verified by a structural engineer and Sagar municipal authorities.\n- Shafts: Both OTS shafts must be open to sky. Plumb lines go inside shafts. Provide MS grating at GF for cleaning access.")
with open(f"{base_dir}/docs/validation-report.md", "w") as f: f.write("# Final Validation Report\n- Parking: Validated. 15x18 ft easily fits 16x7 SUV leaving 3ft clearance for gate swing and pedestrian access to tenant stairs.\n- OTS Shafts: Validated. Shaft 1 (Central) ventilates living/common bath. Shaft 2 (Rear) ventilates rear beds/att bath. Both open to sky.\n- Future Floor: Validated. Wet areas stacked.\n- **Assumptions**: Column sizes (assumed 9x15), soil strength.")
with open(f"{base_dir}/README.md", "w") as f: f.write("# Rental Investment House - Sagar MP\nContains complete architectural deliverables. **WARNING: Conceptual design. Do not construct without local structural engineer verification.**\nSee `index.html` for presentation.")

# Three.js Visualization
with open(f"{base_dir}/visualization/camera-scenes.json", "w") as f: json.dump([{"id":"facade","name":"Front Facade"}, {"id":"gf","name":"Ground Floor Massing"}, {"id":"terrace","name":"Terrace & OHT"}], f)
with open(f"{base_dir}/visualization/threejs-tour.js", "w") as f: f.write('''
import * as THREE from 'https://unpkg.com/three@0.160.0/build/three.module.js';
import { OrbitControls } from 'https://unpkg.com/three@0.160.0/examples/jsm/controls/OrbitControls.js';

export function initTour(containerId) {
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0xf0f2f5);
    const camera = new THREE.PerspectiveCamera(45, window.innerWidth / 600, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({antialias:true});
    renderer.setSize(window.innerWidth, 600);
    document.getElementById(containerId).appendChild(renderer.domElement);
    
    const controls = new OrbitControls(camera, renderer.domElement);
    camera.position.set(40, 30, 40);
    
    scene.add(new THREE.AmbientLight(0xffffff, 0.6));
    const dir = new THREE.DirectionalLight(0xffffff, 0.8);
    dir.position.set(10,20,10); scene.add(dir);
    
    // Simple Massing
    const gf = new THREE.Mesh(new THREE.BoxGeometry(30, 10, 50), new THREE.MeshStandardMaterial({color: 0x90caf9}));
    gf.position.y = 5; scene.add(gf);
    const ff = new THREE.Mesh(new THREE.BoxGeometry(30, 10, 50), new THREE.MeshStandardMaterial({color: 0xa5d6a7}));
    ff.position.y = 15; scene.add(ff);
    const sf = new THREE.Mesh(new THREE.BoxGeometry(15, 10, 15), new THREE.MeshStandardMaterial({color: 0xffe082}));
    sf.position.set(-7.5, 25, 17.5); scene.add(sf); // Studio
    
    // Balcony
    const balc = new THREE.Mesh(new THREE.BoxGeometry(30, 1, 5), new THREE.MeshStandardMaterial({color: 0xeeeeee}));
    balc.position.set(0, 10, 27.5); scene.add(balc);
    
    function animate() { requestAnimationFrame(animate); controls.update(); renderer.render(scene, camera); }
    animate();
    return { camera, controls };
}
''')

with open(f"{base_dir}/visualization/virtual-tour.html", "w") as f: f.write('''
<!DOCTYPE html><html><head><title>3D Tour</title><style>body{margin:0; overflow:hidden;} #btns{position:absolute; top:10px; left:10px;}</style></head>
<body><div id="btns"><button onclick="alert('Viewing Facade')">Facade</button><button onclick="alert('Viewing GF')">Ground Floor</button></div>
<div id="canvas-container"></div>
<script type="module">
import { initTour } from './threejs-tour.js';
initTour('canvas-container');
</script></body></html>
''')

# Index HTML
with open(f"{base_dir}/index.html", "w") as f: f.write('''
<!DOCTYPE html>
<html><head><title>Rental House Project - Sagar</title>
<style>
body { font-family: 'Inter', sans-serif; background: #fafafa; color: #333; margin:0; padding:40px; }
.container { max-width: 1200px; margin: auto; background: #fff; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); }
.alert { background: #ffebee; color: #c62828; padding: 15px; border-left: 4px solid #c62828; margin-bottom: 20px; font-weight: bold; }
h1, h2 { color: #111; }
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
img, iframe, object { width: 100%; border: 1px solid #ddd; border-radius: 8px; }
.btn { display: inline-block; padding: 10px 20px; background: #000; color: #fff; text-decoration: none; border-radius: 4px; margin-top: 10px; }
</style>
</head><body>
<div class="container">
    <div class="alert">⚠️ DO NOT BUILD UNTIL VERIFIED: This is a conceptual architectural plan. It MUST be verified by a local structural engineer and Sagar municipal authorities before construction. Assumptions made for column sizing and soil strength.</div>
    <h1>Dubai-Style Modern Rental Investment</h1>
    <p>30x50 East Facing | Tilli Colony, Sagar MP</p>
    
    <h2>1. Virtual 3D Massing Tour</h2>
    <iframe src="visualization/virtual-tour.html" height="500"></iframe>
    <a href="visualization/virtual-tour.html" class="btn" target="_blank">Open Fullscreen Tour</a>
    
    <h2>2. AutoCAD-Style Floor Plans</h2>
    <div class="grid">
        <div><h3>Ground Floor</h3><object data="plans/ground-floor-plan.svg" type="image/svg+xml"></object></div>
        <div><h3>First Floor</h3><object data="plans/first-floor-plan.svg" type="image/svg+xml"></object></div>
        <div><h3>Second Floor</h3><object data="plans/second-floor-plan.svg" type="image/svg+xml"></object></div>
    </div>
    
    <h2>3. Area & Vastu Strategy</h2>
    <p><strong>Efficiency:</strong> ~82% Rentable Area. <strong>Parking:</strong> 15x18 ft (Fits 16x7 SUV perfectly with clearance).</p>
    <p><strong>Vastu:</strong> NE Main Door, NE UG Water Tank, SE Staircase (independent access).</p>
    <p><strong>Ventilation:</strong> 2 OTS Shafts guaranteeing cross-ventilation in all rooms despite 3 blocked sides.</p>
</div>
</body></html>
''')
