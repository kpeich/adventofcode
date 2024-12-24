import optparse
from copy import deepcopy

def get_path(loc, direction, grid, dbg=False):
    move = ((-1,0), (0,1), (1,0), (0,-1)) # nsew movements
    path = [(loc,direction)]
    count = 0
    while True:
        if (count % 100 == 0) and (count != 0):
            print(f'WARN: LOOP HAS RUN {count} TIMES')
        ahead = tuple(sum(x) for x in zip(loc,move[direction]))
        if (0<=ahead[0]<=len(grid)-1) and (0<=ahead[1]<=len(grid[0])-1) and (grid[ahead[0]][ahead[1]] not in ['#','X']):
            if (ahead,direction) in path:
                if dbg:
                    print(f'LOOP FOUND at {loc} {direction}')
                return path, True
            path.append((ahead,direction))
            loc = ahead
        elif (0 > ahead[0]) or (ahead[0] > len(grid)-1) or (0 > ahead[1]) or (ahead[1] > len(grid[0])-1):
            if dbg:
                print(f'Guard Left the World at {loc} {direction}')
            return path, False
        elif grid[ahead[0]][ahead[1]] in ['#', 'X']:
            direction = (direction + 1) % 4
        else:
            print('SOMETHING WENT WRONG')
            return path, False

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        grid = [[i for i in line.strip()] for line in f]

    for row_idx, row in enumerate(grid):
        if '^' in row:
            loc,direction = (row_idx, row.index('^')), 0 # start facing nsew:0123

    if options.dbg:
        pass

    path, looping = get_path(loc, direction, grid, dbg=options.dbg)
    if options.dbg:
        print(path)
    print(f"Part1: {len(set([i[0] for i in path]))}")

    obstructions = []
    count = 0
    previous = tuple()
    for place in set([i[0] for i in path[1:]]):
        if (count % 100 == 0):
            print(f"CHECKING PLACE {count}/{len(set([i[0] for i in path[1:]]))}")
        direction = 0
        if options.dbg:
            print(f'Place Block at {place}')
        new_grid = deepcopy(grid)
        new_grid[place[0]][place[1]] = 'X'
        this_path, looping = get_path(loc, direction, new_grid, dbg=options.dbg)
        if looping:
            obstructions.append(place)
        count += 1
    print(f"Part2: {len(obstructions)}")
