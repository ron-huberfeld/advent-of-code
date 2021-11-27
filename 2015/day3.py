DIRECTIONS = dict(zip('>^<v', ((1, 0), (0, 1), (-1, 0), (0, -1))))


def get_input(path):
    with open(path, 'r') as fh:
        yield from fh.read()


# print("map: ", DIRECTIONS)
data = get_input('resources/day3_input.txt')
# print("data: ", data)
src = (0, 0)
points = {(0, 0)}
for item in data:
    # print(item)
    step = DIRECTIONS[item]
    # print(src, step)
    dst = tuple(map(sum, zip(src, step)))
    # print(dst)
    points.add(dst)
    src = dst
    # print(points)
print("Day3 - part I: ", len(points))

data = get_input('resources/day3_input.txt')
src1 = (0, 0)
src2 = (0, 0)
points = {(0, 0)}
count = 1
for item in data:
    step = DIRECTIONS[item]
    dst1 = tuple(map(sum, zip(src1, step)))
    dst2 = tuple(map(sum, zip(src2, step)))
    if (count % 2) == 0:
        points.add(dst1)
        src1 = dst1
    else:
        points.add(dst2)
        src2 = dst2
    # print(points)
    count += 1
print("Day3 - part II: ", len(points))
