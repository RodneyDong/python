def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

# why need // operator?

if __name__ == '__main__':
    a,b=40,15
    c = add(a,b)
    print(f"{a} + {b} = {c}")
    c=div(a,b)
    print(f"{a} \u00F7 {b} = {c:.3f}")    
