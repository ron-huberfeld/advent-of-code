def get_input(path):
    with open(path, 'r') as fh:
        return fh.read()


data = get_input('day1_input.txt')
counter = 0
for item in data:
    if item == '(':
        counter += 1
    if item == ')':
        counter -= 1

print("Day 1 - part I: ", counter)  # output 138
position = 0
counter = 0
while position < len(data) and counter != -1:
    if data[position] == '(':
        counter += 1
    if data[position] == ')':
        counter -= 1
    position += 1
print("Day 1 - part II: ", position)  # output 1771