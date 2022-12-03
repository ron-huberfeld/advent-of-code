import itertools
from typing import Counter


def get_input(path):
    with open(path, 'r') as fh:
        return list(map(int, fh.read().split(',')))


def get_new_data(data):
    c = Counter(data)
    data = list(map(lambda x: x-1 if x != 0 else 6, data))
    for _ in range(c[0]):
        data.append(8)
    return data


def get_new_data_two(data):
    n = Counter()
    for k, v in data.items():
        if k == 0:
            n[6] += v
            n[8] = v
        else:
            n[k - 1] += v
    return n


def get_count(data, days):
    c = Counter(data)
    for _ in range(days):
        c = get_new_data_two(c)
    # print(data)
    return sum(c.values())


data = get_input('resources/day6_input.txt')
# data = get_input('resources/day6_test.txt')
# print("data: ", data)
# print(get_count(data, 18))
print(get_count(data, 80))
print(get_count(data, 256))
