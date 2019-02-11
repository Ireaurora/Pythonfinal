#This algorithm goes and divides the list in half continously checking which one
#the number we're looking for
#it has a complexity of O(log(n)) because the number of search operations grows
#more slowly than the list

#the list has to be ordered otherwise it'll take O(n) time because it'll have
#to check both sides 

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
