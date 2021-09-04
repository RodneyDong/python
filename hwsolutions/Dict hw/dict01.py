locations = {
    "scrowdriver": "shelf1, row2, column3",
    "pliers":"shelf2, row1, column1",
    "circle-saw":"garage shelf, bottom",
    "battery":"Kitchen drawer 1",
}
stuff = input("Please enter the stuff you are looking for: ")

for x in locations:
    if x == a:
        y = locations.get(x)
        print(f"Your {a} are locatied at {y}")
        exit()
print("Your stuff is not located here")

location = locations.get(stuff,None)
if location:
    print(f"Your {stuff} are located at {location}.")
else:
    print("Your stuff is not located here.")
