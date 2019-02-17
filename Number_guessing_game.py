import random #imports the random module
guesses_used = 0 # number of guesses already used
Name = input("Enter your name")

number = random.randint(1, 30)

print("Greetings, " + Name + ", I'm thinking of a number between 1 and 30")

while guesses_used < 5:
    guesses_left = str(5-guesses_used)
    print("You have "  + guesses_left + " guesses available")
    guess = int(input("Guess a number now"))
    guesses_used = guesses_used + 1 #for each guess used the count goes up one
    if guess < number:
        print("Too low, try again")
    if guess > number:
        print("Too high, try again")
    if guess > 30 or guess < 1:
        print("Out of range! I'm thinking of a number between 1 and 30")
    if guess == number:
        break
if guess == number:
    guesses_used = str(guesses_used)
    print("Well done, " + Name  +"! You guessed correctly in " + guesses_used + "guesses")

if guess != number:
    number = str(number)
    print("Sorry, you're out of guesses! I was thinking about this number: "+ number)
