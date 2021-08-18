"""
Dictionary is Python's implementation of a data structure 
that is more generally known as an associative array. 

A dictionary consists of a collection of key-value pairs. 
It is unordered, iterable, mutable, and each pair seperated by commas, 
surrounded by {}, and no duplicate key. The key-value pairs seperated by colon.

{'key1':1, 'key2':2}
"""
days = {
    '1': "Monday",
    '2': "Tuesday",
    '3': "Wendseday",
    '4': "Thursday",
    '5': "Friday",
    '6': "Saturday",
    '7': "Sunday",
}
print(days)

# Create a dictionary
d = {}
print(type(d))
print(len(d))

d1 = {
    '1': "Monday",
    '2': "Tuesday",
    '3': "Wendsday",
    '4': "Thursday",
    '5': "Friday",
    '6': "Saturday",
    '7': "Sunday",
}
print(days)

post = dict(message = "SS contopaxi", language = "English")
print(post)

t = ((1,2), (3,4), (5,6)) # use tuple to create dict, how about list?
d = dict(t)
print(d)

# getvalue from key in a dict
x = days['3']
print(x)

x = days.get('3')
print(x)

x = days.get('9', 'No such Day!')
print(x)

if '9' in days:  # before you get value from dict, you need to check the existence of the key.
    days['9']
    print(x)
else: 
    days['9'] = 'no such day!'

print(days)


# dict CRUD (Create, Receive, Update, Delete)
print('done.')
