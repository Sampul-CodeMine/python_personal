print ("\n========= S I M P L E   T R A N S L A T O R ================\n")


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter == "a":
            translation = translation + "@"
        elif letter == "e" or letter == "E":
            translation = translation + "3"
        elif letter == "i":
            translation = translation + "!"
        elif letter == "o" or letter == "O":
            translation = translation + "0"
        elif letter == "u" or letter == "U":
            translation = translation + "^"
        elif letter == "A":
            translation = translation + "4"
        elif letter == "I":
            translation = translation + "|"
        else:
            translation = translation + letter

    return translation


print(translate(input("Enter a Phrase: ")))