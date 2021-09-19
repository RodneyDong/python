from math import pi

def circleArea(radius):
    if type(radius) not in [int,float]:
        raise TypeError('Radius of a circle must to be int or float')
    if type(radius) < 0:
        raise ValueError("Radius for a circle area cannot to be negative.")
    return radius ** 2 * pi

if __name__ == '__main__':
    x = circleArea(-2+3j)
    print(x)