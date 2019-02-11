#it has a complexity of O(n) because the number of search operations grows
#at the same rate as the list

#the list doesn't have to be ordered
listing = list(input("What list would you like to check?"))
x = int(input("What number are you loooking for?"))


def LinearSearch(listing, x):
    i = 1
    while listing[i] != x:
        i = i + 1
    return i


print(LinearSearch(listing, x))
