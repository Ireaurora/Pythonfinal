import string
alphabet = list(string.ascii_lowercase)

initial_message = str(input("What would you like to shift?"))

message = list(initial_message)

array = []

letterarray = []


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

print(final(y))
