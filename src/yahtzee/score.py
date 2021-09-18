def upperSection(data):
    return sum(data)

def lowerSection(data):
    if yahtzee(data):
        return 50
    if largeStraight(data):
        return 40
    if smallStraight(data):
        return 30
    if fullHouse(data):
        return 25
    return upperSection(data)

def kind(data): # return the number of same kind values
    max = 0
    for i in range(len(data)):
        c = data.count(data[i])
        if c > max: max = c
    return max

def fullHouse(data):
    return kind(data) == 3 and len(set(data)) == 2

def smallStraight(data):
    s = set(data)
    list1=[{1,2,3,4},{2,3,4,5},{3,4,5,6},{1,3,4,5,6},{1,2,3,4,6}]
    return s in list1

def largeStraight(data):
    s1,s2 = {1,2,3,4,5},{2,3,4,5,6}
    return set(data) in [s1,s2]

def yahtzee(data):
    return len(set(data))==1


