with open('day03.txt') as f:
    data = [line.strip() for line in f]

def part1():
    ones = zeroes = idx = 0
    gamma = ''
    while (idx < len(data[0])):
        for i in data:
            if i[idx] == '0':
                zeroes += 1
            else:
                ones += 1
        if (ones > zeroes):
            gamma += '1'
        else:
            gamma += '0'
        ones = zeroes = 0
        idx += 1

    return (gamma, int(gamma, 2) * ( int(gamma,2) ^ 4095))

def get_most(data, idx):
    ones = zeroes = 0
    for i in data:
        if i[idx] == '1':
            ones += 1
        else:
            zeroes += 1
    if ones < zeroes:
        return '0'
    return '1'

def get_least(data, idx):
    ones = zeroes = 0
    for i in data:
        if i[idx] == '1':
            ones += 1
        else:
            zeroes += 1
    if ones < zeroes:
        return '1'
    return '0'

def part2():
    o2_generator = data.copy()
    co2_generator = data.copy()
    idx = 0
    while (idx < len(data[0])) and (len(o2_generator) > 1):
        keepers = get_most(o2_generator, idx)
        o2_generator = [ i for i in o2_generator if i[idx] == keepers ]
        idx += 1

    idx = 0
    while (idx < len(data[0])) and (len(co2_generator) > 1):
        keepers = get_least(co2_generator, idx)
        co2_generator = [ i for i in co2_generator if i[idx] == keepers ]
        idx += 1
    return (o2_generator, co2_generator, int(o2_generator[0], 2) * int(co2_generator[0], 2))



if __name__ == '__main__':
    gamma, pt1 = part1()
    o2, co2, pt2 = part2()
    print(gamma, pt1)
    print(o2, co2, pt2)
