CUT = dict(zip(('fold along x', 'fold along y'), ((-1, 0), (0, 1))))


def get_input(path):
    with open(path, 'r') as fh:
        return fh.read().splitlines()


def get_point(line):
    return tuple(map(int, line.split(',')))


def get_fold_location(data):
    x = data.split('=')
    axis = CUT[x[0]]
    return tuple(a*int(x[1]) for a in axis)


def get_fold_item(item, first_fold):
    x, y = first_fold
    if x == 0 and y != 0:
        if item[1] > y:
            return (item[0], y - (item[1] - y))
        else:
            return item
    if item[0] > x:
        return (x - (item[0] - x), item[1])
    else:
        return item


def get_data_after_fold(board, first_fold):
    new_data = []
    for item in board:
        new_point = get_fold_item(item, first_fold)
        new_data.append(new_point)
    return new_data


def get_dot_count(data):
    first_fold = 0
    board = []
    line_num = 0
    while(len(data[line_num]) > 0):
        board.append(get_point(data[line_num]))
        line_num += 1
    first_fold = get_fold_location(data[line_num+1])
    new_data = get_data_after_fold(board, first_fold)
    # print(new_data)
    new_data = set(new_data)
    # print(new_data)
    return len(new_data)


data = get_input('resources/day13_input.txt')
# data = get_input('resources/day13_test.txt')
# print("data: ", data)
print(get_dot_count(data))
