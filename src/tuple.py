"""
A Tuple is an ordered collection of Python objects that is iterable, 
immutable, separated by commas surrounded by ()。圆数组

t1 = (1,2,3,4,5)
"""
# Create tuple
t1=() # empty tuple
t1=tuple()
print(type(t1))
print(len(t1))
t1 = (1, 2, 3, 4, 5)
print(len(t1))
print(t1)
t1 = (1, 2, 3, "hello", (1, 2), 4.5)
print(t1)

# tuple is iterable
for item in t1:
    print(item, end = ', ')
print()

# tuple slicing
x = t1[3]
print(x)
x = t1[::] # [[start]:[stop]:[step]]
print(x)
x = t1[::-1] # count reverse
print(x)

# tuple is immutable
# t1[3] = 'World'
# t1.append(7)

# +, * to generate new tuple from existing
t1 = (1,2,3)
t2 = (4,5,6)
t = t1 + t2
print(t)

t = t1*3
print(t)

t3 = ("firstname","lastname")
t = t3[:1] + t1 + t3[1:]
print(t)

faces = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
suits = ("Spade", "Club", "Diamond", "Heart")
# nested tuple
cards = tuple((face, suit) for face in faces for suit in suits)
print(type(cards))
print(len(cards))
print(cards)
print(cards[4:8])
