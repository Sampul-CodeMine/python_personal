from math import *
# this will import the math class from the standard library in python which will
# give you access to different math functions

# Variables are names given to a memory location or space on your computer memory unit to hold some data.
# The data held by a variable are of different data types vix:
# numeric datatype(integer (negative or positive), real or float (negative or positive numbers with decimal numbers))
# string datatype(these are data with alpha-numeric characters with special characters inclusive.)
# boolean datatype(true or false values)

# ===========INTEGER  VARIABLES=====================
print(3 * 4)  # multiplication operation
print(3 * (4 + 5))  # structures your arithmetic on which will be executed first (B.O.D.M.A.S.)
print(10 % 3)  # displays the remainder from a division operation
print(3 + 10)  # Addition operation
print(10 - 232)  # Subtraction operation

# Rasie a number to the power of another number
print('4 raised to the power of 2 is = ' + str(pow(4, 2)))

# Displays the maximum or biggest number from a list of numbers
print('Shows the maximum number out of a list of numbers 4, 2, 5, 7,-10 = ' + str(max(4, 2, 5, 7, -10)))

# Displays the smallest number from a list of numbers
print('Shows the minimum number out of a list of numbers 4, 2, 5, 7,-10 = ' + str(min(4, 2, 5, 7, -10)))

# Rounds a number to the nearest whole number.
print('Rounds a number up to the nearest whole number 3.5642 to the nearest whole number is ' + str(round(3.5642)))

# You can import a file or class from anywhere or a standard python library into your file using the 'import' keyword

print("\n===================================================================================\n")

print('Floors the value 3.53 to the nearest integer whole number: ' + str(floor(3.53)))
print('Ceil the value 3.53 to the nearest integer whole number: ' + str(ceil(3.53)))
print('Floors the value -3.53 to the nearest integer whole number: ' + str(floor(-3.53)))
print('Ceil the value -3.53 to the nearest integer whole number: ' + str(ceil(-3.53)))
print('Displays the absolute value of an integer (-32): ' + str(abs(-32)))
print('Displays the absolute value of an integer (32): ' + str(abs(32)))
print('Returns the square root of a number (36): ' + str(sqrt(36)))
