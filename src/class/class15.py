""

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    
if __name__ == '__main__':
    rev = Reverse("International")
    for c in rev:
        print(c, end = '')
    print()

    rev = Reverse([1,2,3,4,5])
    for c in rev:
        print(c, end='')
    print()
    