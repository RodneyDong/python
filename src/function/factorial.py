def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1) # adjust the value of n

def f(n):
    result = 1
    while n>1:
        result *=n
        n -= 1
    return result

if __name__ == '__main__':
    n = 6
    result = factorial(n)
    print(f"The factorial of {n} is {result}.")
    result = f(n)
    print(f"The factorial of {n} is {result}.")

