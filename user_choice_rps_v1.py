def choice(question):
    valid = False
    while not valid:
        response = input(question)

        if response == "rock":
            return response

        elif response == "paper":
            return response

        elif response == "scissors":
            return response

        else:
            print("Please choose rock, paper or scissors")




response = choice("What's your choice? Rock, Paper or Scissors? \n")

print("You chose {}".format(response))

