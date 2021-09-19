# def is_only_letter_digit (a):
#     for x in a:
#         y = x.isalpha()
#         z = x.isdigit()
#         if (y == False) and (z == False):
#             return False
#     return True
# def is_eight_characters (a):
#     if len(a) < 8:
#         return False
#     return True
def has_two_digits (a):
    count = 0
    for x in a:
        if x.isdigit():
            count += 1
    return count >= 2
<<<<<<< HEAD
=======

>>>>>>> 0dbc21e700ca75c118efdf059722f8b33a47bf3c
def passwordCheck():
    while True:
        password = input("Input a password：")
        if password.isalnum() and len(password) >= 8 and has_two_digits(password):
            print (password,' is a valid password')
            break
        print(password, ' is not a valid password. Please re-enter')

if __name__ == '__main__':
    passwordCheck()