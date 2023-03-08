# more on variables
myName = 'Ehigboria Dukeson'
myAge = 36
myHeight = 69.0  # inch
myWeight = 63.0  # kg
myEyes = 'Brown'
myTeeth = 'white'
myHair = 'Dark brown'

# Let us now work with the variables and print them out
print("Let us talk about {}.".format(myName))
print("He is {} inches tall.".format(myHeight))
print("He is {} kg heavy.".format(myWeight), " I guess that is not too heavy.")
print("He has got {} eyes and {} hair.".format(myEyes, myHair))
print("His teeth are usually {} depending on the coffee.".format(myTeeth))

# this line is tricky! Try to get it exactly right
print("If I add {}, {}, and {} I'd get {}.".format(myAge, myHeight, myWeight, (myAge + myHeight + myWeight)))

# A simple application to convert weights from kilogram to pounds
weightVal = myWeight * 2.20462
print('')
print("Converting {}'s weight {}kg to pounds, you will get {}pds".format(myName, myWeight, weightVal))

# A simple application to convert lengths from inches to feet
# converting from inch to foot, divide the value of foot with 12
# converting from foot to inch, multiply the value of the foot with 12
heightVal = myHeight / 12
print('')
print("Converting {}'s height {} inches to feet, you will get {}fts".format(myName, myHeight, heightVal))
print()
