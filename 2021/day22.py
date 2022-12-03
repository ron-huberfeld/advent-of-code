def get_input(path):
    with open(path, 'r') as fh:
        return fh.read().splitlines()


def parse_data(line):
    action, coor = line.split(' ')
    # print(action)
    coordinates = coor.split(',')
    for c in coordinates:
        axis, r = c.split('=')
        print(axis, r)
    # x1 = int(data.split('=')[1:][0].split('..')[0])
    # x2 = int(data.split('=')[1:][0].split('..')[1].split(',')[0])
    # y1 = int(data.split('=')[1:][1].split('..')[0])
    # y2 = int(data.split('=')[1:][1].split('..')[1])
    # a = (x1, y2)
    # b = (x2, y1)
    # return (a, b)


def is_valid_line(line):
    borders = parse_data(line)
    print(borders)
    return True


def get_filtered_data(data):
    filtered = []
    for line in data:
        if is_valid_line(line):
            filtered.append(line)
    return 1


def get_result(data):
    filtered_data = get_filtered_data(data)
    return filtered_data


# data = get_input('resources/day22_input.txt')
data = get_input('resources/day22_test.txt')
# print("data: ", data)
print(get_result(data))
