"""
❗️⚡️User may pass wrong argument to function.
raise Error when bad thing happens.
"""
from math import pi

def circle_area(r):
    if type(r) in [int, float]:
        return r * r * pi
    raise TypeError("Please check radius data type.")


if __name__ == '__main__': 
    x = circle_area(2-3j) # 😢without check the calling argument, give you meaningless output
    print(x)
    print("Done.")