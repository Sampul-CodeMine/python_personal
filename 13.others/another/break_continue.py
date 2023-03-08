# BREAK STATEMENTS IN PYTHON
print("BREAK STATEMENT")
numbers = [1, 5, 3, 6, -1, 7]
for val in numbers:
    if val <= 0:
        break  # breaks out of the loop if a value less than or equal to 0 (zero) is found.
    print(val)

print()

# Print the sum of a number
summation = 0
while True:
    n = input('Enter a number: ')
    n = float(n)  # converts the integer input to float value

    if n < 0:
        break  # if the number entered is less than zero (0) break from the loop
    summation += n  # else add to the sum

print("Sum = ", summation)

# CONTINUE STATEMENTS IN PYTHON
print("CONTINUE STATEMENT")

items = [1, 5, 0, 3, 6, -1, 7, -9, 4]
for val in items:
    if val <= 0:
        continue  # disregards other statements and returns for the next iteration.
    print(val)

print()

# PASS STATEMENTS IN PYTHON
print("PASS STATEMENT")
# The pass statement is used in a function or loop which you will like to use later.
# It is used to construct a body that does nothing but will be implemented later.
sequence = {'p', 'a', 'c', 'e'}
for val in sequence:
    pass

print('Statement after loop')
print(sequence)
