import string
import re


def get_input(path):
    with open(path, 'r') as fh:
        return fh.read().splitlines()


def is_contains_at_least_three_vowels(item):
    count = 0
    for v in "aeiou":
        count += item.count(v)
    return count >= 3


def is_contains_at_least_one_letter_twice_in_a_row(item):
    for char in string.ascii_lowercase:
        if char * 2 in item:
            return True
    return False


def is_not_contain_strings(item):
    for pair in ["ab", "cd", "pq", "xy"]:
        if (pair not in item):
            return True
    return False


def is_contain_middle_letter(item):
    for char in string.ascii_lowercase:
        pattern = f"{char}.{char}"
        prog = re.compile(pattern)
        if prog.search(item):
            return True
    return False


def is_contain_pair_letters_twice(item):
    for a in string.ascii_lowercase:
        for b in string.ascii_lowercase:
            if item.count(a + b) >= 2:
                return True
    return False


def is_found_match(item):
    return is_contains_at_least_three_vowels(item) and \
        is_contains_at_least_one_letter_twice_in_a_row(item) and \
        is_not_contain_strings(item)


def is_found_match_part2(item):
    return is_contain_pair_letters_twice(item) and is_contain_middle_letter(item)


data = get_input('resources/day5_input.txt')
# print("data: ", data)
count_nice_strings = 0
for item in data:
    if (is_found_match(item)):
        count_nice_strings += 1
print("Day 5 - part I:", count_nice_strings)

data = get_input('resources/day5_input.txt')
count_nice_strings = 0
for item in data:
    if (is_found_match_part2(item)):
        count_nice_strings += 1
print("Day 5 - part II:", count_nice_strings)
