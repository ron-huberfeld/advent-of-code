def get_input(path):
    with open(path, 'r') as fh:
        return fh.read().splitlines()


def get_surface_area(a, b, c):
    return 2*a*b + 2*b*c + 2*a*c


def get_slack(a, b):
    return a*b


def get_ribbon(a, b):
    return a+a+b+b


def get_bow(a, b, c):
    return a*b*c


data = get_input('resources/day2_input.txt')
total_paper = 0
total_ribbon = 0
for item in data:
    (a, b, c) = item.split('x')
    numbers = [int(a), int(b), int(c)]
    min1 = min(numbers)
    numbers.remove(min1)
    min2 = min(numbers)
    # print("minimum: ", min1, min2)
    paper = get_surface_area(int(a), int(b), int(c)) + get_slack(min1, min2)
    # print(paper)
    ribbon = get_ribbon(min1, min2) + get_bow(int(a), int(b), int(c))
    # print(ribbon)
    total_paper += paper
    total_ribbon += ribbon
print("Day 2 - part I: ", total_paper)
print("Day 2 - part II: ", total_ribbon)
