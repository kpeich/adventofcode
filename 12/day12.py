import optparse

def get_adjacent(loc, plant, grid):
    row, col = loc
    possible = (row+1,col),(row-1,col),(row,col+1),(row,col-1)

    return [(row,col) for row,col in possible if ( (0<=row<len(grid) and 0<=col<len(grid)) and (grid[row][col] == plant) )]

def dfs(start, plant, grid, dbg=False):
    queue = [ {'loc': start, 'box': []} ]
    box = []
    planted = set()

    while queue:
        entry = queue.pop()

        if dbg:
            print(plant, entry['loc'])
            print(queue)
        if entry['loc'] in planted:
            continue
        else:
            queue.extend([ {'loc': i , 'box': entry['box'] + [entry['loc']]} for i in get_adjacent(entry['loc'],plant,grid) ])
            planted.add(entry['loc'])
        box = box + [entry['loc']]
    return box

def get_regions(garden,dbg=False):
    # this should be a dfs for all points?
    # "walls" will just be anything not matching the starting plant
    regions = {}
    planted = set()
    for rdx,row in enumerate(garden):
        for cdx,col in enumerate(row):
            if (rdx,cdx) in planted:
                continue
            else:
                plant = col
                region = dfs((rdx,cdx), plant, garden,dbg=dbg)
                regions[(plant,(rdx,cdx))] = region
                for p in region:
                    planted.add(p)
    return regions

def fence_cost(region,discount=False,dbg=False):
    # calculate the fence cost for a region
    plant, box = region
    if dbg:
        print(plant, box)
    area = len(box)

    if discount:
        return

    perimeter = 0
    for loc in box:
        row,col = loc
        border = (row+1,col),(row-1,col),(row,col+1),(row,col-1)
        perimeter += sum([1 for plant in border if plant not in box])
    return perimeter*area

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        garden = [line.strip() for line in f]

    if options.dbg:
        pass

    regions = get_regions(garden,dbg=options.dbg)
    part1 = [fence_cost(region) for region in regions.items()]
    if options.dbg:
        print(f"GARDEN: {garden}")
        print(f"COSTS: {part1}")
    print(f"Part1: {sum(part1)}")

    a = (('R', (0, 0)), [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (1, 1), (1, 0), (2, 2), (2, 3), (2, 4), (3, 2)])
    part2 = fence_cost(a,discount=True,dbg=options.dbg)
    #part2 = [fence_cost(region,discount=True,dbg=options.dbg) for region in regions.items()]
    print(f"Part2: {part2}")
