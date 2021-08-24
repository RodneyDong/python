def findMom(nameList, targetChildName):
    for childName, momName in nameList:
        if childName==targetChildName:
            return momName

# if without else
def display(childName, momName):
    if momName:
        print(f"{childName}'s mom is {momName}.")
        return
    print(f"{childName}'s mom is not in the name list.")

if __name__ == '__main__':
    nameList = [
        ('james', 'robert'),
        ('john', 'daniel'),
        ('michael', 'william'),
        ('david', 'anthony'),
        ('mark', 'donald'),
        ('andrew', 'kenneth'),
    ]

    child = "michael"
    mom = findMom(nameList, child)
    # if mom:
    #     print(f"{child}'s mom is {mom}.")
    # else:
    #     print(f"{child}'s mom is not in the name list.")
    display(child, mom)