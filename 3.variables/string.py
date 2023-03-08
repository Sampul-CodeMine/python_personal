# Variables are names given to a memory location or space on your computer memory unit to hold some data.
# The data held by a variable are of different data types vix:
# numeric datatype (integer (negative or positive), real or float (negative or positive numbers with decimal numbers))
# string datatype(these are data with alpha-numeric characters with special characters inclusive. )
# boolean datatype(true or false values)

# ===========STRING  VARIABLES=====================
story = '''
There was a man named {},
He was {} years old.
He really likes the name {},
but didn't like being {}.
'''
print(story.format('John', 70, 'Tony', 35))

# ============SIMPLE FUNCTIONS THAT CAN BE USED WITH PYTHON STRING VARIABLES=====================
# Different Escape characters in PYTHON
# \n - New Line
# \\ - Print Backslash
# \" - Print a double quote
# \t - add a tab
phrase = "Giraffe Academy!"
print(phrase)

# Concatenation
print(phrase + " is a good place to learn.")
print(phrase + "\nThis is a good place to learn.")

# Using the uppercase function in PYTHON
new_phrase = "\"" + phrase.upper() + " This is a good place to learn.\""
# some other functions
# len() - gives the length of a string
# str() - Converts a data or variable to a string datatype
# lower() - converts all characters in a string to lowercase
# isupper() - boolean to return true if all characters of a string are uppercase else returns false.
# islower() - boolean to return true if all characters of a string are lowercase else returns false.
# replace() - used to replace a specified subset of string from an entire STRING
# index() - gives us the exact location of a character in a string
# int() - this converts a variable to integer datatype

print('The length of the sentence ' + new_phrase + ' is = ' + str(len(new_phrase)))
print("Are all the characters in the string " + new_phrase + " uppercase? " + str(new_phrase.isupper()))
print("Are all the characters in the string " + new_phrase + " lowercase? " + str(new_phrase.islower()))
checkIndex = int(new_phrase.index('good'))
print(checkIndex)
newString = new_phrase.replace("GIRAFFE", "ELEPHANT")
print(newString)
