from math import pi
def cylinderVolume(r,h):
    v = pi*r*r*h
    return v
radius = 10
height = 10
ans = cylinderVolume(radius,height)
print("Cylinder volume with radius {0} and height {1} is {2}".format(radius,height,ans))