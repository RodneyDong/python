"""
A function is a block of organized, reusable code 
that is used to perform a single, related action.
* function name
* argument list
* function do nothing till you call it.

1. Python built-in functions
print()
len()
sum()
2. User defined function

def <functionName>(arguments):
    pass

"""

# define a function, single responsibility?
def printName(firstName, lastName):
    print(f"First Name: '{firstName}', Last Name: '{lastName}'.")

# call function
printName("Roy", "Huang")
printName("Huang", "Roy")

def printName(x): # override previously defined function
    print(f"Hello, {x}")

# printName("Roy", "Huang")
printName("Roy Huang")

# built-in function can be overridden too.
x = len("Hello")
print(x)

def len():
    print("Hello, world.")

# x = len("Hello") # len() has been overriden, no longer works the way you expected.

from math import pi
def circleArea(radius):
    return pi * radius**2

area = circleArea(1)
print(f"area = {area}")

area = circleArea(2)
print(f"area = {area}")

r = 1
area = circleArea(r)
print(f"circle_area(radius={r}) = {area:.3f}")

# function can take no argument, and return more than one value
def getName():
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    return firstName, lastName

# x = getName()
# print(x)
# print(f"Your first name: {x[0]}, and last name: {x[1]}")

# it works, but not single response function which is a bad design
def area(x):
    circleArea = pi * x**2
    squareArea = x**2
    return {"x":x, "circleArea":circleArea, "squareArea": squareArea}

y = area(4)
print(y)

def printCountry(country="unknown contry"): # give a default value
    print(country)

printCountry('China')
printCountry('United States')
printCountry()
