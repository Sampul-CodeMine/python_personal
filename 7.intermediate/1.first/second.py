print('You enter a dark room with two doors. Do you go through door #1 or door #2?')
door = int(input(':>> '))
if door == 1:
    print('There is a giant bear here eating a cheese cake. What do you want?')
    print('1. Take the cake.')
    print('2. Scream at the bear.')
    resp = int(input('>> '))
    if resp == 1:
        print('The bear eats your face off. Good job!')
    elif resp == 2:
        print('The bear eats your leg off. Good job!')
    else:
        print('Well, doing %s is probably better. Bear runs away.' % resp)
elif door == 2:
    print("You stare into the endless abyss at Cthulhu's retina.")
    print('1. Blueberries.')
    print('2. Yellow Jacket Clothespins.')
    print('3. Understanding revolvers yelling melodies.')
    resp = int(input('>> '))
    if resp == 1 or resp == 2:
        print('The body survives powered by a mind of jello. Good Job!')
    else:
        print('The insanity rots your eyes into a pool of muck. Good Job!')
else:
    print('You stumble around and fall on a knife and die. Good job!')
