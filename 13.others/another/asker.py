name_values = ["First Name", "Last Name"]
names = ""


def ask_name(name):
    prompt = "Enter " + name + ": "
    resp = input(prompt)
    return resp


for i in range(len(name_values)):
    names += ask_name(name_values[i]) + " "

print("You are welcome", names)
