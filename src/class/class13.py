# Define a function outside class

def f1(self, x, y):
    return min(x,y)

class A:
    f = f1
    def g(self):
        return 'hello, world'

class B:
    fb = f1
    def add(self, x, y):
        return x+y

if __name__ == '__main__':
    x = f1(2,4,5)
    print(x)
    a = A()
    x = a.f(3,-2)
    print(x)
    b = B()
    x = b.fb(5,4)
    print(x)