file = open("names_and_marks", "r")
all_marks = 0
counter = 0
for line in file:
    mark = int(line.split(":")[-1])
    all_marks += mark
    counter += 1
print(all_marks, counter)
print(float(all_marks / counter))
