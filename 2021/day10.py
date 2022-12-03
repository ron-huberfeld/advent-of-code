from collections import deque

PAIRING = dict(zip('({[<', ')}]>'))
ERROR = dict(zip(')]}>', (3, 57, 1197, 25137)))
COMP = dict(zip(')]}>', (1, 2, 3, 4)))


def get_input(path):
    with open(path, 'r') as fh:
        return fh.read().splitlines()


def get_first_invalid(line):
    stack = deque()
    for c in line:
        if c in '[{<(':
            stack.append(c)
            # print(stack)
        if c in ']}>)' and len(stack) > 0 and not PAIRING[stack.pop()] == c:
            return c


def get_first_wrong_list(data):
    new_data = []
    for line in data:
        res = get_first_invalid(line)
        if res is not None:
            new_data.append(res)
    return new_data


def get_points(item, count):
    return count * ERROR[item]


def get_result(data):
    arr = get_first_wrong_list(data)
    total_points = 0
    for item in ERROR.keys():
        total_points += get_points(item, arr.count(item))
    return total_points


def get_completing_sequence_2(line):
    x = []
    stack = deque()
    for c in line:
        if c in '[{<(':
            stack.append(c)
            # print(stack)
        if c in ']}>)' and len(stack) > 0:
            stack.pop()
    # print(stack)
    for item in stack:
        x.append(PAIRING[item])
    return x


def get_completing_sequence(data):
    new_data = deque()
    for line in data:
        if get_first_invalid(line) is None:
            com_seq = get_completing_sequence_2(line)
            # print(com_seq)
            new_data.append(com_seq)
    return new_data



def get_result_2(data):
    tot_poi_arr = []
    arr = get_completing_sequence(data)
    for seq in arr:
        total_points = 0
        while(len(seq) > 0):
            value = seq.pop()
            total_points = 5 * total_points + COMP[value]
        # print(total_points)
        tot_poi_arr.append(total_points)
    y = sorted(tot_poi_arr)
    # print(y)
    return y[len(y)//2]


data = get_input('resources/day10_input.txt')
# data = get_input('resources/day10_test.txt')
# print("data: ", data)
print("Day 10 - part I:", get_result(data))
print("Day 10 - part II:", get_result_2(data))
