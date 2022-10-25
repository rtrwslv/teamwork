import os


def test_create_marks():
    assert os.path.exists("names_and_marks") is True


def test_average_value_calculation():
    file = open("names_and_marks_for_test", "r")
    all_marks = 0
    counter = 0
    for line in file:
        mark = int(line.split(":")[-1])
        all_marks += mark
        counter += 1
    assert float("{:.2f}".format(all_marks / counter)) == 3.33
