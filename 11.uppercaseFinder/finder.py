def find_upper_case(str_args):
    found = []
    for letter in str_args:
        if letter.isupper():
            found.append(letter)
        else:
            continue
        
    if len(found) != 0:
        return found
    else:
        return 'No uppercase letter was found.'


firstStr = 'This is what I was saying about using this function.'
print('\nThe word is: \n"{}"\n\tThe uppercase letters found were:\t{}'.format(firstStr, find_upper_case(firstStr)))

anotherStr = 'These are the days of Elijah, declaring the words of the LORD.'
print('\nThe word is: \n"{}"\n\tThe uppercase letters found were:\t{}'.format(anotherStr, find_upper_case(anotherStr)))
