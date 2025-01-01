import optparse

def get_possible_moves(loc, grid_size):
    '''
    loc is tupe of (row, col)
    grid_size size of square grid

    returns list of possible (row, col) locations to move to
    '''
    row, col = loc
    adjacent_cells = [(row+1,col), (row-1,col), (row,col+1), (row, col-1)]

    return [(row,col) for row,col in adjacent_cells if ( (0<=row<=grid_size and 0<=col<=grid_size) and (grid[row][col] != '#') )]

def bfs(grid, dbg=False):
    # BFS
    #queue = [((0,0),0)]
    queue = [((0,0),[])]
    visited = set()
    found = []

    while queue:
        loc, path = queue.pop(0)
        if (loc != (len(grid[0])-1, len(grid[0])-1)):
            if dbg:
                print(loc, visited)
            if loc in visited:
                continue
            else:
                queue.extend([ (i, path + [loc]) for i in get_possible_moves(loc, len(grid[0])-1) ])
                visited.add(loc)
        else:
            return path


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)
    parser.add_option("-g", "--grid", dest="grid_size", help="size of grid", default=0, type=int)
    parser.add_option("-b", "--bytes", dest="num_bytes", help="number of bytes to drop", default=0, type=int)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        # (col, row)
        byte_pos = [line.strip().split(',') for line in f]

    grid = [['.' for col in range(options.grid_size+1)] for row in range(options.grid_size+1)]

    for col, row in byte_pos[:options.num_bytes]:
        if (options.dbg):
            print(row, col)
        grid[int(row)][int(col)] = '#'

    if options.dbg:
        [print(i) for i in grid]

    path = bfs(grid, dbg=options.dbg)
    print(f"part1: {len(path)}")

    # part2
    for col, row in byte_pos[options.num_bytes:]:
        if (options.dbg):
            print(row, col)
        grid[int(row)][int(col)] = '#'
        if (int(row),int(col)) in path:
            path = bfs(grid, dbg=options.dbg)
            if not path:
                print(f"part2: {col},{row}")
                break
        else:
            continue

