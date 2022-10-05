import random
file = open("names", "r")
file2 = open("names and marks", "w")
mass = file.readlines()
for i in mass:
    file2.write(i.replace("\n", "") + ": " + str(random.randint(2, 5)) + "\n")