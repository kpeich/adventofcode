import optparse

def rot_90(grid):
    return [list(reversed(item)) for item in zip(*grid)]

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        data = f.read().strip()

    locks_and_keys = [item.split('\n') for item in data.split('\n\n')]

    if options.dbg:
        print(locks_and_keys)


    locks = []
    keys = []
    for item in locks_and_keys:
        lock = True if item[0] == '#####' else False
        if lock:
            locks.append(tuple([height.count('#') for height in rot_90(item[1:])]))
        else:
            keys.append(tuple([height.count('#')-1 for height in rot_90(item[1:])]))
    if options.dbg:
        print(f"LOCKS : {locks}")
        print(f"KEYS  : {keys}")

    part1 = []
    for lock in locks:
        for key in keys:
            part1.append(not any([(sum(x)-5)>0 for x in zip(lock,key)]))
    print(f"part1: {sum(part1)}")
