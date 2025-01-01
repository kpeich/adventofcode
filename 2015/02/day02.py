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
    part2 = 0
    for box in data:
        l,w,h = tuple(int(i) for i in box.split('x'))
        part1 += 2*( l*w + l*h + w*h ) + min(l*w, l*h, w*h)
        part2 += 2*(sorted([l,w,h])[0] + sorted([l,w,h])[1]) + (l*w*h)
    print(f"part1: {part1}")
    print(f"part2: {part2}")
