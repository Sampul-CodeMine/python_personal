print("\n==========================================================\n")
print("SQUARE FUNCTION")


def squares(x):
    return x * x


new_square = lambda x: x * x

val = 5
best_method = squares(val)
print("Using the right function with def, the square of {} is {}.".format(val, best_method))

not_too_good_method = new_square(val)
print("Using the anonymous function lambda, the square of {} is {}.".format(val, not_too_good_method))

print("\n==========================================================\n")
print("SUMMATION FUNCTION")

a = 10
b = -10
c = 20


def addition(u, v, w):
    return a + b + c


new_addition = lambda u, v, w: u + v + w

first_sum = addition(a, b, c)
print("Using def function declaration, the sum of {}, {}, and {} is {}.".format(a, b, c, first_sum))

second_sum = new_addition(a, b, c)
print("Using the anonymous function lambda, the sum of {}, {}, and {} is {}.".format(a, b, c, second_sum))