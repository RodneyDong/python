def recursive(a):
    score = 0
    for x in range (len(a)):
        score += a[x]
    return score
def input1():
    print("Calculates sum of number from x to y:")
    x = int(input("x:"))
    y = int(input("y:"))
    numbers = []
    for i in range(x,y+1):
        numbers.append(i)
    return numbers
print("The anwser is: ",recursive(input1()))