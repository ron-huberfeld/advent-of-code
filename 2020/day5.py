def get_tickets(path):
    with open(path, 'r') as fh:
        yield fh.read().splitlines()


def get_new_range(_min, _max, value):
    # print(_min, _max, value)
    if value == 'F' or value == 'L':
        mid = _min + (_max - _min) // 2
        return (_min, mid)
    if value == 'B' or value == 'R':
        mid = _min + (_max - _min) // 2 + 1
        return (mid, _max)
    print("something is wrong")


def get_id(ticket):
    # print(ticket)
    range_min = 0
    range_max = 127
    tpl = (0, 127)
    for item in ticket[0:7]:
        tpl = get_new_range(range_min, range_max, item)
        range_min, range_max = tpl
    row = tpl[0]

    range_min = 0
    range_max = 7
    tpl = (0, 7)
    for item in ticket[-3:]:
        tpl = get_new_range(range_min, range_max, item)
        range_min, range_max = tpl
    column = tpl[0]
    return row * 8 + column


_file = 'resources/day5_input.txt'
_id = 0
ids = []
for tickets in get_tickets(_file):
    for ticket in tickets:
        ticket_id = get_id(ticket)
        ids.append(ticket_id)
        if ticket_id > _id:
            _id = ticket_id
print("Day 5 - part I:", _id)
# print(ids)
for i in range(_id):
    if i not in ids and i-1 in ids and i+1 in ids:
        print("Day 5 - part II:", i)