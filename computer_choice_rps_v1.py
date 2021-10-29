import random

def computer_choice():
    computer = random.randint(1, 3)
    if computer == 1:
        computer = "r"
    elif computer == 2:
        computer = "p"
    else:
        computer = "s"
    return computer




