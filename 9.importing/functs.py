import random

feet_in_mil = 5280
meters_in_kilometer = 1000
instruments = ["Percussion", "Strings", "Wind", "Electric"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)