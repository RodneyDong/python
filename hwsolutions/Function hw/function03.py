from math import pi
def circle_area (radius):
    answer = radius*radius*pi
    return answer
r = 10
print("Circle area of radius {0} is: {1}".format(r,circle_area(r)))