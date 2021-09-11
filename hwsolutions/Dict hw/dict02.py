vehicle = {
    "model" : "VX322",
    "year" : "2021",
    "mileage" : "40000"
}
x = 'year'
a = vehicle.get(x)
print(f"The year of the vehicle is: {a}")
vehicle["year"] = 2020
vehicle["type"] = "motorcycle"
print(vehicle)
