# In this exercises we will be asking questions.
# that is a prompt to accept responses and input from users
print()
print()
print("How old are you? ",)
age = input()
print('How tall are you? (in inches) ',)
height = input()
print('What is your weight? (in kg) ',)
weight = input()
print()
print()
newWeight = float(weight) * 2.20462
newHeight = float(height) / 12
print("So you are {}years old, {}inches ({} feet) tall, and {}kg ({} pounds) heavy.".format(age, height, newHeight, weight, newWeight))
print()
print()

# Another way to do this
print('= = A N O T H E R   E X A M P L E = =')
print()
print()
age = input("How old are you? ")
height = input('How tall are you? (in inches) ')
weight = input('What is your weight? (in kg) ')
print()
print()
newWeight = float(weight) * 2.20462
newHeight = float(height) / 12
print("So you are {}years old, {}inches ({} feet) tall, and {}kg ({} pounds) heavy.".format(age, height, newHeight, weight, newWeight))
print()
print()
