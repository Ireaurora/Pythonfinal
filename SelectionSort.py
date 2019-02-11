#declare the string you want to order
listing = list(input("What list would you like to order?"))

def SelectionSort(listing):
    for pointer_a in range(len(listing)):
        min = pointer_a;
        for pointer_b in range(pointer_a + 1, len(listing)):
                if listing[pointer_b] < listing[min]:
                    min = pointer_b
        c = listing[pointer_a]
        listing[pointer_a] = listing[min]
        listing[min] = c
    return listing

print(SelectionSort(listing))
