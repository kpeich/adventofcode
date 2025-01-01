import optparse

def get_nodes(antennas, harmonics=False):
    nodes = set()
    for antenna, locations in antennas.items():
        for a in locations:
            nodes.add(a)
            for b in locations:
                if a == b:
                    continue
                else:
                    row_diff = a[0] - b[0]
                    col_diff = a[1] - b[1]
                    node_x = a[0] + row_diff
                    node_y = a[1]+col_diff
                    if options.dbg:
                        print(a,b, (a[0] + row_diff, a[1]+col_diff))
                    if (0<=node_x<=len(grid)-1) and (0<=node_y<=len(grid[0])-1):
                        nodes.add((node_x,node_y))
                        if harmonics:
                            while (0<=node_x<=len(grid)-1) and (0<=node_y<=len(grid[0])-1):
                                node_x += row_diff
                                node_y += col_diff
                                if options.dbg:
                                    print(a,b, (node_x, node_y))
                                if (0<=node_x<=len(grid)-1) and (0<=node_y<=len(grid[0])-1):
                                    nodes.add((node_x,node_y))
    return nodes

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        grid = [[i for i in line.strip()] for line in f]

    antennas = {}
    for rdx, row in enumerate(grid):
        for cdx, col in enumerate(row):
            if col == '.':
                continue
            else:
                antennas[col] = antennas[col] + [(rdx,cdx)] if col in antennas else [(rdx,cdx)]

    if options.dbg:
        print(antennas)

    part1 = get_nodes(antennas)
    print(f"Part1: {len(part1)}")

    part2 = get_nodes(antennas,harmonics=True)
    print(f"Part2: {len(part2)}")
