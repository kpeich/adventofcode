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

def get_racetrack(start, end, grid, dbg=False):
    # Defined one path from start to end racetrack
    queue = [ (start, []) ]
    visited = set()
    while queue:
        loc, path = queue.pop(0)
        if (loc != (len(grid[0])-1, len(grid[0])-1)):
            if dbg:
                print(loc, path, visited)
            if loc in visited:
                continue
            else:
                queue.extend([ (i, path + [loc]) for i in get_possible_moves(loc, len(grid[0])-1) ])
                visited.add(loc)
    return path

def get_manhattan_cheats(track, grid_size, time=2):
    '''
    track : list of tuples of (row, col) track positions
    grid_size : size of square grid
    time : amount of time allowed to cheat

    returns list of possible (row, col) locations to cheat to
    '''

    time_saved = []
    for idx, start in enumerate(track):
        for end in track[track.index(start)+1:]:
            start_row, start_col = start
            end_row, end_col = end

            manhattan = abs(start_row - end_row) + abs(start_col - end_col)
            if (manhattan <= time) and (path.index(end)-(idx+manhattan)):
                time_saved.append(path.index(end)-(idx+manhattan))
    return time_saved

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    START = 'S'
    END = 'E'
    with open(options.filename) as f:
        grid = [line.strip() for line in f]

    start, end = None, None
    for row_idx, row in enumerate(grid):
        if START in row:
            start = (row_idx, row.index(START))
        if END in row:
            end = (row_idx, row.index(END))
            
    if options.dbg:
        [print(i) for i in grid]
        print(start, end)

    path = get_racetrack(start, end, grid, dbg=options.dbg)

    part1 = get_manhattan_cheats(path, grid, time=2)
    if options.dbg:
        print(sorted(part1))
    print(f"part1: {sum([True for i in part1 if i > 99])}")

    part2 = get_manhattan_cheats(path, grid, time=20)
    if options.dbg:
        print(sorted(part2))
    print(f"part2: {sum([True for i in part2 if i > 99])}")
