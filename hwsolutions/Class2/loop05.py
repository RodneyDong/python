def normalList (a,b):
    list1 = []
    for x in range (a,b+1):
        list1.append(x)
    return list1
def reverseList (a,b):
    list1 = []
    for x in range (a,b):
        list1.append(x)
    list1.reverse()
    return list1
num1 = 1
num2 = 5
a = normalList(num1,num2)
b = reverseList(num1,num2)
x = '* '
z = ' '
print(a)
print(b)
for y in a:
    print(z*(max(a)-y),x*y)
for i in b:
    print(z*(max(b)-i+1),x*i)