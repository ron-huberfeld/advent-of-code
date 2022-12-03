from typing import Counter
import functools


def get_input(path):
    with open(path, 'r') as fh:
        return list(map(int, fh.read().split(',')))


def get_crab_fuel(crab_position, count_in_dict, align_position):
    return (abs(crab_position-align_position)) * count_in_dict


def get_result(data, alignment):
    fuel_arr = []
    c = Counter(data)
    for k, v in c.items():
        # print(k,v)
        fuel_arr.append(get_crab_fuel(k, v, alignment))
    # print(fuel_arr)
    return functools.reduce(lambda x, y: x+y, fuel_arr)


# data = get_input('resources/day7_input.txt')
data = get_input('resources/day7_test.txt')
# print("data: ", data)
minimum_fuel = 100000000
mx = max(data)
mn = min(data)
r = mx - mn
print(mn, mx, r)
for i in range(mx + 1):
    res = get_result(data, i)
    if minimum_fuel > res:
        minimum_fuel = res
print(minimum_fuel)
