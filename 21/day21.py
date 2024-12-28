import optparse

data = '459A,671A,846A,285A,083A'
test = '029A,980A,179A,456A,379A'

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    if options.dbg:
        print(test)


    part1 = 0
    print(f"part1: {part1}")

    part1 = 0
    print(f"part2: {part2}")
