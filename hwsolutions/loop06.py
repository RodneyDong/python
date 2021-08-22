primeList = []
prime = True
for x in range (0,50):
    for i in range (2,10):
        if (x % i) == 0:
            prime = False
            break
        else:
            prime = True
    if prime == True:
        primeList.append(x)
print(primeList)