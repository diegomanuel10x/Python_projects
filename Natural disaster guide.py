print("Welcome to your natural disaster guide!")

print("""
1.Flood
2.Storm
3.Landslide
4.Wildfire
5.Earfquake
""")

disaster = input("Which of the disasters above are you facing(Enter the number): ")

choice = int(disaster)

if not disaster.isdigit():
    print("We expect ou to enter a whole number!")

if choice not in range(1,6):
    print("We expect a number between 1 and 5!")

elif choice == 1:
    print("To stay safe during a flood, prepare by creating a to go bag with essentials, elevating home utilities, and signing up for emergency alerts. During the event, seek higher ground immediately and follow the rule Turn Around, Don't Drown—never walk or drive through floodwaters, as even a few inches can sweep you away. Once the water recedes, avoid contact with floodwater, which is often contaminated, and only return home when officials declare it safe. Always wear protective gear during cleanup to avoid mold and electrical hazards.")

elif choice == 2:
    print("""
    To stay safe during a storm, prepare by securing loose outdoor objects, trimming overhanging branches, and identifying a sturdy, windowless interior room for shelter. When the storm hits, stay indoors and away from windows, glass doors, and electrical appliances, as lightning can travel through wiring and plumbing. If you are caught outside, immediately seek shelter in a substantial building or a hard-top vehicle, avoiding tall trees, open spaces, and metal objects. After the storm, remain cautious of fallen power lines, weakened structures, and contaminated water, and only attempt repairs or travel once authorities confirm it is safe. 
    """)

elif choice == 3:
    print("""
    To stay safe during a landslide, prepare by identifying steep slopes or drainage ways near your home and learning the local emergency evacuation plans. During the event, evacuate immediately if you hear rumbling, see trees tilting, or notice sudden changes in water flow; if trapped indoors, move to the highest floor and curl into a ball to protect your head. Avoid river valleys and low-lying areas where debris flows naturally accumulate. After the slide, stay away from the impacted area, as secondary slides are common, and check for damaged utility lines or structural cracks before re-entering any building.
    """)

elif choice == 4:
    print("""
    To stay safe during a wildfire, prepare by creating a defensible space around your home by clearing flammable vegetation and packing a go-kit with N95 masks and medications. If a fire approaches, evacuate immediately when ordered; if trapped, stay indoors, close all windows to block embers, and turn on all lights to help rescuers find you in the smoke. To protect yourself from heat and sparks, wear protective clothing made of natural fibers like cotton. After the fire, wait for official clearance before returning to avoid hazards like hot ash pits and downed power lines.
    """)

elif choice == 5:
    print("""
    To stay safe during an earthquake, prepare by securing heavy furniture to walls and identifying safe spots in each room, such as under sturdy tables. When the shaking begins, drop, cover, and hold on by getting on your hands and knees, covering your head and neck with your arms, and staying under cover until the shaking stops. If you are outdoors, move to an open area away from buildings, streetlights, and utility wires to avoid falling debris. After the earthquake, be alert for aftershocks and check for gas leaks or structural damage before using any utilities or re-entering buildings.""")

else:
    print("An error has occured!")

