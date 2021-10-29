import random



comp_wins = 0
user_wins = 0
ties = 0



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
        print("your score is " + str(user_wins))


print("your score is " + str(user_wins))

