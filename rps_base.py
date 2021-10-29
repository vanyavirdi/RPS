import random


def user_choice():

    user = input("What's your choice? Rock, Paper or Scissors? \n").lower()

    if user == "r" or user == "R" or user == "rock":
        user = "rock"
    elif user == "p" or user == "P" or user == "paper":
        user = "paper"
    elif user == "s" or user == "S" or user == "scissors" or user == "scissor":
        user = "scissors"
    return user



def computer_choice():
    computer = random.randint(1, 3)
    if computer == 1:
        computer = "rock"
    elif computer == 2:
        computer = "paper"
    else:
        computer = "scissors"
    return computer


def rounds(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:

        try:
            response = int(input(question))

            if low < response <= high:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


#INTRODUCTION TO GAME

name = input("What is your name? ")

print()

print("Hi {}! Welcome to my Rock/Paper/Scissors game."
      "Best of luck, hope you win :)".format(name))

print()


print()

#NUMBER OF ROUNDS BETWEEN 1-10
how_many = rounds("How many rounds would "
                 "you like to play? ", 0, 10)

print()


#INITIAL STATS
rounds_played = 0

comp_wins = 0
user_wins = 0
ties = 0

while True:

    print()
    user_option = user_choice()
    computer = computer_choice()

    rounds_played += 1

    if user_option == "rock":
        if computer == "rock":
            print("You chose rock. The computer chose rock. You tied.")
            ties += 1

        elif computer == "paper":
            print("You chose rock. The computer chose paper. You lose.")
            comp_wins += 1

        else:
            print("You chose rock. The computer chose scissors. You win.")
            user_wins += 1

        print()
        print("{}'s score: {}".format(name, user_wins))
        print("Computer's score: {}".format(comp_wins))
        print("Ties: {}".format(ties))

    elif user_option == "paper":
        if computer == "rock":
            print("You chose paper. The computer chose rock. You win.")
            user_wins += 1

        elif computer == "paper":
            print("You chose paper. The computer chose paper. You tied.")
            ties += 1

        else:
            print("You chose paper. The computer chose scissors. You lose.")
            comp_wins += 1

        print()
        print("{}'s score: {}".format(name, user_wins))
        print("Computer's score: {}".format(comp_wins))
        print("Ties: {}".format(ties))

    else:
        if computer == "rock":
            print("You chose scissors. The computer chose rock. You lose.")
            comp_wins += 1

        elif computer == "paper":
            print("You chose scissors. The computer chose paper. You win.")
            user_wins += 1

        else:
            print("You chose scissors. The computer chose scissors. You tied.")
            ties += 1

        print()
        print("{}'s score: {}".format(name, user_wins))
        print("Computer's score: {}".format(comp_wins))
        print("Ties: {}".format(ties))

    if rounds_played == how_many:
        print("You have now played {} rounds".format(how_many))
        break





