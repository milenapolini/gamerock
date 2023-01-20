# Rock Paper Scissors

# Rules: r > s, s > p, p > r

import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'Tie'

    if is_win(user, computer):
        return 'You Won!'
    
    return 'You Lost! Game Over'

def is_win(player, opponent):
    # Return "True" if the Player Wins
    # Rule: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())