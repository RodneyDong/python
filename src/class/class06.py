class A:
    def __repr__(self):
        return "John"

    def __str__(self):
        return "Wang"
    
    def __len__(self):
        return 5

if __name__ == '__main__':
    a = A()
    print(a)
    print(repr(a))
    print(str(a))
    print(len(a))