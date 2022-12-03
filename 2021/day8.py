import itertools


NUMBERS = dict(zip('1478', '2347'))


def get_input(path):
    with open(path, 'r') as fh:
        return fh.read().splitlines()


def parse(data, is_test):
    if is_test:
        return [line for idx, line in enumerate(data) if idx % 2 != 0]
    return [line.split('|')[1] for line in data]


def get_result(data, is_test):
    counter = 0
    data = parse(data, is_test)
    for line in data:
        digits = line.split()
        for dig in digits:
            if str(len(dig)) in NUMBERS.values():
                counter += 1
    return counter


def get_word_count(digits):
    print(digits)
    w = []
    for word in digits:
        if len(word) == 7:
            w.append('8')
        elif len(word) == 6:
            if 'f' not in word:
                w.append('0')
            elif 'g' not in word:
                w.append('9')
            elif 'a' not in word:
                w.append('6')
        elif len(word) == 5:
            if 'g' not in word and 'a' not in word:
                w.append('5')
            elif 'b' not in word and 'e' not in word:
                w.append('2')
            elif 'e' not in word and 'g' not in word:
                w.append('3')
        elif len(word) == 4:
            w.append('4')
        elif len(word) == 3:
            w.append('7')
        elif len(word) == 2:
            w.append('1')
    # print(w)
    return w


def get_result_part_two(data, is_test):
    counter = 0
    print(data)
    data = parse(data, is_test)
    for line in data:
        # print(line)
        digits = line.rstrip().split()
        num = get_word_count(digits)
        print(num)
        # counter += int(num)
    return counter


data1 = get_input('resources/day8_input.txt')
data2 = get_input('resources/day8_test.txt')
# print("data: ", data)
# print(get_result(data2, True))
# print("Day8 - part I:", get_result(data1, False))
print(get_result_part_two(data2, True))
# print("Day8 - part II:", get_result_part_two(data1, False))
