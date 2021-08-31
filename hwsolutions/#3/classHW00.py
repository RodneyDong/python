class romanNumerals:
    M = 1000
    D = 500
    C = 100
    L = 50
    X = 10
    V = 5
    I = 1
    letters = (M,D,C,L,X,V,I)
    def check (a,b):
        ans = ''
        for x in b:
            if a > x:
                ans += str(x)
                a-x
        print(ans)
z = 2301
r = romanNumerals()
r.check(z,letters)