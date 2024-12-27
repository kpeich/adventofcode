import optparse

def get_possible_moves(loc, grid_size):
    '''
    loc is tupe of (row, col)
    grid_size size of square grid

    returns list of possible (row, col) locations to move to
    '''
    row, col, direction = loc
    adjacent_cells = [(row+1,col), (row-1,col), (row,col+1), (row, col-1)]

    loc_with_cost = []
    if (direction == 'N'):
        ahead = (row-1, col)
        behind = (row+1, col)
    elif (direction == 'E'):
        ahead = (row, col+1)
        behind = (row, col-1)
    elif (direction == 'S'):
        ahead = (row+1, col)
        behind = (row-+1, col)
    else:
        ahead = (row, col-1)
        behind = (row, col+1)

    for x,y in adjacent_cells:
        if (grid[x][y] == '#') or (behind == (x,y)):
            continue
        elif (ahead == (x,y)):
            loc_with_cost.append( ((x,y,direction),1) )
        elif (direction in ['N', 'S']):
            loc_with_cost.append( ((row,col,'E'),1000) )
            loc_with_cost.append( ((row,col,'W'),1000) )
        elif (direction in ['E', 'W']):
            loc_with_cost.append( ((row,col,'N'),1000) )
            loc_with_cost.append( ((row,col,'S'),1000) )
            
    return loc_with_cost


def bfs(start, end, grid, dbg=False):
    queue = [ {'loc': start, 'path': [],  'score': 0} ]
    visited = set()
    winners = []

    while queue:
        queue.sort(key=lambda queue: queue['score'])
        entry = queue.pop(0)

        if dbg:
            print(queue)
            print(entry['loc'])
        if (entry['loc'][:2] != end):
            if (entry['loc'] in visited):
                continue
            else:
                queue.extend([ {'loc': i , 'path': entry['path'] + [entry['loc']], 'score': entry['score'] + cost } for i,cost in get_possible_moves(entry['loc'], len(grid[0])-1) ])
                visited.add(entry['loc'])
        else:
            return entry
    return winners

def dfs(start, end, grid, cutoff, dbg=False):
    queue = [ {'loc': start, 'path': [],  'score': 0} ]
    winners = []
    visited = set()

    while queue:
        entry = queue.pop()

        if dbg:
            print(queue)
            print(entry['loc'])
        if (entry['loc'][:2] != end):
            if (entry['score'] > cutoff):
                continue
            else:
                queue.extend([ {'loc': i , 'path': entry['path'] + [entry['loc']], 'score': entry['score'] + cost } for i,cost in get_possible_moves(entry['loc'], len(grid[0])-1) ])
        else:
            entry['path'].append(entry['loc'])
            winners.append(entry) 
    return winners


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    INF = 99999999999999
    WALL = '#'
    START = 'S'
    END = 'E'
    with open(options.filename) as f:
        grid = [line.strip() for line in f]

    start, end = None, None
    for row_idx, row in enumerate(grid):
        if START in row:
            start = (row_idx, row.index(START), 'E') # start facing east
        if END in row:
            end = (row_idx, row.index(END)) # don't care what dir we face to end
            
    if options.dbg:
        [print(i) for i in grid]

    winner = bfs(start, end, grid, dbg=options.dbg)
    print(f"part1: {winner['score']}")

    winners = dfs(start, end, grid, winner['score'], dbg=options.dbg)
    tiles = set()
    for winner in winners:
        for tile in winner['path']:
            tiles.add(tile[:2])
    print(f"part2: {len(tiles)}")
