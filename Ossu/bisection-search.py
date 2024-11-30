# get user input

def main():

    # the number the computer must find
    my_number = 91

    print("Please think of a number between 1 - 100\n")
    # define the range (high and low)
    low = 0
    high = 100

    answer = ''

    # define the first guess
    # make sure it's an int
    guess = round((high + low)/2)

    while answer != 'c':
        print("Is your secret number", guess, "?")

        answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. \n")

        # if the guess is too high
        if answer == 'h': 
            # decrease the high to the value of guess
            high = guess
            guess = round((high + low)/ 2)
        # if the guess was too low
        elif answer == 'l': 
            # increase the low to the value of guess
            low = guess
            guess = round((high + low) / 2)
        # if the answer is correct
        elif answer  == 'c': 
            print(f"Game over. Your secret number was: {guess}")
        else:
            print("I can't understand your input")

    return




main()
