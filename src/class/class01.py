class Robot: # user defined data type
    pass

if __name__ == '__main__':
    r1 = Robot() # call default constructor to create an object of Robot class
    r2 = Robot()
    print(type(r1))
    print(r1==r2)

    r1.name = "Marvin"
    r1.buildYear = 1995

    r2.name = "John"
    r2.buildYear = 2021

    print(r1.name)
    print(r2.name)
    
    Robot.brand = "GE" # class level attribute
    print(r1.brand)
    print(r2.brand)

    Robot.brand = "Boyn" # class level attribute
    print(r1.brand)
    print(r2.brand)

    r1.brand = "Texas" # instance level attribute override class level attribute
    print(r1.brand)
    print(r2.brand)

    r1.energy = "2000"
    z = getattr(r1, 'energy', 1000)
    print(z)
