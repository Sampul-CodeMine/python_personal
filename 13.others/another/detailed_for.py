# Prints the elements contained in the list / array
languages = ['Java', 'Python', 'Visual Basic', 'C Sharp', 'PHP', 'Node.js', 'C++', 'Javascript']
for item in languages:
    print(item)


# Sum of numbers from 0 to 100
num_range = range(0, 101)
additions = 0
for i in num_range:
    additions += i
print("Sum of numbers from 0 to 100 = ", additions)


# Multiplication table from 1 to 20
multiplication_table = range(1, 21)
multiplier_val = range(1, 13)

for i in multiplication_table:
    for j in multiplier_val:
        print(i, " * ", j, " = ", (i * j))
