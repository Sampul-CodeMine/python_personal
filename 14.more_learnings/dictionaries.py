data = {}
print("Welcome to this simple Data Collection Method using Python Dictionaries")
while True:
    info = []
    print("==== OPTIONS ====")
    print("P  =  [P]ut\nG  =  [G]et\nL  =  [L]ist\nQ  =  [Q]uit")
    action = input("Response: ")
    if action == 'P' and action.isupper():
        key = input("Enter Key: ")
        data_items = ['Name', 'Age', 'Sex']
        for i in range(len(data_items)):
            prompt = "Enter " + data_items[i] + ": "
            data_values = input(prompt)
            info.append(data_items[i] + ": " + data_values)
        data[key] = info
    elif action == 'G' and action.isupper():
        get_key = input("Enter your Key: ")
        if get_key not in data:
            print("You do not have any data in the dictionary with such key")
        else:
            print("Your data in the dictionary is: {}".format(data[get_key]))
    elif action == 'L' and action.isupper():
        print("Dictionary Content:\n{}".format(data))
    elif action == 'Q' and action.isupper():
        print("Thank you for using this application.")
        break
    else:
        print("Wrong Response... Try again")
        continue
