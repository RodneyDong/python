def recursive(a):
    if a == 0:
        return 0
    return a + recursive (a-1)
if __name__ == '__main__':
    x = recursive(10)
    print(x)
