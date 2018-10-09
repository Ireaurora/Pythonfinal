from random import randint

question = str(input("Should I roll the dice?"))

def sum():
    return randint(0, 6) + randint(0, 6)

def roll_the_dice():
    return sum()

def start_question():
    while question == "yes":
        return roll_the_dice()
    else:
        return "Okay"


print(start_question())
