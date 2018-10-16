number = int(input("Give me a number with up to 7 digits"))
number = str(number)

def check_if (number):
    if len(number) == 1:
        var1 = number[0]* 1 == 1
        if var1 == number:
            return True
        else:
            return False
    elif len(number) == 2:
        var2 = number[0] * 1 + number[1]* 2
        if var2 == number:
            return True
        else:
            return False
    elif len(number) == 3:
        var3 = number[0] * 1 + number[1]* 2 + number[2]*3
        if var3 == number:
            return True
        else:
            return False
    elif len(number) == 4:
        var5 = number[0] * 1 + number[1] * 2 + number[2]*3 + number[3]*4
        if var5 == number:
            return True
        else:
            return False
    elif len(number) == 5:
        var4 = number[0] * 1 + number[1] * 2 + number[2]*3 + number[3]*4 + number[4]*5
        if var4 == number:
            return True
        else:
            return False
    elif len(number) == 6:
        var6 = number[0] * 1 + number[1] * 2 + number[2]*3 + number[3]*4 + number[4]*5 + number[5]*6
        if var6 == number:
            return True
        else:
            return False
    elif len(number) == 7:
        var7 = number[0] * 1 + number[1] * 2 + number[2]*3 + number[3]*4 + number[4]*5 + number[5]*6 + number[6]*7
        if var7 == number:
            return True
        else:
            return False

print(check_if(number))