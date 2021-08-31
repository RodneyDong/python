class Robot:
    id = 12345
    def __init__(self,newname): # self is everything in the "class", mandatory argument for functions in class
        self.name = newname

    def __init1__(self,newname1):
        self.name = newname1

    def __repr__(self):
        return self.name

    def hi(self):
        print(f"Hi, I am {self.name}")

    def hi1(self):
        print(f"Hi, I am {self.name}")

if __name__ == '__main__':
    r = Robot("John") # 只调动__init__
    r.hi()
    r.__init1__("Rodney")
    r.hi1()
    print(Robot())