from itertools import combinations


def get_data_from_file(path):
    with open(path, 'r') as fh:
        return list(fh.read().splitlines())


# _file = 'resources/day1_test.txt'
_file = 'resources/day1_input.txt'
data = get_data_from_file(_file)
r = 2
for item in list(combinations(data, r)):
    num1 = int(item[0])
    num2 = int(item[1])
    if num1 + num2 == 2020:
        print("Day1 - part I:", num1 * num2)

data = get_data_from_file(_file)
r = 3
for item in list(combinations(data, r)):
    num1 = int(item[0])
    num2 = int(item[1])
    num3 = int(item[2])
    if num1 + num2 + num3 == 2020:
        print("Day1 - part II:", num1 * num2 * num3)
