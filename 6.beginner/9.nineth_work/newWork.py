from sys import argv

scriptName, name, age, gender, height, weight = argv
age = float(age)
height = float(height)
weight = float(weight)
newWeight = weight * 2.20462
newHeight = height / 12

print("""
    Hello {}.
    You are {} years old and {} by gender.
    You are {} in inches that is {}feet in height.
    Also, you are {} kg that is {} pounds in weight.
""".format(name, age, gender, height, newHeight, weight, newWeight))

print()
print()
print("= = A N O T H E R  E X E R C I S E = =")
prompt = ':>>> '
print()
print("Hi %s, I'm the %s script." % (name, scriptName))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % name)
likes = input(prompt)
print("Where do you live %s?" % name)
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)
print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))
print()
print()
