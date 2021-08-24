"""
pass a function to another function
"""
def add(a,b):
    return a + b

def mul(a,b):
    return a * b

def ff(f, x, y):
    return f(x, y)

if __name__ == '__main__':
    x = ff(mul, 3, 4) # 中央决定GDP一年翻两翻（ff），中央不确定各个省如何办到
    print(x)