import optparse

def get_adjacent(loc):
    row, col = loc
    possible = (row+1,col),(row-1,col),(row,col+1),(row,col-1)

    return possible

def get_regions(garden):
    # this should be a dfs for all points?
    # "walls" will just be anything not matching the starting plant
    return

def fence_cost(region):
    # calculate the fence cost for a region
    return

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        garden = [line.strip() for line in f]

    if options.dbg:
        pass

    part1 = 0
    print(f"Part1: {garden}")
    part2 = 0
    print(f"Part2: {part2}")
