def f(**keywordargs):
    print(type(keywordargs))
    print(keywordargs)
    # for key in keywordargs:
    #     print(f"Key={key} and Value={keywordargs.get(key)}")
    for key, value in keywordargs.items():
        print(key,value)

f(a="1", b='2', c=3)

x = {1:11, 2:22, 3:33, 4:44, 5:55}
f(a=x)