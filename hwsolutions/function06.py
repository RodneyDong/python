def addList (a,b):
    newList = []
    for x in range (len(a)):
        newList.append(a[x]+b[x])
    return newList
l1 = [1,2,3]
l2 = [4,5,6]
print(addList(l1,l2))