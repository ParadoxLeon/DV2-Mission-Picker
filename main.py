import random

missionlist = [
"Grand Washington Hotel (Invaded)",
"Jefferson Trade Center (Invaded)",
"ViewPoint Museum (Invaded)",
"American History Museum (Invaded)",
"Air & Space Museum (Invaded)",
"Jefferson Plaza (Invaded)",
"Bank Headquarters (Invaded)",
"DCD Headquarters (Invaded)",
"Lincoln Memorial (Invaded)",
"Potomac Event Center (Invaded)",
"Federal Emergency Bunker (Invaded)",
"District Union Arena (Invaded)",
"Roosevelt Island (Invaded)",
"Capitol Building (Invaded)",
"Camp White Oak (Invaded)",
"Manning National Zoo (Invaded)",
"Invaded Space Administration HQ (Invaded)",
"Grand Washington Hotel",
"ViewPoint Museum",
"American History Museum",
"Air & Space Museum",
"Bank Headquarters",
"DCD Headquarters",
"Lincoln Memorial",
"Potomac Event Center",
"Jefferson Trade Center",
"Space Administration HQ",
"Federal Emergency Bunker",
"Camp White Oak",
"The Pentagon",
"DARPA Research Labs",
"Coney Island Ballpark",
"Coney Island Amusement Park",
"The Tombs",
"Stranded Tanker",
"Pathway Park",
"Wall Street",
"Liberty Island",
"District Union Arena",
"Roosevelt Island",
"Capitol Building",
"Tidal Basin",
"Manning National Zoo",
]
print(random.choice(missionlist))
for i in missionlist:
    print("reroll? y/n")
    x = input()
    if x == "y":
        print(random.choice(missionlist))
    elif x == "n":
        break
