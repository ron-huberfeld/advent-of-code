DIRECTION = ((-1, -1), (0, -1), (1, -1), (1, 0),
             (1, 1), (0, 1), (-1, 1), (-1, 0))


def get_input(path):
    with open(path, 'r') as fh:
        return fh.read().splitlines()


def concat(a, b):
    return f"{a}{b}"


def print_board(board):
    row = ''
    row_num = 0
    for i, j in board.items():
        if i[0] != row_num:
            print(row)
            row = ''
            row_num += 1
        row = concat(row, j)
    print(row)


def create_grid(data):
    grid = dict()
    for i, row in enumerate(data):
        for j, digit in enumerate(row):
            grid[(i, j)] = int(data[i][j])
    return grid


def increase_enrergy_level_by_one(board):
    for k, v in board.items():
        board[k] = v+1
    return board


def is_valid_point(tpl, board):
    return tpl in board


def increase_enrergy_level_by_one_to_adjacent(flush_points, board):
    for point in flush_points:
        for direction in DIRECTION:
            increment_point = tuple(map(sum, zip(direction, point)))
            if is_valid_point(increment_point, board):
                board[increment_point] += 1
    return board


def decrease_energy_to_zero(board):
    for k, v in board.items():
        if v > 9:
            board[k] = 0
    return board


def get_flush_points(board, visited):
    new_flush_points = []
    for k, v in board.items():
        if v > 9 and k not in visited:
            new_flush_points.append(k)
    if len(new_flush_points) == 0:
        return new_flush_points
    board = increase_enrergy_level_by_one_to_adjacent(new_flush_points, board)
    visited += new_flush_points
    return get_flush_points(board, visited)


def get_count_per_cycle(board, step):
    # print("step:", step)
    # print_board(board)
    board = increase_enrergy_level_by_one(board)
    flush_points = []
    flush_points += get_flush_points(board, flush_points)
    board = decrease_energy_to_zero(board)
    return len(flush_points)


def get_board_per_step(board):
    board = increase_enrergy_level_by_one(board)
    flush_points = []
    flush_points += get_flush_points(board, flush_points)
    board = decrease_energy_to_zero(board)
    return board


def get_result(data, num):
    board = create_grid(data)
    flush_count = 0
    for step in range(num):
        flush_count += get_count_per_cycle(board, step)
    return flush_count


def is_board_full(board):
    for v in board.values():
        if v != 0:
            return False
    return True


def get_part_2_result(data, num):
    board = create_grid(data)
    for step in range(1, num):
        board = get_board_per_step(board)
        if is_board_full(board):
            return step


data = get_input('resources/day11_input.txt')
# data = get_input('resources/day11_test.txt')
# data = get_input('resources/day11_test2.txt')
# print("data: ", data)
print("Day11 - part I:", get_result(data, 100))
print("Day11 - part II:", get_part_2_result(data, 1000))
