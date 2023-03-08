print("\n===== F O R   L O O P S   =============\n")
letters = "GIRAFFE ACADEMY"
print("this will print out each alphabet as a separate entity.\n")
for letter in letters:
    print(letter) 

print(" Another Example \n")
friends = ["Mummy", "Wifey", "Sisters", "Brothers"]
for pal in friends:
    print(pal)

for pals in range(len(friends)):
    print(pals, " - ", friends[pals])

print(" Another Example \n")
numbers = 10
for index in range(numbers):
    print(index )

print(" Another Example \n")
for indic in range(2, numbers):
    print(indic)
