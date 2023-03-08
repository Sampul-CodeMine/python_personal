class Error(Exception):
    pass

class ValueTooLargeError(Error):
    pass

class ValueTooSmallError(Error):
    pass

class ValueError(Error):
    pass

# import the inbuilt random number generator
import random

low = random.randint(1, 10)
high = random.randint(10, 100)
to_guess = random.randint(low, high)

is_found = False
counter = 0

while counter <= 9:
    try:
        num_val = input("Guess Number ({} - {}) : ".format(low, high))
        counter += 1
        if num_val.isnumeric():
            num_val = int(num_val)
            if num_val > to_guess:
                is_found = False
                raise ValueTooLargeError
            elif num_val < to_guess:
                is_found = False
                raise ValueTooSmallError
            else:
                is_found = True
                print("Nice work. You found the number {} after {} guesses.".format(to_guess, counter))
                exit(0)
        else:
            is_found = False
            raise ValueError
        
        break
    except ValueTooLargeError:
        print("Count: {}\t{} is bigger than the number to guess.".format(counter, num_val))
    except ValueTooSmallError:
        print("Count: {}\t{} is smaller than the number to guess.".format(counter, num_val))
    except ValueError:
        print("Count: {}\tNumber Required.".format(counter))

print("You could not guess the number {} correctly after {} guess(es).".format(to_guess, counter))
exit(0)
