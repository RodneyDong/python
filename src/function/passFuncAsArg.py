"""
定义简单的一元一次函数
"""
def f1(x):
    return 3*x + 2

def f2(x):
    return 2*x**2+4*x-2

# 类似于中央作五年计划，要求GDP翻两翻，但是靠干什么来翻翻，不确定，走着瞧
def ff(f, x):
    """
    调用ff时才给定function f 和 变量 x
    """
    return f(x)

y = ff(f1, 3)
print(y)
y = ff(f2, 3)
print(y)

# function goal, 应对变化，搞活一盘棋
def userValidate(f, name, password):
    return f(name, password)

# different way to validate user
def validate1(name, password):
    pass

# different way to validate user
def validate2(name, password):
    pass

# define general function pass two arguments
def ff2(f, x,y):
    return f(x,y)

def fib(n):
    """
    this function will print Fibonacci series.
    n: positive integer number
    """
    a, b = 0, 1
    while a < n:
        print(a+b, end=' ')
        a, b = a+1, a+b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def sayHello(name="John"):
    print("Hello, %s!" % name)

def hello(age, firstName="John", lastName="Wang"):
    print("Hello %s %s, you are %d years old." % (firstName, lastName, age))

def test():
    """
    normal call
    """
    fib(20)

    x = fib2(500)
    print(x)

    sayHello()
    sayHello(name="Charles")

    hello(13, "Helen", "Lee")
    hello(13, lastName="Lee", firstName="Helen")

    """
    functional programming call
    """
    ff(fib, 20)
    print(ff(fib2, 20))
    ff(sayHello, 'David')
    ff(hello, 11)

if __name__ == '__main__' :
    test()

