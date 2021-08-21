def removeValue(a,b):
    for x in range (len(a)):
        if a[x] == b:
            a.pop(x)
    return a
list1 = [1,2,3,1,4,2]
print(removeValue(list1,1))
