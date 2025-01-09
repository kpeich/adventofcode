import optparse

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    map_dict = {}
    with open(options.filename) as f:
        for line in f:
            city1, to, city2, eq, distance = line.strip().split()
            if city1 in map_dict:
                map_dict[city1][city2] = int(distance)
            else:
                map_dict[city1] = {city2 : int(distance)}

            if city2 in map_dict:
                map_dict[city2][city1] = int(distance)
            else:
                map_dict[city2] = {city1 : int(distance)}

    print(map_dict)
    if options.dbg:
        pass

    part1 = 0
    print(f"part1: {part1}")

    part2 = 0
    print(f"part2: {part2}")
