import optparse
import re

def on(x,y,grid):
    return True
def off(x,y,grid):
    return False
def flip(x,y,grid):
    return not grid[x][y]

def inc(x,y,grid):
    return 1
def dec(x,y,grid):
    return -1
def incc(x,y,grid):
    return 2

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    data = []
    with open(options.filename) as f:
        for line in f:
            fn = re.match(r'(.*) (\d+),(\d+).* (\d+),(\d+).*$', line)
            inst = fn.group(1)
            grid = tuple( int(fn.group(i)) for i in range(2,6) )
            data.append((inst,grid))

    if options.dbg:
        pass

    # part1
    lights = [[False for j in range(1000)]for i in range(1000)]
    code_dict = {'turn on': on, 'turn off': off, 'toggle': flip}
    for instr,coords in data:
        if options.dbg:
            print(instr,coords)
        for i in range(coords[0],coords[2]+1):
            for j in range(coords[1], coords[3]+1):
                lights[i][j] = code_dict[instr](i,j,lights)
    print(f"part1: {sum([sum(row) for row in lights])}")

    # part2
    lights2 = [[0 for j in range(1000)]for i in range(1000)]
    code_dict2 = {'turn on': inc, 'turn off': dec, 'toggle': incc}
    for instr,coords in data:
        if options.dbg:
            print(instr,coords)
        for i in range(coords[0],coords[2]+1):
            for j in range(coords[1], coords[3]+1):
                lights2[i][j] += code_dict2[instr](i,j,lights2)
                lights2[i][j] = 0 if lights2[i][j] < 0 else lights2[i][j]
    print(f"part2: {sum([sum(row) for row in lights2])}")
