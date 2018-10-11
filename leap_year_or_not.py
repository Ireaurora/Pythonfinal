year = int(input("What year do you want to check?"))

def checking_years(year):
    if year % 4 == 0:
        return "This is a leap year"
    else:
        return "This is not a leap year"


print(checking_years(year))