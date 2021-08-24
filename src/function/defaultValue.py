def f(x=5): # the default value is evaluated only once
    print(x)

i = 6
f(i)
f(x=19)

# print default value of x
f()

def f1(a, l=[]):
    l.append(a)
    return l

print(f1(1))
print(f1(4))
print(f1(6))

def f2(a, l=None):
    if l is None:
        l = []
    l.append(a)
    return l

print(f2(1))
print(f2(4))
print(f2(6))

l = f2(1)
print(l)
l = f2(4,l)
print(l)
l= f2(6,l)
print(l)

print(f1(3, [3,4,5]))

