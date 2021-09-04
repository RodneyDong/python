def is_only_letter_digit (a):
    for x in a:
        y = x.isalpha()
        z = x.isdigit()
        if (y == False) and (z == False):
            return False
    return True
def is_eight_characters (a):
    if len(a) < 8:
        return False
    return True
def has_two_digits (a):
    count = 0
    for x in a:
        z = x.isdigit()
        if z:
            count += 1
    if count >= 2:
        return True
    return False
def passwordCheck():
    while True:
        password = input("Input a password：")
        x = is_only_letter_digit(password)
        y = is_eight_characters(password)
        z = has_two_digits(password)
        if x and y and z:
            print (password,' is a valid password')
            break
        print(password, ' is not a valid password. Please re-enter')

if __name__ == '__main__':
    passwordCheck()