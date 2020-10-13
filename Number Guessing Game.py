# Jenny Ogden
# Purpose: Create a Number Guessing Game

# Import the 'random' module in order to generate a random number for the game.
from random import randint

# Generate a number between 1 and 100 (inclusive).
RandomNumber = randint(1,100)
print(RandomNumber)

# Create a variable, count, that keeps track of the number of valid guesses.
Count = 0
print()
print(f"Welcome to the Number Guessing Game!\n")
print(f"Instructions:")
print(f"\t* Guess an integer between 1 and 100.")
print(f"\t* Guess again if your guess is too high or too low.")
print(f"\t* You may quit at anytime by typing 'quit'.")
print(f"\t* Good Luck!")
print()

# Include an option to quit instead of taking another guess.
try:
    if input("Press [ENTER] to continue.") == "quit":
        print(f"Thank you for playing!")
    else:
        while True:
            print()
            Name = input(f"First, please tell me what your name is:")
            print(f"\nWelcome {Name}!")
            Guess = input(f"Please guess an integer between 1 and 100:")
            GuessInt = int(Guess)
            Count += 1
            if GuessInt > 100 or GuessInt < 1:
                print(f"ERROR: You may only choose an integer between 1 and 100.")
                print()
            elif RandomNumber < GuessInt <= 100:
                print(f"Your guess of {GuessInt} is too high. Try again!")
                print()
            elif 0 < GuessInt < RandomNumber:
                print(f"Your guess of {GuessInt} is too low. Try again!")
                print()
            elif GuessInt == RandomNumber:
                if Count == 1:
                    print(f"Congratulations!! You correctly guessed the number {RandomNumber} in {Count} try!")
                    break
                else:
                    print(f"Congratulations!! You correctly guessed the number {RandomNumber} in {Count} tries!")
                    break
            continue
except EOFError as e:
    print(f"Looks like you wanted to get out of the game early! Bye!")

except Exception as e:
    print(f"An error has occured and your game is ending.\nThank you for playing!")