import optparse
import re

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
    for line in data:
        num_literal = len(line)
        print(line)
        line = re.sub(r'\\x[0-9A-Fa-f][0-9A-Fa-f]','x',line) # every ascii is just an x
        line = line.replace('\\"', '"')
        line = line.replace('\\\\', '\\')
        print(line)
        num_mem = len(line[1:-1])

        part1 += num_literal - num_mem
    print(f"part1: {part1}")

    part2 = 0
    for line in data:
        num_literal = len(line)
        print(line)
        line = line.replace('\\', '\\\\')
        line = line.replace('"', '\\"')
        print(line)
        num_mem = len(line) + 2 # add 2 for the outermost double quotes
        print(num_literal, num_mem)

        part2 += num_mem - num_literal 
    print(f"part2: {part2}")
