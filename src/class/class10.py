from enum import Enum

class Sample():
    def __str__(self):
        return "Sample"

class A():
    def __new__ (cls): # override __new__() can return different type of object
        return Sample()

class Coordinate (bytes, Enum):
    def __new__(cls, value, label, unit): # useful sample code for override __new__()
        obj = bytes.__new__(cls, [value])
        obj._value_ = value 
        obj.label = label
        obj.unit = unit
        return obj

    PX = (0,'Positioin on X.','km')
    PY = (1, 'Position on Y','km')
    VX = (2, 'Velocity on X','km/s')
    VY = (3, 'Velocity on Y', 'km/s')

class Position:
    def __init__(self, x, y):
        self.px = Coordinate.PX
        self.py = Coordinate.PY
        self.x = x
        self.y = y

    def __repr__ (self):
        return f'{self.x}({self.px.unit}), {self.y}({self.py.unit})'

if __name__ == '__main__':
    a = A()
    print(type(a))

    vx = Coordinate.VX
    print(f"label: {vx.label}")
    print(f"unit: {vx.unit}")

    p = Position(12.5, 41.2)
    print(p)
    
    for i in Coordinate:
        print(i)
