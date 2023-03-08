# TO create a function in python, you use the keyword "def"
# def functionName: This is how to define a functionName
def say_hi():
    print("")
    name = accept_name()
    print()
    display = "Hello " + str(name) + "! Welcome to the use of functions in the Python Programming Language."
    print(display)


def accept_name():
    # This function is used to accept inputs in the form of a username from the user
    prompt = "Enter Your Name: "
    name = input(prompt)
    return name


say_hi()
