primeList = []
for x in range (1,50):
    isprime = True 
    for i in range (2,x//2+1):
        if (x % i) == 0:
            isprime = False
            break
    if isprime and x!=1 and x!=0:
        primeList.append(x)
print(primeList)