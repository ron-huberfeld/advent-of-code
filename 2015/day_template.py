def get_input(path):
    with open(path, 'r') as fh:
        return fh.read().splitlines()


data = get_input('resources/day_X_input.txt')
print("data: ", data)
