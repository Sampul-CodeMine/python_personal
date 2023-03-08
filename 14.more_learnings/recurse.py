def calc_sum(x):
    if x == 1:
        return 1
    else:
        return x + calc_sum(x - 1)


add_up = calc_sum(10)
print(add_up)
