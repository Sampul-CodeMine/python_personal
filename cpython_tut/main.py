#!/usr/bin/python3

def accept_val() -> int:
    while True:
        try:
            data = int(input("Enter a Number: "))
            return data
        except (ValueError, TypeError):
            print("Invalid data type.")


if __name__ == "__main__":

    from funcs import add, sub, mult, divi

    resp = 'y'
    question = """
    1.\t[Addition]
    2.\t[Subtraction]
    3.\t[Multiplication]
    4.\t[Division]
    """
    while resp in 'yY':
        f_val = accept_val()
        s_val = accept_val()

        oper = input(question + "Choose:\t")
        if oper == "1":
            print(f"{f_val:d} + {s_val:d} = {add(f_val, s_val):d}")
        elif oper == "2":
            print(f"{f_val:d} - {s_val:d} = {sub(f_val, s_val):d}")
        elif oper == "3":
            print(f"{f_val:d} x {s_val:d} = {mult(f_val, s_val):d}")
        elif oper == "4":
            result = divi(f_val, s_val)
            if result is None:
                print(f"{f_val:d} / {s_val:d}:\tCannot divide by zero")
            else:
                print("{:d} / {:d} = {:.2f}".format(f_val, s_val, result))
        else:
            print("Invalid option selected")

        resp = input("Do you wish to continue (y/n) ? ")

