# Jenny Ogden
# Purpose: Create a Number Guessing Game that keeps track of the number of guesses and
# writes the top scorers to a separate .txt file

# Import two modules: random and sys to assist in code. Also, import Functions from TopPlayers,
# which is a function that writes the top 5 players to a .txt file.
import random
import sys
from Functions import TopPlayers

# Print our instructions for the Number Guessing Game.
print(f"Welcome to the Number Guessing Game!\n")
print(f"Instructions:")
print(f"\t* Guess an integer between 1 and 100.")
print(f"\t* Guess again if your guess is too high or too low.")
print(f"\t* You may quit at anytime by typing 'quit'.")
print(f"\t* Good Luck!")
print()

# Include an option to quit instead of taking another guess.
# Ask for player's name and store it into the variable, Name.
try:
    Enter = input("Press [ENTER] to begin. ")
    if Enter == "quit":
        print(f"Thank you for playing!")
        sys.exit()
    print()

    Name = input("Before we begin, please tell me your name? ")
    if Name == 'quit':
        print(f"Thank you for playing!")
        sys.exit()
    else:
        print()
        print(f"Welcome, {Name}!")
except Exception as e:
    print("ERROR: An error has occured. Thanks for playing!")
    sys.exit()

# Create a method, GuessingGame(), that does the following:
    # Generates a variable, Count, to keep track of the number of guesses.
    # Generates a random number, for which the player guesses.
    # Prints whether the guess is too high, too low, or correct.
def GuessingGame():
    Count = 0
    RandomNumber = random.randint(1, 100)
    #print(RandomNumber)
    while True:
        try:
            Guess = input("Please guess an integer between 1 and 100: ")
            if Guess == "quit":
                print(f"Thank you for playing!")
                break

            # Turn the guess into an integer and begin incrementing Count.
            GuessInt = int(Guess)
            Count += 1

            # If Guess is outside the range (greater than 100 or less than 1), print an error message.
            if GuessInt > 100 or GuessInt < 1:
                print(f"Invalid Input: You may only choose an integer between 1 and 100.")
                print()
                Count = Count - 1

            # Print that the guess is too high.
            if RandomNumber < GuessInt <= 100:
                print(f"Your guess of {GuessInt} is too high. Try again!")
                print()

            # Print that the guess is too low.
            elif 0 < GuessInt < RandomNumber:
                print(f"Your guess of {GuessInt} is too low. Try again!")
                print()

            # If guess is correct on the first try, reward the player and output name to the top scorer file.
            elif GuessInt == RandomNumber:
                if Count == 1:
                    print()
                    print(f"Congratulations!! You correctly guessed the number {RandomNumber} in {Count} try!")
                    print()

                    # Call our function, TopPlayer, that writes top players to a .txt file
                    TopPlayers(Count, Name)
                    print()

                    # Allow the player to loop through the game again.
                    try:
                        if input("Would you like to play again? If so, press 'Y': ") in ("Y", "y"):
                            print()
                            print("Great!")
                            GuessingGame()
                        else:
                            print("Thanks for playing!")
                            break
                    except Exception as e:
                        raise e

                # If guess is correct where Count > 1, reward the player and determine if they make it
                # to the top 5 or not.
                else:
                    print()
                    print(f"Congratulations!! You correctly guessed the number {RandomNumber} in {Count} tries!")
                    print()
                    TopPlayers(Count, Name)
                    print()

                    # Allow the player to loop through the game again.
                    try:
                        if input("Would you like to play again? If so, press 'Y': ") in ("Y", "y"):
                            print()
                            print("Great!")
                            GuessingGame()
                        else:
                            print("Thanks for playing!")
                            sys.exit()
                    except Exception as e:
                        raise e
        # Catch any EOF errors, like CTRL+D.
        except EOFError as e:
            print(f"Looks like you're trying to get out of the game! Thanks for playing!")
            break

        # Catch all other exceptions.
        except Exception as e:
            print(f"ERROR: You must choose an integer between 1 and 100.")
            print()

GuessingGame()