import optparse

def move(obj, loc, direction, grid, dbg=False):
    moves = { '^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1) }
    row,col = loc
    dr,dc = moves[direction]

    if grid[row+dr][col+dc] == '.':
        grid[row][col] = '.'
        grid[row+dr][col+dc] = obj
        return (row+dr,col+dc), grid
    elif grid[row+dr][col+dc] == 'O':
        queue = [(obj,loc),('O',(row+dr,col+dc))]
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

def get_gps(grid):
    return sum([sum([rdx*100+cdx for cdx,col in enumerate(row) if col == 'O']) for rdx,row in enumerate(grid)])

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        start = None
        grid = []
        movement = ''
        for idx,line in enumerate(f):
            if line[0] == '#':
                grid.append([cell for cell in line.strip()])
            if line[0] in '^v<>':
                movement = movement + line.strip()
            if '@' in line:
                loc = (idx,line.index('@'))

    if options.dbg:
        [print(i) for i in grid]
        print(start)
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
