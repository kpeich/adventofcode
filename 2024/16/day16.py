import optparse
import sys

# A* Algorithm (https://en.wikipedia.org/wiki/A*_search_algorithm)
# BFS Algorithm (https://en.wikipedia.org/wiki/Breadth-first_search#Pseudocode)
INF = 99999999999999
WALL = '#'
START = 'S'
END = 'E'

MASTER_HISTORY = set()
GOOD_PATHS = []

def get_possible_moves(loc, history):
    '''
    loc is tupe of (row, col, dir)
    history is list of previous positions

    returns list of possible (row, col) locations to move to
    '''
    row, col, direction = loc
    #last_pos = (INF, INF, 'E')
    pos_history = [loc[:2] for loc in history]
#    print(pos_history)
    #if history != []:
    #    last_pos = history[-1]
    
    adjacent_cells = [(row+1,col), (row-1,col), (row,col+1), (row, col-1)]

    #return [(row,col) for row,col in adjacent_cells if ( (grid[row][col] != WALL) and ((row, col) != last_pos[:2]) )]
    return [(row,col) for row,col in adjacent_cells if ( (grid[row][col] != WALL) and ((row, col) not in pos_history) )]


def try_move(loc, history, end, moves, turns, grid):
    '''
    loc is tupe of (row, col, dir)
    end is (row,col) ending location
    history is path history of locations
    grid is the puzzle grid
    '''
    mov = {'N': (-1,0), 'E': (0,1), 'S': (1,0), 'W': (0,-1)}
    ahead = tuple(x + y for x, y in zip(mov[loc[-1]], loc[:2]))
    print(f"AT {loc} : {history}, {moves}, {turns}")

    print(f"MASTER : {MASTER_HISTORY}")

    if loc[:2] == end:
        print(f"Found END in {moves} moves and {turns} turns. PATH: {len(history)} {history} PT1 turns: {sum([x[2]!=y[2] for x,y in zip(history, history[1:])])}")
        turns = sum([pos[0][2] != pos[1][2] for pos in zip(history,history[1:])])
        GOOD_PATHS.append((turns*1000 + len(history)-turns ,turns, len(history) - turns, history))
        return
    else:
        possible_moves = get_possible_moves(loc, history)
        print(f"Possible Moves: {possible_moves}")
        if (possible_moves == []) or (loc in history):
            # this is dead path
            print("NOWHERE TO MOVE CAN'T MOVE BACKWARDS")
        else:
            for new_loc in possible_moves:
                MASTER_HISTORY.add(loc)
                print(f"AT {loc} TRYING: {new_loc}")
                visited = [new_loc[:2]+('N',), new_loc[:2]+('E',), new_loc[:2]+('S',), new_loc[:2]+('W',)]
                #print(f"VISITED: {set(visited)} HISTORY: {set(history)}")
                if set(visited).intersection(set(history)):
                    # this is dead path
                    print(f"LOCATION VISITED : {new_loc}")
                else:
                    if (loc[2] == 'N') and (new_loc == ahead):
                        moves += 1
                        print("MOVE NORTH")
                        try_move(new_loc + ('N',), history + [loc], end, moves, turns, grid)
                    elif (loc[2] == 'E') and (new_loc == ahead):
                        moves += 1
                        print("MOVE EAST")
                        try_move(new_loc + ('E',), history + [loc], end, moves, turns, grid)
                    elif (loc[2] == 'S') and (new_loc == ahead):
                        moves += 1
                        print("MOVE SOUTH")
                        try_move(new_loc + ('S',), history + [loc], end, moves, turns, grid)
                    elif (loc[2] == 'W') and (new_loc == ahead):
                        moves += 1
                        print("MOVE WEST")
                        try_move(new_loc + ('W',), history + [loc], end, moves, turns, grid)
                    else:
                        if loc[2] == 'N': # facing North
                            print('FACING NORTH')
                            if new_loc[1] > loc[1]: # try East
                                turns += 1
                                print("TURN EAST")
                                try_move(loc[:2] + ('E',), history + [loc], end, moves, turns, grid)
                            else: # try West
                                turns += 1
                                print("TURN WEST")
                                try_move(loc[:2] + ('W',), history + [loc], end, moves, turns, grid)

                        elif loc[2] == 'E': # facing East
                            print('FACING EAST')
                            if new_loc[0] > loc[0]: # try South 
                                turns += 1
                                print("TURN SOUTH")
                                try_move(loc[:2] + ('S',), history + [loc], end, moves, turns, grid)
                            else: # try North  
                                turns += 1
                                print("TURN NORTH")
                                try_move(loc[:2] + ('N',), history + [loc], end, moves, turns, grid)

                        elif loc[2] == 'S': # facing South
                            print('FACING SOUTH')
                            if new_loc[1] > loc[1]: # try East
                                turns += 1
                                print("TURN EAST")
                                try_move(loc[:2] + ('E',), history + [loc], end, moves, turns, grid)
                            else: # try West
                                turns += 1
                                print("TURN WEST")
                                try_move(loc[:2] + ('W',), history + [loc], end, moves, turns, grid)

                        elif loc[2] == 'W': # facing West
                            print('FACING WEST')
                            if new_loc[0] > loc[0]: # try South 
                                print("TURN SOUTH")
                                turns += 1
                                try_move(loc[:2] + ('S',), history + [loc], end, moves, turns, grid)
                            else: # try North
                                print("TURN NORTH")
                                turns += 1
                                try_move(loc[:2] + ('N',), history + [loc], end, moves, turns, grid)

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    sys.setrecursionlimit(10000)

    with open(options.filename) as f:
        grid = [line.strip() for line in f]

    start, end = None, None
    for row_idx, row in enumerate(grid):
        if START in row:
            start = (row_idx, row.index(START), 'E') # start facing east
        if END in row:
            end = (row_idx, row.index(END)) # don't care what dir we face to end
            
    if options.dbg:
        print("    ", end="")
        [print(f"{i//10}", end="") for i in range(len(grid[0]))]
        print("\n    ", end="")
        [print(f"{i%10}", end="") for i in range(len(grid[0]))]
        print()
        [print(f"{i:02} :{row}") for i, row in enumerate(grid)]
        print(f"Start: {start}, End: {end}\n")

    try_move(start, [], end, 0, 0, grid)
    part1 = min([path[0] for path in GOOD_PATHS])
    print(f"Part1: {part1}")

    part2 = 0
    print(f"Part2: {part2}")

