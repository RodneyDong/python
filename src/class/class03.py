class Robot:
    id = 12345
    def hi(self):
        print(f"Hi, I am {self.name}")
if __name__ == '__main__':
    r = Robot()
    print(isinstance(r, Robot)) # If r and Robot is the same class, it will return True
    r.name = "Rodney"
    r.hi()