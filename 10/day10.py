import optparse

def get_possible_moves(loc, grid):
    row, col = loc
    grid_size = len(grid) - 1
    adjacent_cells = [(row+1,col), (row-1,col), (row,col+1), (row, col-1)]

    return [(x,y) for x,y in adjacent_cells if (0<=x<=grid_size and 0<=y<=grid_size) and (grid[x][y] == grid[row][col]+1)]

def find_paths(loc, grid):
    queue = [loc]
    peaks = []

    while queue:
        x,y = queue.pop()
        if grid[x][y] == 9:
            peaks.append((x,y))
        else:
            queue.extend([i for i in get_possible_moves((x,y), grid)])

    return len(set(peaks)), peaks

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        topography = [[int(i) for i in line.strip()] for line in f]

    if options.dbg:
        pass

    part1 = []
    for rdx, row in enumerate(topography):
        for cdx,col in enumerate(row):
            if col == 0:
                part1.append(find_paths((rdx,cdx),topography))
    print(f"Part1: {sum([i[0] for i in part1])}")
    print(f"Part2: {sum([len(i[1]) for i in part1])}")
