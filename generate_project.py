import os
import json

base_dir = "/Users/vineetpathak/Documents/New project/AntiGravity/rental-house-sagar"
for d in ["plans", "data", "visualization", "docs"]: os.makedirs(os.path.join(base_dir, d), exist_ok=True)

def svg_wrap(content, title):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" width="900" height="600" style="background:#fff; border: 1px solid #ccc; font-family: monospace;">
    <rect width="100%" height="100%" fill="#ffffff" />
    <g transform="translate(50, 50)">
        <text x="0" y="-20" font-size="20" font-weight="bold" fill="#333">{title}</text>
        {content}
    </g>
    <g transform="translate(850, 50)">
        <circle cx="0" cy="0" r="15" fill="none" stroke="#333" stroke-width="2"/>
        <polygon points="-5,5 5,5 0,-15" fill="#333"/>
        <text x="0" y="25" text-anchor="middle" font-size="12" font-weight="bold">N</text>
    </g>
</svg>'''

def rect(x, y, w, h, fill="#fdfdfd", stroke="#000", lw=2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="{lw}"/>\\n'

def text(x, y, t, s=12, w="normal", fill="#000", a="middle", r=0):
    tr = f' transform="rotate({r} {x} {y})"' if r else ""
    return f'<text x="{x}" y="{y}" font-size="{s}" font-weight="{w}" fill="{fill}" text-anchor="{a}"{tr}>{t}</text>\\n'

def line(x1, y1, x2, y2, stroke="#000", lw=2, dash=""):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{lw}"{da}/>\\n'

def draw_door(x, y, r, rot):
    return f'<g transform="translate({x},{y}) rotate({rot})"><path d="M 0 0 L {r} 0 A {r} {r} 0 0 1 0 {r} Z" fill="none" stroke="#f44336" stroke-width="2"/></g>\\n'

def draw_window(x, y, w, h):
    return rect(x, y, w, h, fill="#e0f7fa", stroke="#00bcd4", lw=1) + line(x, y+h/2, x+w, y+h/2, stroke="#00bcd4", lw=1)

def draw_gf():
    c = rect(0, 0, 500, 300, fill="none", lw=4)
    c += text(520, 150, "30 FT ROAD (EAST)", 16, "bold", r=90)
    c += line(500, -20, 500, 320, stroke="#999", lw=2, dash="5,5")
    
    # 1. PARKING & STAIRS (Front 15ft = X: 350-500)
    c += rect(350, 0, 150, 170, fill="#e8f5e9") # Parking
    c += text(425, 60, "SUV PARKING", 14, "bold")
    c += text(425, 75, "15' x 17'")
    c += rect(370, 90, 110, 60, fill="#cfd8dc", stroke="#999", lw=2)
    c += text(425, 120, "SUV (16'x7')", 10)
    
    c += rect(350, 170, 150, 60, fill="#fff") # Passage
    c += text(425, 200, "TENANT PASSAGE (15'x6')", 10)
    c += rect(480, 170, 20, 60, fill="#ffcc80") # Meters
    c += text(490, 200, "METERS", 8, "bold", r=90)
    
    c += rect(350, 230, 150, 70, fill="#f5f5f5") # Stairs
    c += text(425, 265, "STAIRS (UP)", 12, "bold")
    for i in range(15): c += line(350+i*10, 230, 350+i*10, 300, stroke="#ccc", lw=1)

    # 2. LIVING & KITCHEN (Middle 10-20ft = X: 150-350)
    c += rect(250, 0, 100, 170, fill="#fff") # Living
    c += text(300, 80, "LIVING ROOM", 14, "bold")
    c += text(300, 95, "10' x 17'")
    c += text(270, 140, "[TV Wall]", 10, fill="#999", r=-90)
    c += text(335, 120, "◄ MAIN ENTRANCE", 10, "bold", fill="#d32f2f", r=-90)
    
    c += rect(150, 170, 200, 130, fill="#fff3e0") # Kitchen
    c += text(250, 230, "KITCHEN AND DINING", 14, "bold")
    c += text(250, 245, "20' x 13'")
    c += rect(150, 170, 180, 20, fill="#eee", stroke="#ccc")
    c += text(200, 180, "[Stove]", 10, fill="#d32f2f")
    c += text(300, 180, "[Sink]", 10, fill="#1976d2")
    c += text(335, 210, "◄ BACK DOOR", 8, fill="#666", r=-90)

    # 3. BEDROOMS & BATHS (Rear 15-25ft = X: 0-250)
    c += rect(0, 0, 150, 120, fill="#fafafa") # Bed 2
    c += text(75, 55, "BEDROOM 2", 14, "bold")
    c += text(75, 70, "15' x 12'")
    
    c += rect(0, 170, 150, 130, fill="#fafafa") # Master Bed
    c += text(75, 230, "MASTER BEDROOM", 14, "bold")
    c += text(75, 245, "15' x 13'")
    
    c += rect(150, 0, 50, 50, fill="#eceff1") # OTS 1
    c += line(150,0,200,50, stroke="#999"); c += line(150,50,200,0, stroke="#999")
    c += text(175, 25, "OTS", 10)
    
    c += rect(200, 0, 50, 70, fill="#e3f2fd") # C.Bath
    c += text(225, 30, "C.BATH", 10, "bold")
    c += text(225, 45, "5'x7'", 10)
    
    # Corridor and inner baths (Y=120-170)
    c += rect(0, 120, 40, 50, fill="#eceff1") # OTS 2
    c += line(0,120,40,170, stroke="#999"); c += line(0,170,40,120, stroke="#999")
    
    c += rect(40, 120, 60, 50, fill="#e3f2fd") # Att Bath
    c += text(70, 140, "BATH", 10, "bold")
    c += text(70, 155, "6'x5'", 10)
    
    c += rect(100, 120, 50, 50, fill="#fff") # Inner Corridor
    c += rect(150, 50, 50, 120, fill="#fff") # Main Corridor 1
    c += rect(200, 70, 50, 100, fill="#fff") # Main Corridor 2
    c += text(180, 120, "CORRIDOR", 10, "bold")

    # Walls
    c += line(150, 0, 150, 120, lw=4) # Bed2 East
    c += line(150, 170, 150, 300, lw=4) # MBed East
    c += line(200, 0, 200, 70, lw=4) # Cbath West
    c += line(250, 0, 250, 170, lw=4) # Living West
    c += line(350, 0, 350, 300, lw=4) # Front Wall
    c += line(0, 120, 200, 120, lw=4) # Bed2 South
    c += line(0, 170, 350, 170, lw=4) # MBed/Kitchen North
    
    # Internal Flow / Doors
    c += draw_door(350, 100, 40, 180) # Main Door (Into Living)
    c += draw_door(350, 200, 30, 180) # Back Door (Into Kitchen)
    
    # Living to Kitchen Arch (Y=170)
    c += line(280, 170, 320, 170, lw=4, stroke="#fff") # Erase wall
    c += line(280, 170, 320, 170, lw=2, dash="5,5", stroke="#f44336") # Arch
    c += text(300, 175, "ARCHWAY", 8, fill="#d32f2f")
    
    # Corridor to Living Arch (X=250)
    c += line(250, 100, 250, 140, lw=4, stroke="#fff") # Erase wall
    c += line(250, 100, 250, 140, lw=2, dash="5,5", stroke="#f44336") # Arch
    c += text(255, 120, "ARCH", 8, fill="#d32f2f", r=-90)

    # Room Doors
    c += draw_door(150, 80, 30, 180) # Bed 2 (Hinge 150,80. Inward left-up)
    c += draw_door(150, 200, 30, 180) # Master Bed (Hinge 150,200. Inward left-up)
    c += draw_door(250, 50, 30, 180) # C.Bath (Hinge 250,50 on X=250? No, C.Bath is at X=200-250, Y=0-70. Door at 200, 50. Inward right-up = rot -90)
    c += draw_door(200, 50, 30, -90) # C.Bath
    c += draw_door(100, 140, 30, 180) # Att Bath (Hinge 100,140. Inward left-up)
    
    return svg_wrap(c, "GROUND FLOOR PLAN (FLAWLESS 2BHK FLOW)")

def draw_ff():
    c = rect(0, 0, 500, 300, fill="none", lw=4)
    # Shafts & Stairs same
    c += rect(0, 120, 40, 50, fill="#eceff1")
    c += line(0, 120, 40, 170, stroke="#999"); c += line(0, 170, 40, 120, stroke="#999")
    c += rect(150, 0, 50, 50, fill="#eceff1")
    c += line(150, 0, 200, 50, stroke="#999"); c += line(150, 50, 200, 0, stroke="#999")
    c += rect(350, 230, 150, 70, fill="#f5f5f5")
    for i in range(15): c += line(350+i*10, 230, 350+i*10, 300, stroke="#ccc", lw=1)
    
    # 1BHK
    c += rect(0, 170, 150, 130, fill="#fafafa") # Bed
    c += text(75, 230, "1BHK BEDROOM", 14, "bold")
    c += rect(40, 120, 110, 50, fill="#e3f2fd") # Bath
    c += text(95, 145, "1BHK BATH", 12, "bold")
    c += rect(150, 170, 200, 130, fill="#fff") # Living
    c += text(250, 230, "1BHK LIVING", 14, "bold")
    c += rect(150, 50, 100, 120, fill="#fff3e0") # Kitchen
    c += text(200, 110, "1BHK KITCHEN", 12, "bold")
    
    c += rect(350, 170, 100, 60, fill="#fff") # Lobby
    c += text(400, 200, "STAIR LOBBY", 12, "bold")
    
    # Single Room
    c += rect(0, 0, 150, 120, fill="#fafafa") # SR Bed
    c += text(75, 50, "SR BED/LIVING", 14, "bold")
    c += rect(200, 0, 50, 90, fill="#e3f2fd") # SR Bath
    c += text(225, 40, "SR BATH", 10, "bold")
    c += rect(250, 0, 200, 170, fill="#fafafa") # SR Room / Kitchenette
    c += text(350, 80, "SINGLE ROOM UNIT", 14, "bold")
    
    c += rect(450, 0, 50, 230, fill="#e0f7fa") # Balcony
    c += text(475, 115, "EAST BALCONY", 14, "bold", r=90)
    
    # Doors
    c += draw_door(350, 210, 30, 90) # 1BHK Main
    c += draw_door(350, 170, 30, 180) # SR Main 
    c += draw_door(450, 115, 30, 0) # SR to Balcony
    c += draw_door(450, 210, 30, 0) # 1BHK to Balcony
    
    return svg_wrap(c, "FIRST FLOOR PLAN (1BHK + SINGLE ROOM)")

def draw_sf():
    c = rect(0, 0, 500, 300, fill="none", lw=4)
    # Shafts & Stairs same
    c += rect(0, 120, 40, 50, fill="#eceff1")
    c += line(0, 120, 40, 170, stroke="#999"); c += line(0, 170, 40, 120, stroke="#999")
    c += rect(150, 0, 50, 50, fill="#eceff1")
    c += line(150, 0, 200, 50, stroke="#999"); c += line(150, 50, 200, 0, stroke="#999")
    c += rect(350, 230, 150, 70, fill="#f5f5f5")
    for i in range(15): c += line(350+i*10, 230, 350+i*10, 300, stroke="#ccc", lw=1)
    
    c += rect(200, 170, 150, 130, fill="#fafafa") # Studio Room
    c += text(275, 230, "STUDIO ROOM", 14, "bold")
    c += rect(150, 170, 50, 130, fill="#e3f2fd") # Studio Bath
    c += text(175, 235, "BATH", 10, "bold")
    
    c += rect(0, 0, 150, 120, fill="#e8f5e9")
    c += rect(40, 120, 110, 50, fill="#e8f5e9")
    c += rect(0, 170, 150, 130, fill="#e8f5e9")
    c += rect(150, 50, 200, 120, fill="#e8f5e9")
    c += rect(200, 0, 300, 170, fill="#e8f5e9")
    c += rect(350, 170, 150, 60, fill="#e8f5e9")
    c += text(200, 100, "OPEN TERRACE / DRYING AREA", 16, "bold")
    
    c += rect(370, 240, 40, 40, fill="#1565c0") # OHT
    c += text(390, 260, "OHT", 10, fill="#fff")
    
    c += draw_door(350, 210, 30, 90) # Studio Main
    c += draw_door(300, 170, 30, 180) # Studio to Terrace
    c += draw_door(350, 230, 30, 180) # Stairs to Terrace
    
    return svg_wrap(c, "SECOND FLOOR PLAN (STUDIO + TERRACE)")

with open(f"{base_dir}/plans/ground-floor-plan.svg", "w") as f: f.write(draw_gf())
with open(f"{base_dir}/plans/first-floor-plan.svg", "w") as f: f.write(draw_ff())
with open(f"{base_dir}/plans/second-floor-plan.svg", "w") as f: f.write(draw_sf())
