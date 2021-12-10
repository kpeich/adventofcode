with open('day01.txt') as f:
    data = [int(line.strip()) for line in f]

test = [199,200,208,210,200,207,240,269,260,263]

def part1(data):
    return sum([1 for i in range(1,len(data)) if data[i] > data[i-1]])

print(f'Test1: {part1(test)}')
print(f'Part1: {part1(data)}')

def part2(data):
    return sum([1 for i in range(3,len(data)) if data[i] > data[i-3]])

print(f'Test2: {part2(test)}')
print(f'Part2: {part2(data)}')

