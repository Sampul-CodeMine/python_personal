from sys import exit


def start_game():
    login_things = []
    print()
    print('=====================================================================================================')
    print(' ================ S T A R T   T H E   A N I M A L   I N F O   G A M E   N O W ! ! ! ================ ')
    print('=====================================================================================================')
    print()

    prompt = input('Enter Your Name: ')
    name = prompt.upper()

    login_things.append(name)
    try:
        prompt = int(input('Enter Your Age: '))
        age = prompt
        login_things.append(age)
        check_details(login_things[0], login_things[1])
        exit(0)

    except ValueError:
        response = 'Please provide a valid age. Numeric age is needed.'
        end_game(response)
        exit(0)


def check_details(name, age):
    print()
    if age < 18:
        goto_kid_game(name, age)
        exit(0)
    elif age >= 18:
        goto_adult_game(name, age)
        exit(0)
    else:
        response = 'Hello', name + '! Your age is not certain.'
        end_game(response)
        exit(0)


def goto_kid_game(name, age):
    pets = ['cat', 'dog', 'monkey', 'parrot']
    print()
    print('You need to choose from the list of pets:\n1. Cat\n2. Dog\n3. Monkey\n4. Parrot\n')
    resp = input('Choose Pet : > ').lower()
    if resp in pets:
        chosen = resp
        goto_pet_response(name, age, chosen)
        exit(0)
    else:
        print()
        print('Hello {}! That pet is not on the list.'.format(name))
        print()
        goto_kid_game(name, age)
        exit(0)


def goto_pet_response(name, age, chosen):
    if chosen == 'cat':
        cat_info(name, age)
    elif chosen == 'dog':
        dog_info(name, age)
    elif chosen == 'monkey':
        monkey_info(name, age)
    elif chosen == 'parrot':
        parrot_info(name, age)
    else:
        print('The choice you made is not available or not ready.')
        goto_kid_game(name, age)
        exit(0)


def cat_info(name, age):
    print()
    print('===============================================')
    print(' ======= C A T    I N F O R M A T I O N ====== ')
    print('===============================================')
    print()
    resp = input('Do you wish to choose another pet? (y/n) >  ')
    if (resp == 'Y' or resp == 'y') and age < 18:
        goto_kid_game(name, age)
        exit(0)
    else:
        end_game('You chose to stop viewing pet information')
        exit(0)


def dog_info(name, age):
    print()
    print('===============================================')
    print(' ======= D O G    I N F O R M A T I O N ====== ')
    print('===============================================')
    print()
    resp = input('Do you wish to choose another pet? (y/n) >  ')
    if (resp == 'Y' or resp == 'y') and age < 18:
        goto_kid_game(name, age)
        exit(0)
    else:
        end_game('You chose to stop viewing pet information')
        exit(0)


def monkey_info(name, age):
    print()
    print('===============================================')
    print(' ==== M O N K E Y   I N F O R M A T I O N ==== ')
    print('===============================================')
    print()
    resp = input('Do you wish to choose another pet? (y/n) >  ')
    if (resp == 'Y' or resp == 'y') and age < 18:
        goto_kid_game(name, age)
        exit(0)
    else:
        end_game('You chose to stop viewing pet information')
        exit(0)


def parrot_info(name, age):
    print()
    print('===============================================')
    print(' ==== P A R R O T   I N F O R M A T I O N ==== ')
    print('===============================================')
    print()
    resp = input('Do you wish to choose another pet? (y/n) >  ')
    if (resp == 'Y' or resp == 'y') and age < 18:
        goto_kid_game(name, age)
        exit(0)
    else:
        end_game('You chose to stop viewing pet information')
        exit(0)


def goto_adult_game(name, age):
    predators = ['bear', 'elephant', 'lion', 'tiger']
    print()
    print('You need to choose from the list of predators:\n1. Bear\n2. Elephant\n3. Lion\n4. Tiger\n')
    resp = input('Choose Predator : > ').lower()
    if resp in predators:
        chosen = resp
        goto_predator_response(name, age, chosen)
        exit(0)
    else:
        print()
        print('Hello {}! That predator is not on the list.'.format(name))
        print()
        goto_adult_game(name, age)
        exit(0)


def goto_predator_response(name, age, chosen):
    if chosen == 'bear':
        bear_info(name, age)
    elif chosen == 'elephant':
        elephant_info(name, age)
    elif chosen == 'lion':
        lion_info(name, age)
    elif chosen == 'tiger':
        tiger_info(name, age)
    else:
        print('The choice you made is not available or not ready.')
        goto_adult_game(name, age)
        exit(0)


def bear_info(name, age):
    print()
    print('===============================================')
    print('======= B E A R    I N F O R M A T I O N ======')
    print('===============================================')
    print()
    resp = input('Do you wish to choose another predator? (y/n) >  ')
    if (resp == 'Y' or resp == 'y') and age >= 18:
        goto_adult_game(name, age)
        exit(0)
    else:
        end_game('You chose to stop viewing pet information')
        exit(0)


def elephant_info(name, age):
    print()
    print('===============================================')
    print('=== E L E P H A N T   I N F O R M A T I O N ===')
    print('===============================================')
    print()
    resp = input('Do you wish to choose another predator? (y/n) >  ')
    if (resp == 'Y' or resp == 'y') and age >= 18:
        goto_adult_game(name, age)
        exit(0)
    else:
        end_game('You chose to stop viewing pet information')
        exit(0)


def lion_info(name, age):
    print()
    print('===============================================')
    print('======= L I O N    I N F O R M A T I O N ======')
    print('===============================================')
    print()
    resp = input('Do you wish to choose another predator? (y/n) >  ')
    if (resp == 'Y' or resp == 'y') and age >= 18:
        goto_adult_game(name, age)
        exit(0)
    else:
        end_game('You chose to stop viewing pet information')
        exit(0)


def tiger_info(name, age):
    print()
    print('================================================')
    print('====== T I G E R    I N F O R M A T I O N ======')
    print('================================================')
    print()
    resp = input('Do you wish to choose another predator? (y/n) >  ')
    if (resp == 'Y' or resp == 'y') and age >= 18:
        goto_adult_game(name, age)
        exit(0)
    else:
        end_game('You chose to stop viewing pet information')
        exit(0)

# this is a function that will display an error message and then proceed to either end the
# program or continue depending on what option the user chooses


def end_game(resp):
    print()
    print(resp)
    print()
    inquire = input('Do you want to play the game again? (y/n) _ ')
    if inquire == 'y' or inquire == 'Y':
        start_game()
    else:
        print()
        print('Thank you for using this game.')
        print()
        exit(0)


start_game()
