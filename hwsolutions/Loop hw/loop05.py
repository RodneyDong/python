# def normalList (a,b):
#     list1 = []
#     for x in range (a,b+1):
#         list1.append(x)
#     return list1
# def reverseList (a,b):
#     list1 = []
#     for x in range (a,b):
#         list1.append(x)
#     list1.reverse()
#     return list1
num1 = 1
num2 = 5
# a = normalList(num1,num2)
# print(a)
# b = reverseList(num1,num2)
# print(b)
#a = [i for i in range(num1, num2+1)]
# b = [i for i in range(num2-1, num1-1, -1)]
# print(a)
# print(b)
# x = '* '
# z = ' '
for y in range(1, num2+1):
    print(' '*(num2+1-y),'* '*y)
for y in range(num2-1, num1-1, -1):
    print(' '*(num2-y+1),'* '*y)
