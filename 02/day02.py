with open('day02.txt') as f:
    data = [line.strip().split() for line in f]


test = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''
t = [i.split() for i in test.split('\n')]

def part1(data):
    depth = pos = 0
    for i in data:
        if i[0] == 'up':
            depth -= int(i[1])
        elif i[0] == 'down':
            depth += int(i[1])
        elif i[0] == 'forward':
            pos += int(i[1])
    return depth * pos

print(f'Test1: {part1(t)}')
print(f'Part1: {part1(data)}')

def part2(data):
    depth = pos = aim = 0
    for i in data:
        if i[0] == 'up':
            aim -= int(i[1])
        elif i[0] == 'down':
            aim += int(i[1])
        elif i[0] == 'forward':
            pos += int(i[1])
            depth += aim * int(i[1])
    return depth * pos

print(f'Test2: {part2(t)}')
print(f'Part2: {part2(data)}')
