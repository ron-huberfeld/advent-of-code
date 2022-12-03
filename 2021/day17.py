def get_input(path):
    with open(path, 'r') as fh:
        return fh.read()


def parse_data(data):
    x1 = int(data.split('=')[1:][0].split('..')[0])
    x2 = int(data.split('=')[1:][0].split('..')[1].split(',')[0])
    y1 = int(data.split('=')[1:][1].split('..')[0])
    y2 = int(data.split('=')[1:][1].split('..')[1])
    a = (x1, y2)
    b = (x2, y1)
    return (a, b)


def get_drag_and_gravity(tpl):
    x, y = tpl
    if x > 0:
        x -= 1
    elif x < 0:
        x += 1
    return (x, y - 1)


def is_valid(dst, area):
    # print(dst, area)
    if dst[0] <= area[1][0] and dst[1] >= area[1][1]:
        return True
    return False


def get_probe_moves(current_position, velocity, moves, area):
    dst = tuple(map(sum, zip(current_position, velocity)))
    if(not is_valid(dst, area)):
        return moves
    velocity = get_drag_and_gravity(velocity)
    moves.append(dst)
    return get_probe_moves(dst, velocity, moves, area)


def get_probe_route(velocity, target_area):
    # print(velocity, target_area)
    init = (0, 0)
    probe_moves = []
    probe_moves = get_probe_moves(
        init, velocity, probe_moves, target_area)
    # print(probe_moves)
    return probe_moves


def is_valid_location(point, target_area):
    # print(point, target_area)
    x, y = point
    a, b = target_area
    x1, y1 = a
    x2, y2 = b
    # print(x1, x, x2, y1, y, y2)
    if x1 <= x and x <= x2 and y1 >= y and y >= y2:
        return True
    return False


def is_valid_route(moves, target_area):
    index = 0
    while (index < len(moves)):
        if is_valid_location(moves[index], target_area):
            return True
        index += 1
    return False


def get_highest_point(data):
    target_area = parse_data(data)
    highest = 0
    tar_range = target_area[1]
    for i in range(1, tar_range[0]):
        for j in range(300, tar_range[1], -1):
            moves = get_probe_route((i, j), target_area)
            if is_valid_route(moves, target_area):
                maxi = max(moves, key=lambda x: x[1])[1]
                if maxi > highest:
                    highest = maxi
    return highest


def get_diff_init_velocity(data):
    target_area = parse_data(data)
    velocity_counter = 0
    tar_range = target_area[1]
    for i in range(1, tar_range[0] + 1):
        for j in range(300, tar_range[1] -1, -1):
            moves = get_probe_route((i, j), target_area)
            if is_valid_route(moves, target_area):
                velocity_counter += 1
    return velocity_counter


data = get_input('resources/day17_input.txt')
# data = get_input('resources/day17_test.txt')
print("data: ", data)
print(get_highest_point(data))
print(get_diff_init_velocity(data))
