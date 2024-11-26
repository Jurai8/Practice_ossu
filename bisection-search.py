# get user input

def main():

    # the number the computer must find
    my_number = 67

    print("Please think of a number between 1 - 100\n")
    # define the range (high and low)
    low = 0
    high = 100

    # define the first guess
    # make sure it's an int
    guess = round((high + low)/2)

    # while guess != my_number:
        # print("Is your secret number", guess + "?")

        # answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

        # if answer == 'h': ## if the guess is too high
            ## decrease the high to the value of guess
            # high = guess
            # guess = round((high + low)/ 2)

        # elif answer == 'l' ## if the guess was too low
            ## increase the low to the value of guess
            # low = guess
            # guess = round((high + low) / 2)

        # elif answer  == 'c' ## if the answer is correct
            # print("Game over. Your secret number was: " + guess)
            # return




main()
