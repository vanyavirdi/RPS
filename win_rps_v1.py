

def win(player, computer):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False

if win(user, computer):
    print("You have chosen {} and the computer has chosen {}. You won!!".format(user, computer))
