def reverseList (b,a):
    list1 = []
    for x in range (a,b):
        list1.append(x)
    list1.reverse()
    return list1
x = '* '
a = reverseList (6,1)
for y in a:
    print(x*y)