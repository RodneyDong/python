"""
__new__(cls): object constructor, avoid override this function unless you have to
__init__(self): initializing the object
"""

class A:
    def __new__(cls, name): # constructor to create a new object
        print("A.__new__ is called")
        return super(A,cls).__new__(cls) # call super class __new__(cls)

    def __init__(self,name): # initializing the object
        print("__init__ is called")
        self.name = name

    def __repr__(self): # return a string representate
        return self.name

    def add(self, x, y):
        return x+y

if __name__ == '__main__':
    a = A("John")
    print(a)
    x = a.add(4,5)
    print(x)