import string
import random

password_size = int(input("How long would you like your password to be?"))

def checking_lenght():
    if password_size < 6:
        print(checked())
    else:
        print(random_password())

def random_password():
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters)for x in range (0, password_size))


def checked():
    password_size = int(input("How long would you like your password to be?"))
    return checking_lenght()

print(checking_lenght())
