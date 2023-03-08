from math import *

print("An Exponential Power Function==================\n")


def raise_to_power(base, power):
    result = 1
    for values in range(power):
        result = result * base

    return result


def accept_base_input():
    prompt = "Enter the Base Number: "
    return float(input(prompt))


def accept_power_input():
    try:
        prompt = "Enter the Power: "
        val = input(prompt)
        return int(val)
    except ValueError:
        print("Integer required for the power value. Float value was supplied.")
        exit(0)


base_value = accept_base_input()
power_val = accept_power_input()

print(
    str(base_value) + " raised to the power of " + str(power_val) + " = " + str(raise_to_power(base_value, power_val)))
