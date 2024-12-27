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
        outside = []
        #outside = {}
        for loc in box:
            row,col = loc
            border = (row+1,col),(row-1,col),(row,col+1),(row,col-1)
            outside += [plant for plant in border if plant not in box]
            #outside[loc] = [plant for plant in border if plant not in box]
        
        side_counts = {i:outside.count(i) for i in outside}
        sides = []
        idx = 0
        for side,count in side_counts.items():
            row,col = side
            num_added = 0
            # look vertical
            if ((row+1,col) in outside) or (row-1,col) in outside and ((row,col+1) in box or (row,col-1) in box):
                sides.append([side])
                while (row,col) in outside and ((row,col+1) in box or (row,col-1) in box):
                    sides[idx].append((row,col))
                    row += 1
                row,col=side
                while (row,col) in outside and ((row,col+1) in box or (row,col-1) in box):
                    sides[idx].append((row,col))
                    row -= 1
                sides[idx] = list(set(sides[idx]))
                print(f"{side} : {sides[idx]}")
                num_added += 1
                idx += 1
            
            # look horizontal
            row,col = side
            if ((row,col+1) in outside or (row,col-1) in outside) and ((row+1,col) in box or (row-1,col) in box):
                sides.append([side])
                while (row,col) in outside and ((row+1,col) in box or (row-1,col) in box):
                    sides[idx].append((row,col))
                    col += 1
                row,col=side
                while (row,col) in outside and ((row+1,col) in box or (row-1,col) in box):
                    sides[idx].append((row,col))
                    col -= 1
                sides[idx] = list(set(sides[idx]))
                print(f"{side} : {sides[idx]}")
                num_added += 1
                idx += 1
            while num_added < count:
                print(f"SOLO {side} {num_added} {count}")
                sides.append([side])
                num_added += 1
                idx += 1

        uniq = { tuple(sorted(side)):sides.count(side) for side in sides }
        print([loc for loc in side_counts if side_counts[loc] > 1])
        uniq_sides = sum([uniq[fence] if len(fence) == 1 else 1 for fence in uniq])
        #return len(uniq), uniq
        #return uniq_sides * area
        print(side_counts)
        return uniq_sides, uniq

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

    [print(region) for region in regions.items()]
    #a = (('R', (0, 0)), [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 2), (1, 1), (1, 0), (2, 2), (2, 3), (2, 4), (3, 2)])
    #a = (('S', (8, 4)), [(8, 4), (9, 4), (9, 5)]) 
    #a = (('F', (0, 8)), [(0, 8), (0, 9), (1, 9), (2, 9), (2, 8), (2, 7), (3, 7), (3, 8), (3, 9), (4, 8)])
    a = (('E', (0, 0)), [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)])
    #(('X', (1, 1)), [(1, 1), (1, 2), (1, 3), (1, 4)])
    #(('X', (3, 1)), [(3, 1), (3, 2), (3, 3), (3, 4)])
    part2 = fence_cost(a,discount=True,dbg=options.dbg)
    print(f"Part2: {part2}")
    #part2 = [fence_cost(region,discount=True,dbg=options.dbg) for region in regions.items()]
    # too high: 898170 
    #print(f"Part2: {sum(part2)}")
