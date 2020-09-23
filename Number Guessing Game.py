# Jenny Ogden
# Purpose: Create a Number Guessing Game

# Import the 'random' module in order to generate a random number for the game.
import random

# Generate a number between 1 and 100 (inclusive).
x = random.randint(1,100)

# Create a variable, count, that keeps track of the number of valid guesses.
count = 0
print(f"Welcome to the Number Guessing Game! You may quit at anytime during the game by typing 'quit' into the prompt.")
input("press [ENTER] to begin")
print()

# Include an option to quit instead of taking another guess.
while True:
    guess = input("Guess an integer between 1 and 100: ")
    if guess == "quit":
        print(f"Thank you for playing!")
        break

# Use try and except to differentiate between integer and string values of "guess."
# Create a loop that continues until the user has the correct guess.
    try:
        guess_int = int(guess)
        count += 1

        if guess_int > 100 or guess_int < 1:
            print(f"ERROR: You may only choose an integer between 1 and 100.")
            print()
        elif x < guess_int <= 100:
            print(f"Your guess of {guess_int} is too high. Try again!")
            print()
        elif 0 < guess_int < x:
            print(f"Your guess of {guess_int} is too low. Try again!")
            print()
        elif guess_int == x:
            if count == 1:
                print(f"Congratulations!! You correctly guessed the number {x} in {count} try!")
                break
            else:
                print(f"Congratulations!! You correctly guessed the number {x} in {count} tries!")
                break
    except:
        print(f"ERROR: Invalid input. Please choose an integer between 1 and 100!")
        print()
        continue