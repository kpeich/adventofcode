import optparse

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        data = [line.strip() for line in f]

    if options.dbg:
        pass

    part1 = 0
    print(f"part1: {part1}")

    part2 = 0
    print(f"part2: {part2}")
