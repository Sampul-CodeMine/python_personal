x = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in x[::2]:
    print(i, end = ', ')

print("\n\n=========================ANOTHER METHOD====================\n")

count = 0
while count < len(x):
    if count % 2 == 0:
        print(x[count], end =', ')
    else:
        pass
    count += 1

print("\n\n=========================ANOTHER METHOD====================\n")

odds = x[::2]
evens = x[1::2]
print("ODD Placements: {}".format(odds))
print("EVEN Placements: {}".format(evens))

print("\n=========================ANOTHER METHOD====================\n")

odd = []
even = []
for i in range(len(x)):
    if (i+1) % 2 == 1:
        odd.append(x[i])
    else:
        even.append(x[i])
print("ODD Placements: {}".format(odd))
print("EVEN Placements: {}".format(even))
