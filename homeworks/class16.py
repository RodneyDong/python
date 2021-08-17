"""
class inheritance, review class level attribute
"""

class Superclass:
    def __init__(self, a):
        self.instance = a

    def __repr__(self):
        return self.instancedata

    def superFunc(self):
        print("subFunc() is running...")

class Subclass(Superclass): # Subclass inherits from Superclass
    def subFunc(selF):
        print("subFunc() is running...")

if __name__ == '__main__':
    obji = Superclass('Super1')
    obji.

