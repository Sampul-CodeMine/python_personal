# import or include the exit class to your file
from sys import exit


# function to handle the gold room in the game
def gold_room():
    how_much = 0
    print('This room is full of gold. How much do you take?')
    next_response = input('>>  ')  # accepts input
    if '0' in next_response or '1' in next_response:  # if the input has 0 or 1 in it
        how_much = int(next_response)
    else:
        print('Man, Learn to type a number.')  # display an error message and allow user type a response again
        gold_room()

    if how_much < 50:  # if the input is less than 50 win the game and end the game
        print('Nice, you are not ready, you win!')
        exit(0)
    else:
        dead('You greedy bastard!')  # end the game after displaying an error message


# Function to handle tbe bear room part of the game.
def bear_room():
    print('There is a bear here.')
    print('The bear has a bunch of honey.')
    print('The fat bear is in front of another door.')
    print('How are you going to move the bear?')
    bear_moved = False

    while True:
        next_response_question = input('>>  ')  # accepts an input

        if next_response_question == 'take honey':  # if input is take honey, return an error and then end the game
            dead('The bear looks at you then slaps your face off.')
        elif next_response_question == 'taunt bear' and not bear_moved:
            # if taunt bear is entered and bear was not moved then move the bear
            print('The bear has moved from the door. You can go through it now.')
            bear_moved = True
        elif next_response_question == 'taunt bear' and bear_moved:
            # if taunt bear is entered and the bear has been moved previously, display error and end the game.
            dead('The bear gets pissed off and chews your leg off.')
        elif next_response_question == 'open door' and bear_moved:
            # if open door is entered and bear has been moved, go to the room for gold
            gold_room()
        else:
            print('I got no idea what to do.')  # display error and allow user to input an option again


# cthulhuRoom function
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("Hey, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    next_response = input("> ")
    if "flee" in next_response:  # if the input contains the word flee, then start the game all over again
        start()
    elif "head" in next_response:  # if the input has head in it, then it displays an error and end the game
        dead("Well that was tasty!")
    else:  # if no valid input, then rerun the cthulhuRoom function.
        cthulhu_room()


# function to display a message and then ends the application
def dead(why):
    print(why, "Good job!")
    exit(0)


# function to start the game, accepts inputs from the user and then redirect them according to their choices
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    next_response = input("> ")
    if next_response == "left":  # if the input is equal to left then go to the bear_room()unction and execute
        bear_room()
    elif next_response == "right":  # if the input is equal to right then go to the cthulhuRoom function and execute
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")  # displays an error then end the program.


# Game starts or begin execution here by calling the start function
start()
