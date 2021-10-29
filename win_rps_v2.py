import random

def play ():


def win(player, computer):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False


computer = random.choice (['r', 'p', 's'])


if user == computer:
    print("You and computer have both chosen {}. It's a tie :|".format(computer))

if win(user, computer):
    print("You have chosen {} and the computer has chosen {}. You won!!".format(user, computer))

