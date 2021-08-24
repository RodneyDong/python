from math import pi

def circleArea(radius):
    if radius<0:
        raise ValueError(f"the radius must be positive number. You give {radius}")
    return pi*radius**2

if __name__ == '__main__':
    try:
        a = circleArea(1)
        print(a)
        a = circleArea(-2) # this block of code is your test area
        print(a)
    except Exception as error:
        print(error)
    print("Done.")