print("\n===============================================================")
print("==================== SIMPLE CALCULATOR ========================")
print("===============================================================")
# === SIMPLE CALCULATOR PROGRAM =======


def accept_value():
    while True:            
        try:
            val_resp = float(input("\nEnter Value: (numeric) "))
            break
        except ValueError as err:
            print("Error: Not numeric: {}".format(err))
    return val_resp


def accept_ops():
    ops_resp = input("\nEnter Operator: +, -, *, /, %:\t")
    return ops_resp


def add(num1, num2):
    result = num1 + num2
    return result


def subtract(num1, num2):
    result = num1 - num2
    return result


def multiply(num1, num2):
    result = num1 * num2
    return result


def divide(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError as err:
        return "Error: Division by zero. ", err


def modulo_division(num1, num2):

    try:
        result2 = num1 % num2
        result = "The remainder is " + str(result2)
        return result
    except ZeroDivisionError as err:
        return "Error: Integer division by zero.", err


def calculate():
    first_num = accept_value()
    operator = accept_ops()
    second_num = accept_value()

    if operator == "+":
        final_result = "The sum of {} {} {} = {}".format(first_num, operator, second_num, add(first_num, second_num))
        print("\nAnswer: " + final_result)
    elif operator == "-":
        final_result = "The difference between {} {} {} = {}".format(first_num, operator, second_num, subtract(first_num, second_num))
        print("\nAnswer: " + final_result)
    elif operator == "*":
        final_result = "The product of {} {} {} = {}".format(first_num, operator, second_num, multiply(first_num, second_num))
        print("\nAnswer: " + final_result)
    elif operator == "/":
        final_result = "{} {} {} = {}".format(first_num, operator, second_num, divide(first_num, second_num))
        print("\nAnswer: " + final_result)
    elif operator == "%":
        final_result = "The remainder from the division of {} {} {} = {}".format(first_num, operator, second_num, modulo_division(first_num, second_num))
        print("\nAnswer: " + final_result)
    else:
        final_result = "Invalid Operator"
        print("\n" + final_result)


user_response = "y"
prompt = "\nDo you wish to  continue with more calculations? (y/n) "
while user_response == "y" or user_response == "Y":
    calculate()
    user_response = input(prompt)

print("\n\nThank you for using this software....\n\n")
