import itertools

from numpy.core.defchararray import count


def get_input(path):
    with open(path, 'r') as fh:
        return fh.read().splitlines()


def get_boards(data):
    borads_map = dict()
    borad_number = 0
    board_array = []
    for item in data:
        if item == "":
            borad_number += 1
            borads_map[borad_number] = board_array
            board_array = []
        else:
            board_array.append(item)
    borads_map[borad_number + 1] = board_array
    # print(borads_map)
    return borads_map


def replace_num_in_boards(num, boards):
    new_boards = dict()
    for idx, board in boards.items():
        new_board = []
        for row in board:
            row = row.split()
            new_row = []
            for item in row:
                if item == num:
                    new_row.append('X')
                else:
                    new_row.append(item)
            row = ' '.join(new_row)
            new_board.append(row)
        new_boards[idx] = new_board
        # print(new_boards)
    return new_boards


def is_winning_row(row):
    # print(row)
    count = 0
    for item in row:
        if item == 'X':
            count += 1
    if count == 5:
        # print(row)
        return True
    return False


def is_winning_col(board, index):
    column = []
    for item in board:
        y = list(itertools.islice(item, index, index+1))
        column += y
    column = " ".join(column)
    return is_winning_row(column)

def print_board(board):
    for row in board:
        print(' '.join(str(col if col else 'x') for col in row))

def winner_borad(board):
    for row in board:
        if is_winning_row(row):
            return True
    for idx in range(5):
        if is_winning_col(board, idx):
            return True
    return False


def get_sum_of_all_unmarked_numbers(board):
    counter = 0
    print(board)
    for row in board:
        row = row.split()
        for item in row:
            if item != 'X':
                counter += int(item)
    print(counter)
    return counter


def is_bingo(board):
    if winner_borad(board):
        return True
    return False


def replace_and_check(numbers, boards):
    idx = 0
    got_bingo = False
    result = 0
    while idx < len(numbers) and not got_bingo:
        num = numbers[idx]
        boards = replace_num_in_boards(num, boards)
        for _, board in boards.items():
            if is_bingo(board):
                print_board(board)
                got_bingo = True
                print(num)
                result = get_sum_of_all_unmarked_numbers(board)
        idx += 1
        # print(num)
        result = int(num) * result
    return result


def get_score(data):
    numbers = data[0].split(',')
    # print(numbers)
    boards = get_boards(data[2:])
    # print(boards)
    return replace_and_check(numbers, boards)


# data = get_input('resources/day4_input.txt')
# data = get_input('resources/day4_test.txt')
data = get_input('resources/day4_test2.txt')
# # print("data: ", data)
print(get_score(data))
