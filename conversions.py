def initial():
    initial_unit = str(input("Enter the unit you currently have"))
    final_unit = str(input("Enter the unit you want to get"))
    if initial_unit == "stones" and final_unit == "kg":
        print(from_stones_to_kg(int(str(input("Enter the unit you currently have")))))
    elif initial_unit == "pounds" and final_unit == "kg":
        print(from_pounds_to_kg(int(str(input("Enter the unit you currently have")))))
    elif initial_unit == "kg" and final_unit == "stones":
        print(from_kg_to_stones(int(str(input("Enter the unit you currently have")))))
    elif initial_unit == "kg" and final_unit == "pounds":
        print(from_kg_to_pounds(int(str(input("Enter the unit you currently have")))))
    else:
        False

def from_stones_to_kg(stones):
    if stones != 0:
        newweight = stones * 6.35029
        return newweight
    else:
        return 0


def from_pounds_to_kg(pounds):
    if pounds != 0:
        newweight = pounds * 0.453592
        return newweight
    else:
        return 0


def from_kg_to_stones(kg):
    if kg != 0:
        newweight = kg / 6.35029
        return newweight
    else:
        return 0


def from_kg_to_pounds(kg):
    if kg != 0:
        newweight = kg / 0.453592
        return newweight
    else:
        return 0

initial()



