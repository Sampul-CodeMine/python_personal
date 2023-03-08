print("\n================= GUESSING GAME ==================\n")

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_max = 5
out_of_guesses = False
guess_remain = 0
guess_val = ""

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_max:
        guess_remain = int(guess_max - guess_count)
        if guess_remain == 1:
            report = str(guess_remain) + " trial left"
        else:
            report = str(guess_remain) + " trials left"
        guess = input("Enter guess - (" + report + ") : ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You have used your 5 trials and you are out of guesses. You LOSE!")     
else:
    if guess_remain == 5:
        guess_val = "1st"
    elif guess_remain == 4:
        guess_val = "2nd"
    elif guess_remain == 3:
        guess_val = "3rd"
    elif guess_remain == 2:
        guess_val = "4th"
    elif guess_remain == 1:
        guess_val = "5th"

    print("\nYou Won at the " + guess_val + " guess!")
