
class Bag:
    def __init__(self):
        self.data = []

    def add(self,x):
        self.data.append(x)
    
    def addTwice(self, x):
        self.add(x)
        self.add(x)

if __name__ == '__main__':
    x = Bag()
    x.addTwice("apple")
    x.add("Orange")
    print(x.data)