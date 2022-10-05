import random
file = open("names", "r")
file2 = open("names and marks", "w")
bottom = 2
top = 5
mass = file.readlines()
for i in mass:
    file2.write(i.replace("\n", "") + ": " + str(random.randint(bottom, top)) + "\n")