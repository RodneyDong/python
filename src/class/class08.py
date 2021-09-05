'''
property
'''
class Robot:
    id = 12345
    def __init__(self,newname=None, energy=1000):
        self.name = newname
        self.__energy = energy #__energy is a private attribute in this class
    # The dunder(__) is the key for encapsulation
    def __repr__(self):
        return self.name + ":" + str(self.__energy)

    def hi(self):
        if self.name:
            print(f"Hi, I am {self.name}")
        else:
            print("Hi, I have no name")

    def getEnergy(self): # Get the protected __energy variable
        return self.__energy
    
    def setEnergy(self,newenergy): # You can set a if-else to protect the variable
        self.__energy = newenergy
    
    def getName(self):
        return self.__name
    
    def setName(self,name):
        self.__name = name
    
    def delName(self):
        del self.__name

    name = property(getName, setName, delName)

if __name__ == '__main__':
    r = Robot("john")
    print(r.name) # try get name from r
    r.name = "Rodney" # assign new value called setter
    print(r)

    del r.name # del will call delName() function
    print(r)