from re import match


def get_data_from_file(path):
    with open(path, 'r') as fh:
        return fh.read().splitlines()


def is_valid_byr(v):
    return 1920 <= int(v) <= 2002


def is_valid_iyr(v):
    return 2010 <= int(v) <= 2020


def is_valid_eyr(v):
    return 2020 <= int(v) <= 2030


def is_valid_hgt(v):
    if 'cm' in v:
        val = v.strip('cm')
        if 150 <= int(val) <= 193:
            return True
    if 'in' in v:
        val = v.strip('in')
        if 59 <= int(val) <= 76:
            return True
    return False


def is_valid_hcl(v):
    return bool(match(r'^#[0-9a-f]{6}', v))


def is_valid_ecl(v):
    return bool(match(r'amb|blu|gry|brn|grn|hzl|oth', v))


def is_valid_pid(v):
    return bool(match(r'^\d{9}$', v))


def is_valid(passports):
    keys = passports.keys()
    if 'byr' in keys and 'iyr' in keys and 'eyr' in keys and 'hgt' in keys \
            and 'hcl' in keys and 'ecl' in keys and 'pid' in keys:
        bo = True
        for k, v in passports.items():
            if k == 'byr':
                bo = is_valid_byr(v)
            elif k == 'iyr':
                bo = is_valid_iyr(v)
            elif k == 'eyr':
                bo = is_valid_eyr(v)
            elif k == 'hgt':
                bo = is_valid_hgt(v)
            elif k == 'hcl':
                bo = is_valid_hcl(v)
            elif k == 'ecl':
                bo = is_valid_ecl(v)
            elif k == 'pid':
                bo = is_valid_pid(v)
            if not bo:
                return False
        return bo
    return False


def is_valid_part_one(passports):
    keys = passports.keys()
    if 'byr' in keys and 'iyr' in keys and 'eyr' in keys and 'hgt' in keys \
            and 'hcl' in keys and 'ecl' in keys and 'pid' in keys:
        return True
    return False


def get_valid_passports_count_part_1(data):
    ids = {}
    counter = 0
    for item in data:
        if item != "":
            fields = item.split()
            for field in fields:
                key, value = field.split(':')
                ids[key] = value
        else:
            if is_valid_part_one(ids):
                counter += 1
            ids = {}
    if is_valid_part_one(ids):
        counter += 1
    return counter


def get_valid_passports_count(data):
    ids = {}
    counter = 0
    for item in data:
        if item != "":
            fields = item.split()
            for field in fields:
                key, value = field.split(':')
                ids[key] = value
        else:
            if is_valid(ids):
                counter += 1
            ids = {}
    if is_valid(ids):
        counter += 1
    return counter


# _file = 'resources/day4_test3.txt'
_file = 'resources/day4_input.txt'
data = get_data_from_file(_file)
# print(data)
print("Day 4 - Part I:", get_valid_passports_count_part_1(data))
print("Day 4 - Part II:", get_valid_passports_count(data))
