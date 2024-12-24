import optparse

test = '2333133121414131402'

def get_disk(data):
    disk = []
    for idx,i in enumerate(data):
        if idx % 2 == 0:
            disk += [(str(idx//2))] * int(i)
        else:
            disk += ['.'] * int(i)
    return disk

def defrag(disk):
    defragged = []
    tail = -1
    for idx, data in enumerate(disk):
        if data != '.':
            continue
        else:
            while disk[tail] == '.':
                tail -= 1
            if (disk[tail] != '.') and (idx < len(disk)+tail):
                disk[idx] = disk[tail]
                disk[tail] = '.'
    return disk

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        data = [line.strip() for line in f][0]

    if options.dbg:
        disk = get_disk(test)
        print(disk)
        defrag(disk)
        print(disk)
        checksum = sum([idx*int(data) for idx,data in enumerate(disk) if data != '.'])
        print(f"TEST: {checksum}")
        
    disk = get_disk(data)
    defrag(disk)
    checksum = sum([idx*int(data) for idx,data in enumerate(disk) if data != '.'])
    print(f"Part1: {checksum}")

    part2 = 0
    print(f"Part2: {part2}")
