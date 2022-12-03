from collections import Counter


def get_input(path):
    with open(path, 'r') as fh:
        return fh.read().splitlines()


def create_all_points(tpl1, tpl2):
    # print(tpl1, tpl2)
    points_list = []
    x1, y1 = tpl1
    x2, y2 = tpl2
    if x1 != x2:
        if x1 < x2:
            for num in range(x1, x2 + 1):
                points_list.append((num, y1))
        else:
            for num in range(x2, x1 + 1):
                points_list.append((num, y1))
    else:
        if y1 < y2:
            for num in range(y1, y2 + 1):
                points_list.append((x1, num))
        else:
            for num in range(y2, y1 + 1):
                points_list.append((x1, num))
    # print(points_list)
    return points_list


def create_diag_points(tpl1, tpl2):
    # print(tpl1, tpl2)
    points_list = []
    x1, y1 = tpl1
    x2, y2 = tpl2
    if (x1 == y1 and x2 == y2):
        if x1 < x2:
            for num in range(x1, x2 + 1):
                points_list.append((num, num))
        else:
            for num in range(x2, x1 + 1):
                points_list.append((num, num))
    if (x1 == y2 and y1 == x2):
        if x1 < x2:
            for num in range(x1, x2 + 1):
                points_list.append((num, x2 - num))
        else:
            for num in range(x2, x1 + 1):
                points_list.append((num, x1 - num))
    if (abs(x1-x2) == abs(y1-y2)) and not (x1 == y2 and y1 == x2) and not (x1 == y1 and x2 == y2):
        if x1 < x2:
            needed_range = range(x1, x2 + 1)
            if y1 < y2:
                for num in needed_range:
                    points_list.append((num, y2 + num - x2))
            else:
                for num in needed_range:
                    points_list.append((num, y2 - num + x2))
        else:
            needed_range = range(x2, x1 + 1)
            if y1 < y2:
                for num in needed_range:
                    points_list.append((num, y2 - num + x2))
            else:
                for num in needed_range:
                    points_list.append((num, y2 + num - x2))
    # print(len(points_list),points_list)
    return points_list


def get_overlap_points(data, is_part_two):
    all_points = []
    counter = 0
    for items in data:
        p1, p2 = items.split('->')
        (x1, y1) = tuple(map(int, p1.strip().split(',')))
        (x2, y2) = tuple(map(int, p2.strip().split(',')))
        if x1 == x2 or y1 == y2:
            new_points = create_all_points((x1, y1), (x2, y2))
            all_points += new_points
        if is_part_two:
            if (abs(x1-x2) == abs(y1-y2)):
                new_points = create_diag_points((x1, y1), (x2, y2))
                all_points += new_points
    # points = create_diag_points((2,8), (5,5))
    # a = dict(Counter(points))
    # print(a)
    # print(all_points)
    # a = dict(Counter(all_points))
    counter_x = Counter(item for item in all_points)
    # print(counter_x)
    for item in counter_x.values():
        if item >= 2:
            counter += 1
    return counter


data = get_input('resources/day5_input.txt')
# data = get_input('resources/day5_test.txt')
# print("data: ", data)
# print(get_overlap_points(data, False))
print(get_overlap_points(data, True))
