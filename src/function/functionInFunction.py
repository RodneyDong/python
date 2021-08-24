"""
🔥Define function inside another function, protect inner function from calling outside.
"""
def parent(a, b, c):
    def child(x, y):
        return x / y
    
    a += child(b, c)
    return a + b + c

if __name__ == '__main__':
    x = parent(3, 4, 5)
    print(x)
    # x = parent.child(4,7) # 😄so called encapsulation, protect child to be called outside
    
    # 💡OOP: Object Oriented Programming has 4 basic features.
    # 1. abstraction   实体模拟
    # 2. inheritance   共性继承
    # 3. polymorphism  异类同功 (回答相同的问题，由于不同的类型，which inherite from same class or interface，而给出不同答案)
    # 4. encapsulation 自我保护