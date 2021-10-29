import random

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

how_many= rounds("How many rounds would "
                 "you like to play? ", 0, 10)



comp_wins = 0
user_wins = 0
ties = 0

rounds_played = 0

start = input("Press enter to start... ")
while start == "":
    user_choice = input("choose ").lower()

    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "rock"
    elif comp_choice == 2:
        comp_choice = "paper"
    else:
        comp_choice = "scissors"

    if user_choice == "rock":
        if comp_choice == "rock":
            print("You chose rock. The computer chose rock. You tied.")
            ties += 1

        elif comp_choice == "paper":
            print("You chose rock. The computer chose paper. You lose.")
            comp_wins += 1

        else:
            print("You chose rock. The computer chose scissors. You win.")
            user_wins += 1
        rounds_played += 1
        print("your score is " + str(user_wins))

    elif user_choice == "paper":
        if comp_choice == "rock":
            print("You chose paper. The computer chose rock. You win.")
            user_wins += 1

        elif comp_choice == "paper":
            print("You chose paper. The computer chose paper. You tied.")
            ties += 1

        else:
            print("You chose paper. The computer chose scissors. You lose.")
            comp_wins += 1
        rounds_played += 1
        print("your score is " + str(user_wins))


    elif user_choice == "scissors":
        if comp_choice == "rock":
            print("You chose scissors. The computer chose rock. You lose.")
            comp_wins += 1

        elif comp_choice == "paper":
            print("You chose scissors. The computer chose paper. You win.")
            user_wins += 1

        else:
            print("You chose scissors. The computer chose scissors. You tied.")
            ties += 1

        rounds_played += 1
        print("your score is " + str(user_wins))

    if rounds_played == how_many:
        print("You have now played {} rounds".format(how_many))
