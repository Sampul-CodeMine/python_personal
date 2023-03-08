# INSERTION SORT PROGRAM
numbers = []


def accept_input():
    try:
        val_resp = int(input("Number Entry: "))
        return val_resp
    except ValueError as err:
        print(err)
        return int(0)


def number_collector():
    resp = 'y'
    input_prompt = 'More Numbers? (y/n) '
    while resp == 'y' or resp == 'Y':
        val = accept_input()
        numbers.append(val)
        resp = input(input_prompt)


def insertion_sort(args):

    for i in range(1, len(args)):
        key = args[i]
        j = i - 1
        while j >= 0 and key < args[j]:
            args[j+1] = args[j]
            j -= 1
        args[j+1] = key

    return args


response = 'y'
prompt = "\nDo you wish to  continue with more calculations? (y/n) "
while response == "y" or response == "Y":
    
    # Do calculation
    numbers.clear()
    number_collector()
    print("RAW NUMBERS:\t{}".format(numbers))

    print("SORTED NUMBERS:\t{}".format(insertion_sort(numbers)))
    response = input(prompt)
print("\n\nThank you for using this software....\n\n")
