# my_list = [9,0,8,8,0,4,4,9,5,2,0,8,1,0,3,3,0,8,1,3]
#
#
# def count_number(n, mlist):
#     result = mlist.count(n)
#     if result >= 2:
#         print("the number {} appears {} times in {}".format(n, result, mlist))
#     else:
#         print("the number {} appears {} times in {}".format(n, result, mlist))
#
# n = int(input("Enter a number from 0 - 9: "))
# count_number(n, my_list)


import random
my_list = []
for i in range(0, 30):
    my_list.append(random.randint(0, 10))


def count_number(n, mlist):
    result = mlist.count(n)
    if result >= 2:
        print("the number {} appears {} times in {}".format(n, result, mlist))
    else:
        print("the number {} appears {} times in {}".format(n, result, mlist))


n = int(input("Enter a number from 0 - 10: "))
count_number(n, my_list)