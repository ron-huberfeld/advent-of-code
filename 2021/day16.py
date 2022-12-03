import itertools


def get_input(path):
    with open(path, 'r') as fh:
        return fh.read()


def get_hex_from_binary(data):
    # convert binary to int
    num = int(data, 2)
    # convert int to hexadecimal
    # hex_num = hex(num)
    hex_num = format(num, 'x')
    return(hex_num)


def get_header(data):
    version = get_hex_from_binary(data[0:3])
    type_id = get_hex_from_binary(data[3:6])
    return (version, type_id)


def get_binary_data(data):
    scale = 16
    num_of_bits = 4
    return bin(int(data, scale))[2:].zfill(num_of_bits)


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(itertools.islice(iterable, n))


def binary_to_decimal(binary):
    binary1 = int(binary)
    decimal, i, n = 0, 0, 0
    while(binary1 != 0):
        dec = binary1 % 10
        decimal = decimal + dec * pow(2, i)
        binary1 = binary1//10
        i += 1
    return(decimal)


def handle_literal_value(data):
    print(data)
    new_data = []
    while(len(data) > 5 and int(data[0]) == 1):
        new_data.append(data[1:5])
        data = data[5:]
        if len(data) > 5 and int(data[0]) == 0:
            new_data.append(data[1:5])
    value = binary_to_decimal(''.join(new_data))
    return value


def handle_operator_packet(data):
    return 1


def get_version_sum(data):
    version_sum = []
    b_data = get_binary_data(data)
    print(b_data)
    header_version_and_type = get_header(b_data)
    print(header_version_and_type)
    version_sum.append(int(header_version_and_type[0]))
    if int(header_version_and_type[1]) == 4:
        literal_value = handle_literal_value(b_data[6::])
        print(literal_value)
    else:
        operator_packet = handle_operator_packet(b_data[6::])
        print(operator_packet)
    return version_sum


# data = get_input('resources/day16_input.txt')
data = get_input('resources/day16_test.txt')
print("data: ", data)
print(get_version_sum(data))
