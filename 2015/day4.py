import hashlib


def get_input(path):
    with open(path, 'r') as fh:
        return fh.read()


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


data = get_input('resources/day4_input.txt')
# print("data: ", data)
for i in infinite_sequence():
    str2hash = data + str(i)
    # print(str2hash)
    result = hashlib.md5(str2hash.encode())
    hex_res = result.hexdigest()
    if (hex_res.startswith('00000')):
        print("Day 4 - part I: ", i)
        break
data = get_input('resources/day4_input.txt')
for i in infinite_sequence():
    str2hash = data + str(i)
    # print(str2hash)
    result = hashlib.md5(str2hash.encode())
    hex_res = result.hexdigest()
    if (hex_res.startswith('000000')):
        print("Day 4 - part II: ", i)
        break
