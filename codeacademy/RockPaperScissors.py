import random

#Possible movements:
moves = ["r", "p", "s"]

#When Human wins:
player_wins = ["rs", "pr", "sp"]

def gaming(play, computer):

    if play == computer:
        return "Tie"
    elif (play + computer) in player_wins:
        return "You win"
    else:
        return "You lose!"

player_move = input("Choose:\nr for rock \np for paper \ns for scissors \n")
computer_move = random.choice(moves)

print(gaming(player_move, computer_move))

print("\nYou: %s" % player_move)
print("Computer: %s" % computer_move)