'''
1. start from 1, include stop
2. pass start, stop, step
'''
class range1:
    def __init__(self, *args):
        self.start = 1
        self.step = 1
        if len(args) < 1 or len(args) > 3:
            raise ValueError("argument number has to be 1,2 or 3")
        if len(args) == 1:
            self.stop = args[0]
        if len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
        if len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
    
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current > self.stop:
            raise StopIteration
        result = self.current
        self.current += self.step
        return result
    
        

def f(*args):
    print(args)

if __name__ == '__main__':
    for i in range1():
        print(i)
