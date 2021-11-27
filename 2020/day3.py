def get_input(path):
    with open(path, 'r') as fh:
        return fh.read().splitlines()


def is_tree(c):
    return c == '#'


def get_count_per_slope(data, slope):
    slope_counter = 0
    for i, line in enumerate(data):
        location = (slope * i) % len(line)
        # print(i, location, line)
        if is_tree(line[location]):
            slope_counter += 1
    # print(slope_counter)
    return slope_counter

def get_count_per_2_down(data):
    new_data = []
    for i, line in enumerate(data):
        if (i % 2 == 0):
            new_data.append(line)
    return get_count_per_slope(new_data, 1)

# _file = 'resources/day3_test.txt'
_file = 'resources/day3_input.txt'
data = get_input(_file)
# print(data)
counter = get_count_per_slope(data, 3)
print("Day 3 - part I:", counter)

data = get_input(_file)
# print(data)
interval = [1, 3, 5, 7]
down = 1
counter = 1
for slope in interval:
    counter *= get_count_per_slope(data, slope)
counter *= get_count_per_2_down(data)
print("Day 3 - part II:", counter)
