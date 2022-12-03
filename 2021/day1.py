import collections
import itertools


def get_input(path):
    with open(path, 'r') as fh:
        yield from map(int, fh)


def sliding_window(iterable, n):
    # ** from itertools recipes **
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(itertools.islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def get_max_depth(data):
    count = 0
    max_value = 100000
    for item in data:
        if item > max_value:
            count += 1
        max_value = item
    return count


data = get_input('resources/day1_input.txt')
# print("data: ", data)
print("Day1 - part I:", get_max_depth(data))

# part II
data = get_input('resources/day1_input.txt')
# data = get_input('resources/day1_test.txt')
new_data = []
result = list(sliding_window(data, 3))
for item in result:
    inner_count = 0
    for num in item:
        inner_count += int(num)
    new_data.append(inner_count)
# print(new_data)
print("Day1 - part II:", get_max_depth(new_data))
