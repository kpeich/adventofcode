import optparse

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        data = [line.strip() for line in f][0]

    if options.dbg:
        print(data)

    part1 = data.count('(') - data.count(')')
    print(f"part1: {part1}")

    part2 = 0
    for idx,direction in enumerate(data):
        part2 = part2+1 if direction == '(' else part2-1
        if part2 == -1:
            print(f"part2: {idx+1}")
            break

