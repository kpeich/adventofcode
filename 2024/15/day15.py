import optparse
from copy import deepcopy

def move(obj, loc, direction, grid, dbg=False):
    moves = { '^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1) }
    row,col = loc
    dr,dc = moves[direction]

    if grid[row+dr][col+dc] == '.':
        grid[row][col] = '.'
        grid[row+dr][col+dc] = obj
        return (row+dr,col+dc), grid
    elif grid[row+dr][col+dc] in 'O[]':
        queue = [(obj,loc),(grid[row+dr][col+dc],(row+dr,col+dc))]
        while queue:
            if dbg:
                [print(''.join(i)) for i in grid]
            tobj,tloc = queue.pop()
            if dbg:
                print(f"TRY MOVE {tobj} AT {tloc}")
            moved, grid = move(tobj,tloc,direction,grid)
            if moved == tloc:
                return loc, grid
        return moved, grid
    elif grid[row+dr][col+dc] == '#':
        return loc, grid
    else:
        if dbg:
            print("SOMETHING WENT WRONG?")
        return loc, grid

def get_gps(grid, marker='O'):
    return sum([sum([rdx*100+cdx for cdx,col in enumerate(row) if col == marker]) for rdx,row in enumerate(grid)])

def doublewide(grid):
    doublewide = []
    for rdx,row in enumerate(grid):
        doublewide.append([])
        for col in row:
            if col == '#':
                doublewide[rdx] += ['#','#']
            elif col == 'O':
                doublewide[rdx] += ['[',']']
            elif col == '.':
                doublewide[rdx] += ['.','.']
            elif col == '@':
                doublewide[rdx] += ['@','.']
    return doublewide

def move2(obj, loc, direction, grid, dbg=False):
    moves = { '^':(-1,0), 'v':(1,0) }
    row,col = loc
    dr,dc = moves[direction]
    tgrid = deepcopy(grid)

    if grid[row+dr][col+dc] == '.':
        if dbg:
            print(f"{obj} at {loc} free to move")
        grid[row][col] = '.'
        grid[row+dr][col+dc] = obj
        return (row+dr,col+dc), grid
    elif grid[row+dr][col+dc] in '[]':
        box = { '[': 1, ']': -1}
        dc = box[grid[row+dr][col+dc]] # if [ need to also check col+1, if ] need to check col-1

        queue = [(obj,loc),(grid[row+dr][col],(row+dr,col)),(grid[row+dr][col+dc],(row+dr,col+dc))]
        while queue:
            if dbg:
                [print(''.join(i)) for i in grid]
            tobj, tloc = queue.pop()
            if dbg:
                print(f"TRY MOVE {obj} at {loc}")
            moved, grid = move2(tobj, tloc, direction, grid)
            if moved == tloc:
                if dbg:
                    print(f"{tobj} AT {tloc} DIDN'T MOVE")
                return loc, tgrid
        return moved, grid
    
    elif grid[row+dr][col+dc] == '#':
        return loc, grid
    else:
        if dbg:
            print(f"SOMETHING WENT WRONG? {grid[row+dr][col+dc]} {obj} {loc} {direction}")
        return loc, grid


if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        loc = None
        grid = []
        movement = ''
        for idx,line in enumerate(f):
            if line[0] == '#':
                grid.append([cell for cell in line.strip()])
            if line[0] in '^v<>':
                movement = movement + line.strip()
            if '@' in line:
                loc = (idx,line.index('@'))
    grid2 = doublewide(grid)
    loc2 = (loc[0],loc[1]*2)

    if options.dbg:
        [print(i) for i in grid]
        print(loc)
        print(movement)

    for direction in movement:
        if options.dbg:
            print(f"MOVE {loc}: {direction}")
        loc, grid = move('@',loc,direction,grid, dbg=options.dbg)
        if options.dbg:
            [print(''.join(row)) for row in grid]
            print()

    part1 = get_gps(grid)
    print(f"Part1: {part1}")

    if options.dbg:
        [print(i) for i in grid2]
        print(loc2)
        print(movement)
    for step,direction in enumerate(movement):
        if options.dbg:
            print(f"{step} MOVE {loc2}: {direction}")

        if direction in '<>':
            loc2, grid2 = move('@',loc2,direction,grid2, dbg=options.dbg)
        elif direction in '^v':
            loc2, grid2 = move2('@',loc2,direction,grid2, dbg=options.dbg)

        if options.dbg:
            [print(''.join(row)) for row in grid2]
            print()
            
    part2 = get_gps(grid2,marker='[')
    print(f"Part2: {part2}")
