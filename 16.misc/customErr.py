# importing the class to allow for random number generator
import random


class Error(Exception):
    pass


class ValueTooSmallError(Error):
    pass


class ValueTooLargeError(Error):
    pass


class NotValueError(Error):
    pass


low_limit = random.randint(1, 10)
max_limit = random.randint(50, 1000)
to_guess = random.randint(low_limit, max_limit)

print("""
Welcome to a Guess Game...
We will be guessing for a number between {} and {}.
Let the guess game begin.
""".format(low_limit, max_limit))

count = 0
is_found = False
while count <= 14:
    try:
        val_display = "Guess Number: ({} to {}) ".format(low_limit, max_limit)
        i_num = input(val_display)
        count += 1
        if i_num.isnumeric():
            i_num = int(i_num)
            if i_num > to_guess:
                is_found = False
                raise ValueTooLargeError
            elif i_num < to_guess:
                is_found = False
                raise ValueTooSmallError
            else:
                is_found = True
                if count == 1:
                    print("Wow! What a genius! You found the number '{}' with the first guess.".format(to_guess))
                    exit(0)
                elif count <= 5:
                    print("You are Excellent! You found the number '{}' after {} guesses.".format(to_guess, count))
                    exit(0)
                elif count <= 10:
                    print("Nice Work! You found the number '{}' after {} guesses.".format(to_guess, count))
                    exit(0)
                else:
                    print("Fair Tries! You found the number '{}' after {} guesses.".format(to_guess, count))
                    exit(0)
        else:
            is_found = False
            raise NotValueError
        break
    except ValueTooLargeError:
        print('Count ({}): \'{}\' is too large.'.format(count, i_num))
    except ValueTooSmallError:
        print('Count ({}): \'{}\' is too small.'.format(count, i_num))
    except NotValueError:
        print('Count ({}): \'{}\' is not a numeric data.'.format(count, i_num))
print("It is so You could not guess the number '{}' correctly after {} guesses.".format(to_guess, count))
exit(0)