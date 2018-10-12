total_hours_worked = int(input("How many hours have you worked this week?"))
normal_hour_rate = float(input("How much do yoy get paid per hour normally?"))
extra_hour_rate = float(input("How much do you get paid per hour overtime"))


def understanding():
    if total_hours_worked > 40 and total_hours_worked < 7*24:
        return extra_time()
    elif total_hours_worked > 7*24:
        return "That's not a valid input"
    else:
        return week_earning()
def extra_time():
        normal_hours = 40 * normal_hour_rate
        extra_hours = total_hours_worked - 40
        return extra_hours * extra_hour_rate + normal_hours

def week_earning():
        normal_earning = total_hours_worked * normal_hour_rate
        return normal_earning



print(understanding())
