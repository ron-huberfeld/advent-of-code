DIRECTIONS = dict(zip(('forward', 'down', 'up'),
                      ((1, 0), (0, 1), (0, -1))))


def get_input(path):
    with open(path, 'r') as fh:
        return fh.read().splitlines()


def get_result(data, is_second_part):
    src = (0, 0)
    aim = 0
    depth = 0
    for item in data:
        (direction, steps) = tuple(item.split(' '))
        step = DIRECTIONS[direction]
        for _ in range(int(steps)):
            src = tuple(map(sum, zip(src, step)))
        if is_second_part:
            if direction != 'forward':
                aim = src[1]
            else:
                depth += int(steps) * aim
        else:
            depth = src[1]
    return src[0] * depth


data = get_input('resources/day2_input.txt')
# data = get_input('resources/day2_test.txt')
# print("data: ", data)
print("Day2 - part I:", get_result(data, False))
print("Day2 - part II:", get_result(data, True))
