def f(a, b, /, c, d, *, e, f):
    """
    a,b are positional-only, c,d can be positional or keyword
    e and f are required to be keyword.
    / separate the position-only arguments from others
    * separate the keyword-only arguments from others

    dir(__builtins__)
    help(list)
    help(sorted)

    1. no call no action
    2. can be called as many times as you like
    3. return value if has return, or None otherwise
    4. define function in function
    5. return function
    """
    print(a, b, c, d, e, f)


if(__name__ == "__main__"):
    f(2, 4, "c", "d", e=5, f=8) # c,d as positional args
    f(4, 2, c="c", d="d", e=9, f=10) # c,d now is keywords args
    f(4, 2, e=9, f=10, c="c", d="d") # if c,d is keywords, can switch
    f(5, 6, 4, e=7, d="d", f=10) # 4 will be consider as c
#    f(1, 2, 3, 4, 5, f=6) # e cannot be keyword argument
#__add__(self, value, /) # means, no keyword arguments allowed.