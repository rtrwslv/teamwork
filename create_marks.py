import random


def create_marks():
    file = open("names", "r")
    try:
        open("names_and_marks", "r")
    except FileNotFoundError:
        file2 = open("names_and_marks", "w")
        bottom = 2
        top = 5
        mass = file.readlines()
        for i in mass:
            file2.write(i.replace("\n", "") + ": " +
                        str(random.randint(bottom, top)) + "\n")
