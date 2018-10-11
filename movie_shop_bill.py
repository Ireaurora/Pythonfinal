dvd = 2.5
br = 3.5
new_game = 4
old_game = 2.5

def quantitydvd():
    ask = int(input("How many are you buying"))
    price = ask*dvd
    return price
def quantityblueray():
    ask = int(input("How many are you buying"))
    price = ask * dvd
    return price

def quantitynewgame():
    ask = int(input("How many are you buying"))
    price = ask * dvd
    return price
def quantityoldgame():
    ask = int(input("How many are you buying"))
    price = ask * dvd
    return price
def menu():
    ans=True
    while ans:
        print ("""
        1.Buy a DVD
        2.Buy a Blue Ray
        3.Buy a new game
        4.Buy an old game
        """)
        ans=input("What would you like to do? ")
        if ans=="1":
            return quantitydvd()
        elif ans=="2":
            return quantityblueray()
        elif ans=="3":
            return quantitynewgame()
        elif ans=="4":
            return quantityoldgame()
        elif ans !="":
          print("\n This is not a valid choice \n Please try again")

print(menu())