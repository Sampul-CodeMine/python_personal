# Functions that accepts Parameters
def accept_name():
    print()
    prompt = "Enter Your Name: "
    name = input(prompt)
    return name


def say_hello(person):
    resp = "Hello " + str(person) + "!\nHope you are having a wonderful time coding with Python Programming Language."
    print(resp)


say_hello(accept_name())
