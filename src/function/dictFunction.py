"""
function as dictionary value
"""
from math import pi

def circleArea(r):
    return pi * r**2

def squareArea(side):
    return side * side

def triangleArea(base, height):
    return base * height / 2

def rectangleArea(width, length):
    return width * length

areaCalculation = {
    'circle':circleArea, 
    'square':squareArea, 
    'triangle':triangleArea,
    'rectangle':rectangleArea}

if __name__ == '__main__':
    print(areaCalculation['circle'](2))
    print(areaCalculation['triangle'](3,5))
    print(areaCalculation['rectangle'](3,5))
