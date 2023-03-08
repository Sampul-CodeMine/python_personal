# BUBBLE SORT PROGRAM
numbers = []


def accept_input():
    try:
        val_resp = int(input("Number Entry: "))
        return val_resp
    except ValueError as err:
        return int(0)


def number_collector():
    resp = 'y'
    inputPrompt = 'More Numbers? (y/n) '
    while resp == 'y' or resp == 'Y':
        val = accept_input()
        numbers.append(val)
        resp = input(inputPrompt)


def bubble_sort(arrs):
    n = len(arrs)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arrs[j] > arrs[j+1]:
                arrs[j], arrs[j+1] = arrs[j+1], arrs[j]

    return arrs


response = 'y'
prompt = "\nDo you wish to  continue with more calculations? (y/n) "
while response == "y" or response == "Y":
    
    #Do calculation
    numbers.clear()
    number_collector()
    print("RAW NUMBERS:\t{}".format(numbers))

    print("SORTED NUMBERS:\t{}".format(bubble_sort(numbers)))
    response = input(prompt)
print ("\n\nThank you for using this software....\n\n")
