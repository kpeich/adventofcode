import optparse

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        data = [line.strip() for line in f][0]

    if options.dbg:
        pass

    house = [0,0]
    moves = {'<':(0,-1), '>':(0,1), '^':(1,0), 'v':(-1,0)}
    presents = { (0,0):1 }
    for move in data:
        house = [sum(i) for i in zip(house,moves[move])]
        presents[tuple(house)] = presents.setdefault(tuple(house), 1) + 1

    print(f"part1: {len(presents)}")

    houses = [[0,0],[0,0]]
    presents = {(0,0):2}
    for idx in range(0,len(data),2):
        houses[0] = [sum(i) for i in zip(houses[0],moves[data[idx]])]
        houses[1] = [sum(i) for i in zip(houses[1],moves[data[idx+1]])]
        presents[tuple(houses[0])] = presents.setdefault(tuple(houses[0]), 1) + 1
        presents[tuple(houses[1])] = presents.setdefault(tuple(houses[1]), 1) + 1
    print(f"part2: {len(presents)}")
