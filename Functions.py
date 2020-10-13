# Purpose: Create a function called TopPlayers that writes the top 5 players to a .txt file.

def TopPlayers(score, name):

    # Create a new .txt file, topPlayers.txt, and write the default 5 players to it.
    TopPlayers = open('topPlayers.txt', 'w')
    TopPlayers.write("3         Don")
    TopPlayers.write("\n7         Susan")
    TopPlayers.write("\n8         Harold")
    TopPlayers.write("\n8         Jane")
    TopPlayers.write("\n10        Harold")

    # Close the file.
    TopPlayers.close()

    # Open the file and read in the lines as a dictionary, using readlines().
    # Also, initialize a new list, MyList.
    FixedWidth = open('topPlayers.txt').readlines()
    MyList = []

    # Create a loop that loops through each line and creates a tuple for each line and appends
    # each tuple to a list, MyList.
    for line in FixedWidth:
        Tuples = [int(line[0:10]), line[10:20].strip()]
        MyList.append(Tuples)

    # Sort our new list by score in ascending order.
    Sorted = sorted(MyList, key = lambda x: int(x[0]))

    # After sorting, write the variables Scores and Names to separate lists.
    for list in Sorted:
        Scores = [int(Sorted[0][0]), int(Sorted[1][0]), int(Sorted[2][0]),
                  int(Sorted[3][0]), int(Sorted[4][0])]
        Names = [Sorted[0][1], Sorted[1][1], Sorted[2][1],
                 Sorted[3][1], Sorted[4][1]]

    # Write a Boolean that will decide whether a value is less than any of the scores in the Scores list.
    def check(Scores, score):
        for item in Scores:
            if score < item:
                return True
        return False

    # If a value is less than any score in the Scores list, append it to the list, sort the list,
    # and pop() the last line. This ensures that only the top 5 players are kept in the list.
    if(check(Scores, score)):
        Scores.append(score)
        Names.append(name)

        # Combine Scores and Names into one list, UpdatedList.
        UpdatedList = [[Scores[0], Names[0]], [Scores[1], Names[1]], [Scores[2], Names[2]],
                       [Scores[3], Names[3]], [Scores[4], Names[4]], [Scores[5], Names[5]]]
        SortedUpdatedList = sorted(UpdatedList, key = lambda x: int(x[0]))
        SortedUpdatedList.pop()
        #print(SortedUpdatedList)

        # Write the new updated list of players to topPlayers.txt.
        f = open('topPlayers.txt', 'w')
        for t in SortedUpdatedList:
            line = '         '.join(str(x) for x in t)
            f.write(line + '\n')
        f.close()

        # Print the five lines from the new file.
        # If the player made the top 5, congratulate them.
        print(f"And you made the top 5! Below is a list of the top 5 players:")
        print(f"\t[1] {SortedUpdatedList[0][1]}, with a score of {SortedUpdatedList[0][0]}")
        print(f"\t[2] {SortedUpdatedList[1][1]}, with a score of {SortedUpdatedList[1][0]}")
        print(f"\t[3] {SortedUpdatedList[2][1]}, with a score of {SortedUpdatedList[2][0]}")
        print(f"\t[4] {SortedUpdatedList[3][1]}, with a score of {SortedUpdatedList[3][0]}")
        print(f"\t[5] {SortedUpdatedList[4][1]}, with a score of {SortedUpdatedList[4][0]}")
    else:

        # If the player did not make the top 5, let them know and print the top 5.
        print(f"Unfortunately, you did not make the top 5, {name}. ")
        print()
        print("Here is a list of the top 5 players:")
        print(f"\t[1] {Sorted[0][1]}, with a score of {Sorted[0][0]}")
        print(f"\t[2] {Sorted[1][1]}, with a score of {Sorted[1][0]}")
        print(f"\t[3] {Sorted[2][1]}, with a score of {Sorted[2][0]}")
        print(f"\t[4] {Sorted[3][1]}, with a score of {Sorted[3][0]}")
        print(f"\t[5] {Sorted[4][1]}, with a score of {Sorted[4][0]}")