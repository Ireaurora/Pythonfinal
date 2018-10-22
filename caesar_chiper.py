import string
alphabet = list(string.ascii_lowercase) + [' '] + [' ']
print(alphabet)
initial_message = str(input("What would you like to encrypt?"))
second_message = str(input("What would you like to decrypt?"))

message = list(initial_message)
message2 = list(second_message)
array = []
letterarray = []

def deciding():
    if initial_message == '':
        return final(y)
    else:
        return final1(z)

def shifting():
    for letter in message:
        indexing = alphabet.index(letter) + 1
        array.append(int(indexing))
    return array

y = shifting()

def final(y):
    for number in y:
         letterarray.append(str(alphabet[number]))
    return ''.join(letterarray)



def shifting1():
    for letter in message2:
        indexing = alphabet.index(letter) - 1
        array.append(int(indexing))
    return array

z = shifting1()

def final1(z):
    for number in z:
        letterarray.append(str(alphabet[number]))
    return ''.join(letterarray)

print(deciding())