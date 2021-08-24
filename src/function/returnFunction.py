"""
🔥a function can return a function
"""
# function return a function
def quadratic(a,b,c):
    def f(x):
        return a*x*x + b*x + c
    return f

if __name__ == '__main__':
    a,b,c=3, 2, -5
    f = quadratic(a, b, c)
    x = 3
    print(f"quadratic function with cofficients of ({a},{b},{c}) returns {f(x)} when x={x}")