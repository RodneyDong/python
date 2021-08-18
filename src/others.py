"""
Multiple times operator: **
a = 2 * 3
"""

# use ** as arithmatice operator
a = 3
b = 2
c = a**b
print(c)

# merge two dictionary
x = {'key1':'value1', 'key2':'value2'}
y = {'key2':2, 'key3':3}
z = {**y, **x} # dict has no duplicated key
print(z)

# get dict value
date_info = {'year': "2020", 'month': "01", 'day': "01"}
track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
extension = {'ext':'csv'}
filename = "{year}-{month}-{day}-{artist}-{title}.{ext}".format(**date_info, **track_info, **extension)
print(filename)

