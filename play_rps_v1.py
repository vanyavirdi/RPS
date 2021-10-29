def play():
    if user_choice == "rock":
        if comp_choice == "rock":
            print("You chose rock. The computer chose rock. You tied.")

        elif comp_choice == "paper":
            print("You chose rock. The computer chose paper. You lose.")

        elif comp_choice == "scissors":
            print("You chose rock. The computer chose scissors. You win.")

    elif user_choice == "paper":
        if comp_choice == "rock":
            print("You chose paper. The computer chose rock. You win.")

        elif comp_choice == "paper":
            print("You chose paper. The computer chose paper. You tied.")


        elif comp_choice == "scissors":
            print("You chose paper. The computer chose scissors. You lose.")


    elif user_choice == "scissors":
        if comp_choice == "rock":
            print("You chose scissors. The computer chose rock. You lose.")

        elif comp_choice == "paper":
            print("You chose scissors. The computer chose paper. You win.")

        elif comp_choice == "scissors":
            print("You chose scissors. The computer chose scissors. You tied.")
