listing = list(input("What list would you like to check?"))
x = int(input("What number are you loooking for?"))


def LinearSearch(listing, x):
    i = 1
    while listing[i] != x:
        i = i + 1
    return i


print(LinearSearch(listing, x))
