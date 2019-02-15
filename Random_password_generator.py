import string
import random

password_size = int(input("How long would you like your password to be?"))

def random_password():
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters)for x in range (0, password_size))




print(random_password())
