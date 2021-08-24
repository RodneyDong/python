from math import pi

def circleArea(r):
    assert type(r) in [int, float], f"r should be int or float, but r={r}" 
    assert r > 0,  f"r={r} < 0!"
    return pi*r**2

if __name__ == '__main__':
    try:
        r = '-3'
        print(type(r))
        print(type(r) in [int, float])
        x = circleArea(r)
        print(x)    
    except AssertionError as error:
        print(error)
    print("Done")