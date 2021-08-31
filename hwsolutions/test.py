y = ['x','yo,']
x = [',','.']
y[0] = 'y'
print(y)
'''
for x in words: # Deletes commas or periods
    for y in words:
        b = y.replace(y[len(y)-1],'')
        if x == b:
            z = words.index(y)
            x = words[z].replace(words[z][len(y)-1],"")
            words[z] = x
'''