from collections import defaultdict

with open('day05.txt') as f:
    data = [line.strip().split(' -> ') for line in f]
    vents = [[tuple(int(x) for x in coords[0].split(',')), tuple(int(x) for x in coords[1].split(','))] for coords in data]

def basis_vents(vents):
    return [vent for vent in vents if (vent[0][0] == vent[1][0]) or (vent[0][1] == vent[1][1])]

def vent_layout(vents):
    basis = basis_vents(vents)
    overlap = defaultdict(int)
    for line in basis:
        (x0, y0), (x1, y1) = line
        if x0 == x1:
            start = min(y0, y1)
            stop = max(y0, y1)
            for y in range(start, stop+1):
                overlap[(x0,y)] += 1 
        else:
            start = min(x0, x1)
            stop = max(x0, x1)
            for x in range(start, stop+1):
                overlap[(x, y0)] += 1 
    return overlap

def part1(vents):
    count = 0
    for key,value in vent_layout(vents).items():
        if value > 1:
            count += 1
    return count

def get_diagonal(vents):
    return [vent for vent in vents if (vent[0][0] != vent[1][0]) and (abs(((vent[1][1] - vent[0][1]) / (vent[1][0] - vent[0][0]))) == 1)]

def get_diagonal2(vents):
    return [vent for vent in vents if (vent[0][0] != vent[1][0]) and (vent[0][1] != vent[1][1])]

def vent_layout_with_diagonal(vents):
    overlap = vent_layout(vents)
    diagonal = get_diagonal(vents)
    for line in diagonal:
        (x0 , y0), (x1, y1) = line
        slope = (y1 - y0) / (x1 - x0)
        y_current = y0 if (min(x0, x1) == x0) else y1
        x_start = min(x0, x1)
        x_stop = max(x0, x1)
        for x in range(x_start, x_stop+1):
            overlap[(x, y_current)] += 1 
            y_current += int(slope)
    return overlap


def part2(vents):
    count = 0
    for key,value in vent_layout_with_diagonal(vents).items():
        if value > 1:
            count += 1
    return count

print(f'Part1: {part1(vents)}')
print(f'Part2: {part2(vents)}')
