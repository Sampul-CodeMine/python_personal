import os as op_sys
import time

seconds = float(0)
minutes = int(0)
hours = int(0)

run = input("Enter R to run the program: ")

while run.lower() == 'r':
    if seconds > 59:
        seconds = 0
        minutes += 1
    if minutes > 59:
        minutes = 0
        hours += 1
    op_sys.system('cls')
    seconds = (seconds + .1)
    print("{} : {} : {}".format(hours, minutes, seconds))
    time.sleep(.1)

