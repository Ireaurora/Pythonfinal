import random #imports the random module
guesses_used = 0 # number of guesses already used
Name = input("Enter your name")

number = random.randint(1, 30)

print("Greetings," + Name + ", I'm thinking of a number between 1 and 30")

while guesses_used < 5:
    print("You have 5 guesses available")
    guess = int(input("Guess a number now"))
    guesses_used = guesses_used + 1 #for each guess used the count goes up one
    
