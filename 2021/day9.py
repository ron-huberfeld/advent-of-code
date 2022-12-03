from functools import reduce

DIRECTION = dict(zip(('up', 'down', 'left', 'right'),
                     ((0, -1), (0, 1), (-1, 0), (1, 0))))


def get_input(path):
    with open(path, 'r') as fh:
        return fh.read().splitlines()


def create_grid(data):
    grid = dict()
    for i, row in enumerate(data):
        for j, digit in enumerate(row):
            grid[(i, j)] = int(data[i][j])
    return grid


def side_point(point, side):
    return tuple(map(sum, zip(point, DIRECTION[side])))


def is_valid_point(tpl, board):
    return tpl in board


def is_other_point_bigger(other_point, point, board):
    if not is_valid_point(other_point, board) or board[other_point] > board[point]:
        return True
    return False


def is_lowest(point, board):
    if is_other_point_bigger(side_point(point, 'up'), point, board) and \
            is_other_point_bigger(side_point(point, 'down'), point, board) and \
            is_other_point_bigger(side_point(point, 'left'), point, board) and \
            is_other_point_bigger(side_point(point, 'right'), point, board):
        return True
    return False


def get_points_to_side(point, board, side, visited):
    other_point = side_point(point, side)
    if not is_valid_point(other_point, board) or \
            board[other_point] == 9 or \
            board[other_point] <= board[point] or \
            other_point in visited:
        return {point}
    x = get_basin_points(other_point, board)
    return set.union(visited, x)


def get_basin_points(point, board):
    visited = {point}
    for direction in DIRECTION.keys():
        visited = set.union(visited, get_points_to_side(
            point, board, direction, visited))
    return visited


def get_basins_sizes(risk_points, board):
    three_largest_basins = []
    for point in risk_points:
        basin_size = len(get_basin_points(point, board))
        three_largest_basins.append(basin_size)
        if len(three_largest_basins) > 3:
            three_largest_basins.remove(min(three_largest_basins))
    risk_points = reduce((lambda x, y: x * y), three_largest_basins)
    return risk_points


def get_lowest_points_total(board):
    risk_points = []
    sum_of_risks = 0
    for point in board.keys():
        if is_lowest(point, board):
            risk_points.append(point)
            sum_of_risks += (1 + board[point])
    print("Day9 - part II:", get_basins_sizes(risk_points, board))
    return sum_of_risks


def get_result(data):
    board = create_grid(data)
    total = get_lowest_points_total(board)
    return total


data = get_input('resources/day9_input.txt')
# data = get_input('resources/day9_test.txt')
# print("data: ", data)
print("Day9 - part I:", get_result(data))
