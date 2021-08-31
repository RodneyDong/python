# Encapsulation: A private variable that cannot be accessed outside
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
if __name__ == '__main__':
    r1 = Robot("John Wang",2000)
    print(r1)
    print(r1.getEnergy())
    r1.setEnergy(3000)
    print(r1.getEnergy())
    