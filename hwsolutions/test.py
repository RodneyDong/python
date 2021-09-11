class A:
    def __init__(self):
        self.dict1 = {
            'playerOne':2,

        }

    def add(self):
        for x in range(3):
            self.dict1[x] = 0

a = A()
a.add()
print(a.dict1)
a.add()
print(a.dict1)
