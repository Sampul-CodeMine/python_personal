prompt = "Input a value (numeric): "
resp = int(input(prompt))

flag = 1

for i in range(2, resp):
    if (resp % i) == 0:
        print("{} is not a prime number.".format(resp))
        print("{} times {} is {}".format(i, (resp//i), resp))
        flag = 0
        break
if flag == 1:
    print("{} is a prime number.".format(resp))
