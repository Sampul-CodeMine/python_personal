x = "There are %d types of people." % 10
binary = 'binary'
do_not = "don\'t"
y = "Those who know %s and those who %s." % (binary, do_not)
print(x)
print(y)

print("I said: %r." % x)
print("I also said: '%s'." % y)
hilarious = False
jokeEvaluation = "Isn't that joke so funny?! %r"
print(jokeEvaluation % hilarious)
w = "This is the left side of ..."
e = "a string with a right side."
print(w + e)
print()
print()
print(" A N O T H E R   E X E R C I S E ")
print()
print()
print("Mary had a little lamb.")
print("Its fleece are as white as %s." % 'snow')
print("And everywhere that Mary went.")
print("." * 10)  # what would that do

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. Try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, )
print(end7 + end8 + end9 + end10 + end11 + end12)

# At the end of this section, I have come to know that
# 1.    + symbol concatenate strings without adding spaces to the strings
# 2.    , symbol concatenates strings and add a space between the strings


print()
print()
print(" A N O T H E R   E X A M P L E")
print()
print()
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("One", "Two", "Three", "Four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % ("I had this thing", "That you could type up right.",
                   "But it didn't sing", "So I said goodnight."
                   ))
