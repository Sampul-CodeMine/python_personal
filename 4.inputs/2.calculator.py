print('SIMPLE CALCULATOR\n')
# === SIMPLE CALCULATOR PROGRAM =======

def acceptInput():
    num = 0
    while True:
        try:
            num = float(input("Enter a Number: "))
            break
        except:
            print("Please provide a numeric data.")
    return num
        

num1 = acceptInput()
num2 = acceptInput()

result = (num1 + num2)
print("The sum of {} and {} is {}.".format(num1, num2, result))
