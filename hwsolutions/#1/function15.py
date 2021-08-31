def removeValue(a,b):
    l1 = []
    for x in a: # for-each loop
        if x != b:
            l1.append(x)
    return l1

list1 = [1,1,2,3,1,4,2]
print(removeValue(list1,1))

