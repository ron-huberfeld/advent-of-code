def get_input(path):
    with open(path, 'r') as fh:
        return fh.read().splitlines()


def isValid_part1(rule, password):
    (r, c) = rule.split(" ")
    (mini, maxi) = r.split("-")
    num_of_occur = password.count(c)
    if num_of_occur < int(mini) or num_of_occur > int(maxi):
        return False
    return True


def isValid(rule, password):
    (r, c) = rule.split(" ")
    (first, second) = r.split("-")
    first_val = password[int(first)-1]
    second_val = password[int(second)-1]
    if (c == first_val and c != second_val) or (c != first_val and c == second_val):
        return True
    return False


# _file = 'resources/day2_test.txt'
_file = 'resources/day2_input.txt'
data = get_input(_file)
counter = 0
for line in data:
    (rule, password) = line.split(': ')
    if isValid_part1(rule, password):
        counter += 1
print("Day2 - part I:", counter)
data = get_input(_file)
counter = 0
for line in data:
    (rule, password) = line.split(': ')
    if isValid(rule, password):
        counter += 1
print("Day2 - part II:", counter)
