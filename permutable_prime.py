import itertools

num = int(input("What number would you like to test?"))
change_to_string = str(num)
change_to_list = []

def converting_num_to_list(num):
    for digit in change_to_string:
            change_to_list.append(int(digit))
            x = set(itertools.permutations(change_to_list))
    return x

y = converting_num_to_list(num)


def printing_single_list_elements(y):
    for lists in y:
        r = int("".join(map(str, lists)))
        for i in range(2, r):
            if (r % i) == 0:
                print(r, "is not a prime number")
                break
        else:
            print(r, "is a prime number")

printing_single_list_elements(y)


