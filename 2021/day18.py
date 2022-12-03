def get_input(path):
    with open(path, 'r') as fh:
        return fh.read().splitlines()


def get_addition_of_two(a, b):
    print("a:", a)
    print("b:", b)
    arr = [a,b]
    return arr


def get_result(data):
    result = get_addition_of_two(data[0], data[1])
    return result


# data = get_input('resources/day18_input.txt')
data = get_input('resources/day18_test.txt')
print("data: ", data)
print(get_result(data))
