def recursive(a):
    if a == 0: # 终止条件
        return 0
    return a + recursive(a-1) # 调整变量

if __name__ == '__main__': # test code block    
    x = recursive(10)
    print(x)