"""
Good final example how to use timer decorator 
"""
import time

def my_timer(original):
    print(original.__name__)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original(*args, **kwargs)
        t2 = time.time() - t1
        print(f'11: {original.__name__} ran in {t2:.3f} seconds.')
        return result
    return wrapper

@my_timer
def display_info(name, age):
    time.sleep(2) # simulate long process function
    print(f"19: display_info()... run with arguments: ({name}, {age})")

@my_timer
def anotherFunction(todo):
    time.sleep(3)
    print(f"24: anotherFunction()... run with arguments: ({todo})")

if __name__ == '__main__':
    display_info("John", 23)

    anotherFunction("Let's go shopping.")
