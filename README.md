# Rental Investment House Concept - Tilli Colony, Sagar MP

Editable concept package for an east-facing 30 ft x 50 ft rental-investment house in Tilli Colony, Sagar, Madhya Pradesh.

## What This Contains

- `index.html` - polished one-page concept and marketing sheet.
- `plans/ground-floor-plan.svg` - ground floor 2BHK, parking, stair, services, and appliance locations.
- `plans/first-floor-plan.svg` - first floor 1BHK, single-room unit, balcony, utility, and service zones.
- `plans/second-floor-plan.svg` - caretaker studio, terrace, utility, stair access, and overhead tank concept.
- `plans/one-page-concept-sheet.svg` - combined sheet for review meetings.
- `visualization/virtual-tour.html` - simple Three.js 3D massing tour.
- `data/*.json` - room schedule, Vastu checklist, validation checklist, dimensions, and camera scene data.
- `docs/*.md` - architect questions, buildability notes, validation report, and water/electricity notes.

## Project Assumptions

- Plot size is 30 ft frontage by 50 ft depth, total 1500 sq ft.
- East side is open to a 30 ft road; north, south, and west sides are assumed blocked or built up.
- The concept prioritizes rental value, independent access, common stair movement, stacked plumbing, and heat-conscious ventilation.
- Future one-floor expansion is an intent only. It must be confirmed through structural design for columns, beams, footings, slab loads, staircase headroom, and local approvals.
- Room dimensions are approximate planning dimensions and do not include final wall thickness, column offsets, site tolerances, or municipal setbacks.

## How To Open

Open `index.html` in a browser, or serve the folder locally:

```bash
python3 -m http.server 4175
```

Then open `http://127.0.0.1:4175/`.

The SVG files can be opened directly in any browser or edited in vector tools. The JSON files are intended for review, validation, and future automation.

## Validation Summary

The concept represents the requested building program:

- Ground floor: independent 2BHK, two bathrooms, pooja, covered SUV parking, two to three bike parking, appliance positions, separate entry, and common stair.
- First floor: independent 1BHK, independent single room with attached washroom, east balcony, utility/washing area, and appliance positions.
- Second floor: caretaker/studio unit, kitchenette, washroom, terrace access, drying/wash area, and overhead tank concept.
- Services: separate meter zone, underground sump plus pump and overhead tank, stacked wet areas, and ventilation shafts.

Remaining checks before finalization:

- Municipal setbacks and balcony projection rules.
- Existing or proposed column grid and foundation capacity.
- Soil, drainage, sewer, water pressure, and electricity meter regulations.
- Staircase feasibility, fire/safety access, waterproofing, and terrace slope.
- Structural design for the intended future floor.

## Critical Warning

This is not a final construction drawing. Do not build from this package. A local architect, licensed structural engineer, MEP consultant where required, and Sagar municipal approval are mandatory before construction.
