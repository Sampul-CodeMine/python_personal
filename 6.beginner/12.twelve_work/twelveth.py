# Creating a function that will carry out simple calculations
def summation(arg1, arg2):
    print('The sum of {} and {} = {}.'.format(arg1, arg2, (arg1 + arg2)))


def differences(arg1, arg2):
    print('The difference between {} and {} = {}.'.format(arg1, arg2, (arg1 - arg2)))


def products(arg1, arg2):
    print('The product of {} and {} = {}.'.format(arg1, arg2, (arg1 * arg2)))


def division(arg1, arg2):
    print('{} divided by {} = {}.'.format(arg1, arg2, (arg1 / arg2)))


# The is a simple calculation program
print()
print('==SIMPLE ARITHMETIC CALCULATIONS==')
print()
prompt = 'y'
while prompt == 'y' or prompt == 'Y':
    firstVal = ''
    secondVal = ''
    print('Press A - Addition')
    print('Press S - Subtraction')
    print('Press M - Multiplication')
    print('Press D - Division')
    ops = input('What do you want to do? >>  ')
    if ops == 'a' or ops == 'A':
        firstVal = float(input('first value: '))
        secondVal = float(input('second value: '))
        summation(firstVal, secondVal)
    elif ops == 's' or ops == 'S':
        firstVal = float(input('first value: '))
        secondVal = float(input('second value: '))
        differences(firstVal, secondVal)
    elif ops == 'm' or ops == 'M':
        firstVal = float(input('first value: '))
        secondVal = float(input('second value: '))
        products(firstVal, secondVal)
    elif ops == 'd' or ops == 'D':
        firstVal = float(input('first value: '))
        secondVal = float(input('second value: '))
        division(firstVal, secondVal)
    else:
        print('No valid option was selected.')

    print()
    prompt = input('Do you wish to try another? >> ')
print()
print('Thank you for your time')
print()
