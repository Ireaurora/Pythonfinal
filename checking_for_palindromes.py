import string

alphabet = list(string.ascii_lowercase)

initial_message = str(input("What word would you like to check?"))
initial_message = initial_message.lower()


def reversing_word(initial_message):
    reversed_string = initial_message[::-1]
    if reversed_string == initial_message:
        return ["This is a palidrome"]
    else:
        return list(initial_message) + [": is not a palidrome, because "] + list(reversed_string)


def more_complex_wordspace(initial_message):
    if initial_message.index(" ") != -1:
        initial_message = [s.replace(" ", "") for s in initial_message]
        return final(initial_message)
    else:
        return "Not sure how to proceed"

def more_complex_wordexclamative(initial_message):
    if initial_message.index(" ") != -1:
        initial_message = [s.replace(" ", "") for s in initial_message]
        return final(initial_message)
    else:
        return "Not sure how to proceed"

def more_complex_wordcomma(initial_message):
    if initial_message.index(" ") != -1:
        initial_message = [s.replace(" ", "") for s in initial_message]
        return final(initial_message)
    else:
        return "Not sure how to proceed"


def final(initial_message):
    if initial_message.find(" ") == -1 and initial_message.find("!") == -1 and initial_message.find(",") == -1:
       return reversing_word(initial_message)
    while initial_message.index("") != 1:
        return more_complex_wordspace(initial_message)
    while initial_message.index("!") != 1:
        return more_complex_wordexclamative(initial_message)
    while initial_message.index(",") != 1:
        return more_complex_wordcomma(initial_message)




print(final(initial_message))