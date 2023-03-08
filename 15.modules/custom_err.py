# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input is too large"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input is too small"""
    pass


class ValueError(Error):
    """Raised when the input is not an integer or is an alphabet"""
    pass


number = 100  # Number to guess

while True:
    try:
        i_num = input("Enter your guessed value: ")
        if i_num.isnumeric():
            i_num = int(i_num)
            if i_num > number:
                raise ValueTooLargeError
            elif i_num < number:
                raise ValueTooSmallError
            break
        else:
            raise ValueError
        break
    except ValueError:
        print("Invalid data. Numeric Integer value is required. Try again.")
    except ValueTooSmallError:
        print("Value is too small. Try again.")
    except ValueTooLargeError:
        print("Value is too large. Try again.")
print("You guessed it right. Congratulations.")