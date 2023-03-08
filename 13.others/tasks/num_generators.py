prompt = "For how many numbers do you want to generate fibonacci: "
resp = int(input(prompt))

first = 0  # first term
second = 1  # second term
count = 0

print("Fibonacci Numbers up to {}:".format(resp))
while count < resp:
    print(first, end=', ')
    next_val = first + second
    first = second
    second = next_val
    count += 1
print()