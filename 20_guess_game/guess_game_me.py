# import the inbuilt random number generator
import random

low = random.randint(0, 10)  # get the lower range of value to guess
high = random.randint(10, 100)  # get the higher range of value to guess
to_guess = random.randint(low, high)  # generate a value to guess between the low and high range respectively 

is_found = False  # boolean flag to keep track of whether guessed number is found or not
counter = 0  # counter to hold the number of guesses made by the user,

while is_found is False:
    while True:
        num_val = input("Guess Number: ( {} - {} ) ".format(low, high))
        counter += 1
        if num_val.isnumeric():
            num_val = int(num_val)
            if num_val > to_guess:
                is_found = False
                print("{} is bigger than the number to guess.".format(num_val))
                continue
            elif num_val < to_guess:
                is_found = False
                print("{} is smaller than the number to guess.".format(num_val))
                continue
            else:
                is_found = True
                break

        else:
            is_found = False
            print("Must be numeric data.")
            continue

        
if is_found is True and counter <= 5:
    print("You are a genius. You found the number to guess '{}' after {} guesses.".format(to_guess, counter))
elif is_found is True and counter <=10:
    print("Nice work. You found the number to guess '{}' after {} guesses.".format(to_guess, counter))
else:
    print("You found the number to guess {} after {} guesses. Your attempt was poor.".format(to_guess, counter))
exit(0)