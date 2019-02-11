listing = list(input("What list would you like to check?"))
x = int(input("What number are you loooking for?"))


def BinarySearch(listing, x):
    l = 1
    r = len(listing)
    m = (r+l)/2
    while listing[m] != x:
        if x < listing[m]:
            r = m
        else:
            l = m
        m = (r + l)/2
    return m

print(BinarySearch(listing, x))
