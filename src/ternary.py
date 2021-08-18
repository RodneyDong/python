"""
Ternary operator: if-else, and-or

if-else: a if a<b else b
1. first value
2. condition: if condition is True, return first value, 
3 another value, if condition is False, return another value.

and-or: a<b and a or b
1. condition
2. return first value if condition is True
3. return another value if condition is False
"""

a, b = 10, 20

# if-else ternary
min1 = a if a<b else b # always return the smaller number between a and b.
print(min1)

max1 = a if a>b else b # always return greater number
print(max1)

# and-or ternary
min1 = a<b and a or b # if condition True, return a, otherwise return b
print(min1)

max1 = a>b and a or b
print(max1)

# use tuple and condition to choose value
max1 = (a, b)[a<b] # return b if True, otherwise return a
print(max1)
min1 = (a, b)[a>b] # return b if True, otherwise return a
print(min1)

min1 = min(a, b)
print(min1)
max1 = max(a, b)
print(max1)

t = (3, 1, 5,7,23,11)
min1 = min(t)
print(min1)
max1 = max(t)
print(max1)
