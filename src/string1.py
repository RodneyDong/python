s = 'meet me at python class.' # single or double quote are the same
print(type(s))
print(s)

# string is iterable
for item in s:
    print(item, end=' ')

# string slicing
print(s[0:6])
print(s[4:9])
print(s[1:100])
print(s[1:100:2]) # s[[start]:[stop]:[step]]
print(s[::])
print(s[-1]) # get last character in the string s
print(s[::-1])

# string functions
s = "123"
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())

s='92F'
print(s.endswith('F'))
print(s[:2])
x = int(s[:2])
print(x+29)

s="print.md"
index = s.index('.')
print(s[index:])

# string math operators
s1 = "John"
s2 = "Wang"
fullName = s1 + ' ' + s2

n="2"
s = n*5
print(type(s))
print(n*5)

s = "2476"
n = len(s)
s = 9674839
n = len(str(s))
print(f"the number {s} has {n} digits.")