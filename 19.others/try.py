# def make_sum(*args):
#     sum = 0
#     for num in (args):
#         sum += num
#
#         return sum
#
# print(make_sum(10, 20, 30, 40))


def make_sum(*args):
    sum = 0
    for num in (args):
        sum += num

    return sum


print(make_sum(10, 20, 30, 40))