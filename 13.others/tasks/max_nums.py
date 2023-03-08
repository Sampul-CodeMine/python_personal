num_seq = []


def accept_data():  # method to accept inputs
    count = 1
    while count <= 3:
        var = int(input("Enter Value: "))
        num_seq.append(var)
        count += 1
    return num_seq


def find_max(a=0, b=0, c=0):  # method to find the largest number from a list of numbers
    if (a == 0) and (b == 0) and (c == 0):
        ans = "No largest number. Values provided are {}, {}, and {}.".format(a, b, c)
        return ans
    else:
        if (a >= b) and (a >= c):
            largest = a
        elif (b >= a) and (b >= c):
            largest = b
        else:
            largest = c
        resp = "The largest number from {}, {}, and {} = {}.".format(a, b, c, largest)
        return resp


accept_data()
answer = find_max(num_seq[0], num_seq[1], num_seq[2])
print(answer)
