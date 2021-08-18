"""
A List is an ordered collection of Python objects that is iterable,
mutable, separated by commas, surrounded by []. 方数组

l1 = [1,2,3,4]
"""

# Create list
l1=[]
l1=list()
print(type(l1))
print(len(l1))
print(l1)
l1 = [1,2,3,4,54,34,121,2,1]
print(l1)
l1 = [i for i in range(1,11)]
print(l1)
l1 = list(range(10))
print(l1)
l1 = list("hello")
print(l1)
t=(1,2,3)
l1 = list(t)
print(l1)

# nested list
faces = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
suits = ("Spade", "Club", "Diamond", "Heart")
cards = [(face, suit) for face in faces for suit in suits]
print(len(cards))
#print(cards)

# list slicing
print(cards[4:8])
l1 = [1,2,3,4,5]
x = l1[0] # get single element from the list
print(x)
x = l1[::2] # get sublist from the  [[start=0]:[stop=end]:[step=1]]
print(x)
x=l1[::-1] # reverse the 
print(l1)
print(x)

# modify list (append,insert)
l1[3]=100 # modify single element in the list
print(l1)
l1.append(11)
print(l1)
l1.insert(2,11) # insert new element before the given index
print(l1)
l1.remove(11) # remove value NOT index
print(l1)
x = l1.pop() # LIFO: stack, FIFO: queue
print(l1)
print(x)
l2=[7,8,9]
l1.extend(l2)
print(l1)
l1.extend("WORLD")
print(l1)

# +, * on list
l1=[1,2,3]
list1 = l1 + l2
print(list1)
list1 = l1*3
print(list1)
print(*l1, *l2)

c = list(zip(l1, l2))
print(c)
