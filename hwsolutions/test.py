class A:
    def __init__(self):
        self.list1 = [1]

    def add(self):
        for x in range(3):
            self.dict1[x] = 0

class B(A):
    pass

def player(a):
    if a == '1':
        return a
ans = player('1')
print(ans)
if ans:
    print("done")