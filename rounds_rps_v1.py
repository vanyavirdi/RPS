
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

