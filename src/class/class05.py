class Robot:
    id = 12345
    def __init__(self,newname=None):
        self.name = newname

    def __repr__(self):
        return self.name

    def hi(self):
        if self.name:
            print(f"Hi, I am {self.name}")
        else:
            print("Hi, I have no name")
if __name__ == '__main__':
    r1 = Robot("John")
    r1.hi()
    r2 = Robot()
    r2.hi()

