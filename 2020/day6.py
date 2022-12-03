def get_input(path):
    with open(path, 'r') as fh:
        return fh.read().splitlines()


def get_answer_map_per_person(line):
    letters_map = dict()
    for letter in line:
        letters_map[letter] = line.count(letter)
    # print(letters_map)
    return letters_map


_file = 'resources/day6_input.txt'
data = get_input(_file)
group_map = {}
group_index = 1
answers_per_group = 0
overall_map = {}
total_count = 0
for item in data:
    if len(item) == 0:
        group_index += 1
        answers_per_group = 0
        group_map = {}
    else:
        person_answers = get_answer_map_per_person(item)
        for k,v in person_answers.items():
            group_map[k] = v
    overall_map[group_index] = len(group_map.keys())
for k,v in overall_map.items():
    total_count += v
print("Day 6 - Part I:", total_count)