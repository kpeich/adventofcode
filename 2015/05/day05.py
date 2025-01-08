import optparse

def check_string(string):
    invalid = ('ab','cd','pq','xy')
    vowels = 'aeiou'
    num_vowels = 0
    double = False

    for idx,ch in enumerate(string):
        if ch in vowels:
            num_vowels += 1
        try:
            if string[idx+1] == ch:
                double = True
            if ch+string[idx+1] in invalid:
                return False
        except:
            continue

    return num_vowels > 2 and double 

def check_string2(string):
    has_pair = False
    has_gap = False

    for idx,ch in enumerate(string):
        try:
            if string[idx+2] == ch:
                has_gap = True
        except IndexError:
            continue
        if string[idx-1]+ch in string[idx+1:] and idx != 0:
            has_pair = True

    return has_pair and has_gap


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        data = [line.strip() for line in f]

    if options.dbg:
        pass

    part1 = [check_string(string) for string in data]
    print(f"part1: {sum(part1)}")

    part2 = [check_string2(string) for string in data]
    print(f"part2: {sum(part2)}")
