def user_choice(question):
    valid = False
    while not valid:
        user = input(question).lower()

        if user == "r" or user == "R" or user == "rock":
            user = "rock"
            return user

        elif user == "p" or user == "P" or user == "paper":
            user = "paper"
            return user

        elif user == "s" or user == "S" or user == "scissors" or user == "scissor":
            user = "scissors"
            return user

        else:
            print("Please choose rock, paper or scissors")




user = user_choice("What's your choice? Rock, Paper or Scissors? \n")

print("You chose {}".format(user))


