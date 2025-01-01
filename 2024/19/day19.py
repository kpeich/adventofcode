import optparse
import functools

def get_possible(pattern, towels):
    if pattern == '':
        return '!'
    else:
        towel_list = ''
        for towel in towels:
            if pattern.startswith(towel):
                towel_list = towel_list + towel + ',' + get_possible(pattern[len(towel):],towels)
# for part2?
#        if towel_list != '' and towel_list[-1] == '!':
#            return towel_list
# just tryin to exit early
                if towel_list[-1] == '!':
                    return towel_list
        return ''

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        lines = [line.strip() for line in f]

    towels = tuple(lines[0].split(', '))
    designs = lines[2:]

    if options.dbg:
        print(len(towels))
        print(sorted(towels, key=len,reverse=True))

    part1 = []
    test = 'grrgwbgubwrbubrwubguburrggbbugwwwwruuwwuggbg'
    print(f"TEST {get_possible(test,towels)}")

    part1 = [get_possible(design,towels) for design in designs]
    if options.dbg:
        print(f"{part1}")
    print(f"Part1: {len([i.count('!') for i in part1 if '!' in i])}")


    #print([i for i in part1])
    print(f"Part2: {[i.count('!') for i in part1 if '!' in i]}")
    print(f"Part2: {sum([i.count('!') for i in part1 if '!' in i])}")
