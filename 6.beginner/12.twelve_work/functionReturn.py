# Creating a function that will carry out simple calculations
def summation(arg1, arg2):
    return arg1 + arg2


def differences(arg1, arg2):
    return arg1 - arg2


def products(arg1, arg2):
    return arg1 * arg2


def division(arg1, arg2):
    return arg1 / arg2


# The is a simple calculation program
print()
print('==SIMPLE ARITHMETIC CALCULATIONS==')
print()
prompt = 'y'
while prompt == 'y' or prompt == 'Y':
    firstVal = ''
    secondVal = ''
    add = 0
    minus = 0
    times = 0
    share_divider = 0
    print('Press A - Addition')
    print('Press S - Subtraction')
    print('Press M - Multiplication')
    print('Press D - Division')
    ops = input('What do you want to do? >>  ')
    if ops == 'a' or ops == 'A':
        firstVal = float(input('first value: '))
        secondVal = float(input('second value: '))
        add = summation(firstVal, secondVal)
        print('The sum of {} + {} = {}'.format(firstVal, secondVal, add))
    elif ops == 's' or ops == 'S':
        firstVal = float(input('first value: '))
        secondVal = float(input('second value: '))
        minus = differences(firstVal, secondVal)
        print('The difference between {} - {} = {}'.format(firstVal, secondVal, minus))
    elif ops == 'm' or ops == 'M':
        firstVal = float(input('first value: '))
        secondVal = float(input('second value: '))
        times = products(firstVal, secondVal)
        print('The product of {} * {} = {}'.format(firstVal, secondVal, times))
    elif ops == 'd' or ops == 'D':
        firstVal = float(input('first value: '))
        secondVal = float(input('second value: '))
        share_divider = division(firstVal, secondVal)
        print('{} / {} = {}'.format(firstVal, secondVal, share_divider))
    else:
        print('No valid option was selected.')

    print()
    prompt = input('Do you wish to try another? >> ')
print()
print('Thank you for your time')
print()
