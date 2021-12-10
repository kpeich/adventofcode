from statistics import median

with open('day07.txt') as f:
    data = [line.strip() for line in f]
    pos = [int(i) for i in data[0].split(',')]

test = [16,1,2,0,4,2,7,1,2,14]

def get_fuel(data):
    middle = median(data)
    return sum([abs(i-middle) for i in data])

print(f'Test1: {get_fuel(test)}')
print(f'Part1: {get_fuel(pos)}')

def get_fuel2(align, data):
    return sum([((i-align)**2 + abs(i-align))/2 for i in data])

def part2(data):
    align = median(data)
    fuel = get_fuel2(align, data)
    fuel_left = get_fuel2(align-1, data)
    fuel_right = get_fuel2(align+1, data)
    if (fuel_left < fuel):
        while (fuel_left < fuel):
            align -= 1
            fuel = fuel_left
            fuel_left = get_fuel2(align-1, data)
    elif (fuel_right < fuel):
        while (fuel_right < fuel):
            align += 1
            fuel = fuel_right
            fuel_right = get_fuel2(align+1, data)
    return fuel

print(f'Test2: {part2(test)}')
print(f'Part2: {part2(pos)}')
