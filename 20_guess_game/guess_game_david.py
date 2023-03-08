import random

print("Welcome to Number Guessing Game")

trials = 5
counts = 0

number = random.randint(1, 100)

while trials > 0:
    guess = int(input("Guess (Between 1 to 100): "))
    trials -= 1
    counts += 1

    if guess == number:
        print("Congratulations, you got it right.")
    elif guess > number:
        print("Number larger than the guess value.")
    else:
        print("Number smaller than the guess value.")

if trials == 0:
    print("Game over! Try again")
    print("You guessed {0} times".format(counts))
    print("The number to guess is {0}".format(number))