# Define a merge function
* test the following code, the merge two dictionary will keep the key in y dict. try to define your own function which keeps the key in x instead of y.

```py
x = {"a": 1, "b": 2}
y = {"b": 3, "c": 4}
z = {**x, **y} # no duplicated key in dict
print(z)
```

```py
def mergeDict(x, y):
    pass
```

Expected result:
z = {'b': 2, 'c': 4, 'a': 1}