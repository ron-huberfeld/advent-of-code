import itertools
from collections import Counter


def get_input(path):
    with open(path, 'r') as fh:
        return fh.read().splitlines()


def concat(a, b):
    return f"{a}{b}"


def bit_to_dec(value):
    return int(value, 2)


def get_most_common(num, data_size):
    if num >= (data_size - num):
        return '1'
    return '0'


def flip_bit(value):
    return value.replace('1', '2').replace('0', '1').replace('2', '0')


def get_result(data):
    gamma_rate = ''
    epsilon_rate = 0
    y = dict()
    x = dict()
    data_size = len(data)
    for item in data:
        for index, digit in enumerate(item):
            y[index] = int(digit)
        if x == {}:
            x.update(y)
        else:
            x = dict(Counter(x)+Counter(y))
    for i, j in x.items():
        gamma_rate = concat(gamma_rate, get_most_common(j, data_size))
        epsilon_rate = flip_bit(gamma_rate)
    return bit_to_dec(gamma_rate) * bit_to_dec(epsilon_rate)


def get_list_for_most_common(data):
    return get_most_common(sum(list(map(int, data))), len(data))


def get_most_common_map(data, index):
    x = []
    for item in data:
        y = list(itertools.islice(item, index, index+1))
        x += y
        most_common = get_list_for_most_common(x)
    return most_common


def get_filtered_data(data, index, most_common, is_included):
    if is_included:
        return list(itertools.filterfalse(lambda z: not z[index] == most_common, data))
    return list(itertools.filterfalse(lambda z: z[index] == most_common, data))


def get_data_generator(data, index, include_filter):
    if len(data) > 1 and index < len(data[0]):
        most_common = get_most_common_map(data, index)
        new_data = get_filtered_data(data, index, most_common, include_filter)
        index += 1
        return get_data_generator(new_data, index, include_filter)
    return data


def get_oxygen_generator_rating(data):
    data = get_data_generator(data, 0, True)
    return bit_to_dec(data[0])


def get_co2_scrubber_rating(data):
    data = get_data_generator(data, 0, False)
    return bit_to_dec(data[0])


data = get_input('resources/day3_input.txt')
# data = get_input('resources/day3_test.txt')
print("Day3 - part I:", get_result(data))
oxy = get_oxygen_generator_rating(data)
crb = get_co2_scrubber_rating(data)
print("Day3 - part II:", oxy*crb)
