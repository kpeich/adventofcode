with open('day09.txt') as f:
    data = [line.strip() for line in f]
    heightmap = [[int(i) for i in list(line)] for line in data]

test = '''2199943210
3987894921
9856789892
8767896789
9899965678'''

t = [[int(i) for i in list(line)] for line in test.split('\n')]

def get_lowpoints(heightmap):
    last_row = len(heightmap) - 1
    last_col = len(heightmap[0]) - 1
    lowpoints = []
    for r_idx, row in enumerate(heightmap):
        for c_idx, loc in enumerate(row):
            if r_idx not in (0,last_row) and c_idx not in (0,last_col):
                left = heightmap[r_idx][c_idx+1]
                right = heightmap[r_idx][c_idx-1]
                above = heightmap[r_idx-1][c_idx]
                below = heightmap[r_idx+1][c_idx]
                if loc < min(left, right, above, below):
                    lowpoints.append((r_idx, c_idx))
            elif r_idx == 0 and c_idx not in (0, last_col):
                left = heightmap[r_idx][c_idx+1]
                right = heightmap[r_idx][c_idx-1]
                below = heightmap[r_idx+1][c_idx]
                if loc < min(left, right, below):
                    lowpoints.append((r_idx, c_idx))
            elif r_idx == last_row and c_idx not in (0, last_col):
                left = heightmap[r_idx][c_idx+1]
                right = heightmap[r_idx][c_idx-1]
                above = heightmap[r_idx-1][c_idx]
                if loc < min(left, right, above):
                    lowpoints.append((r_idx, c_idx))
            elif c_idx == 0 and r_idx not in (0, last_row):
                right = heightmap[r_idx][c_idx+1]
                above = heightmap[r_idx-1][c_idx]
                below = heightmap[r_idx+1][c_idx]
                if loc < min(right, above, below):
                    lowpoints.append((r_idx, c_idx))
            elif c_idx == last_col and r_idx not in (0, last_row):
                left = heightmap[r_idx][c_idx-1]
                above = heightmap[r_idx-1][c_idx]
                below = heightmap[r_idx+1][c_idx]
                if loc < min(left, above, below):
                    lowpoints.append((r_idx, c_idx))
            elif r_idx == 0:
                if c_idx == 0:
                    right = heightmap[r_idx][c_idx+1]
                    below = heightmap[r_idx+1][c_idx]
                    if loc < min(right, below):
                        lowpoints.append((r_idx, c_idx))
                else:
                    left = heightmap[r_idx][c_idx-1]
                    below = heightmap[r_idx+1][c_idx]
                    if loc < min(left, below):
                        lowpoints.append((r_idx, c_idx))
            elif r_idx == last_row:
                if c_idx == 0:
                    right = heightmap[r_idx][c_idx+1]
                    above = heightmap[r_idx-1][c_idx]
                    if loc < min(right, above):
                        lowpoints.append((r_idx, c_idx))
                else:
                    left = heightmap[r_idx][c_idx-1]
                    above = heightmap[r_idx-1][c_idx]
                    if loc < min(left, below):
                        lowpoints.append((r_idx, c_idx))
    return lowpoints

def part1(heightmap):
    coords = get_lowpoints(heightmap)
    return sum([heightmap[loc[0]][loc[1]] + 1  for loc in coords])

print(f'Test1: {get_lowpoints(t)} Sum: {part1(t)}')
print(f'Part1: {part1(heightmap)}')

simplified = [[1 if loc != 9 else loc for loc in row] for row in heightmap]
[print(i) for i in simplified]
