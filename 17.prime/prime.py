# import os


def test_prime(val):
    output = ''
    for x in range(2, val):
        if val % x == 0:
            return False
    return val > 1


prime_nos = []
answer = 'y'
prompt = 'Do you wish to try another? (y/n) '
while answer == 'y':
    try:
        os.system('cls')
        num = int(input('Enter A Positive Number: '))
        for v in range(1, num+1):
            if test_prime(v):
                prime_nos.append(v)
        print('\n\nPRIME NUMBERS FROM 1 TO', num, '=====================\n')
        print('Prime Numbers: {}\n'.format(prime_nos))
    except ValueError:
        print('Number Required.')
        continue
    answer = input(prompt)
       