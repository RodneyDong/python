def f1(*args, k1="k1", k2="k2", k3="k3"):
    print("from f1()...")
    for i in args:
        print(i, end=' ')
    print(f"{k1}::{k2}::{k3}")

def get_multiple(*keys, dictionary, default=None):
    print("from get_multiple()...")
    return [dictionary.get(key, default) for key in keys]

def f2(a, b, c=4, *args, **kwargs):
    print("from f2()...")
    print(a, b, c)
    for x in args:
        print(x)
    for x in kwargs:
        print(":".join((x,kwargs.get(x))), end='; ')
    print()

f1(1,"2","3",k1="k1a",k2="k2a",k3="k3a")
f2(1,"2","3",k1="k1a",k2="k2a",k3="k3a")
f2(1,"2",k1="k1a",k2="k2a",k3="k3a")

fruits = {'lemon': 'yellow', 'orange': 'orange', 'tomato': 'red'}
values = get_multiple('lemon', 'tomato', 'squash', dictionary=fruits, default='unknown')
print(values)