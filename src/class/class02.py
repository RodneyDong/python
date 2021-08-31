def hi(obj):
    print("Hi I am " + obj.name)
class Robot:
    pass
if __name__ == '__main__':
    r = Robot()
    r.name = "john"
    hi(r)