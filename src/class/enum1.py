import enum

class Color(enum.Enum):
    RED = 1 # constand, class level attribute
    GREEN = 2
    BLUE = 3
if __name__ == '__main__':
    print(Color.RED)
    