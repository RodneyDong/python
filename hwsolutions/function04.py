from math import pi
def cylinderVolume(r,h):
    v = pi*r*r*h
    return v
radius = 10
height = 10
ans = cylinderVolume(radius,height)
print("Cylinder volume with radius {} and height {} is {}".format(radius,height,ans))