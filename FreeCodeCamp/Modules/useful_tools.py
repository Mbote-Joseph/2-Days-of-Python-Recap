import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)


def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def get_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def get_number_float(question, low, high):
    response = None
    while response not in range(low, high):
        response = float(input(question))
    return response


def get_number_float_2(question, low, high):
    response = None
    while response not in range(low, high):
        response = float(input(question))
    return response


    