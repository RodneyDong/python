from math import pi

def circleArea(radius):
    if radius<0:
        raise ValueError(f"the radius must be positive number. You give {radius}")
    return pi*radius**2

if __name__ == '__main__':
    try:
        r = 1.1
        area = circleArea(r)
        print(area)
    except: # not necessary grab the error.
        print("failed")
    print("Done.")