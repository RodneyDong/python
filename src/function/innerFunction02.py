"""
Define functions in function, scope of attribute
https://www.javatpoint.com/python-decorator
"""
def Scope_test():
    def do_local():
        spam = "local spam" # parent function assignment will not override this value
        print(f"Local variable: {spam}")

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam" # this is parent variable assignment

    def do_global():
        global spam
        spam = "global spam" # global variable assignment, will not change local variable

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

if(__name__ == "__main__"):

    scope_test()
    print("In global scope:", spam) # global variable