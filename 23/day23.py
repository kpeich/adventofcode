import optparse

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        lines = [tuple(line.strip().split('-')) for line in f]

    if options.dbg:
        print(lines)

    connections = {}
    for comp1,comp2 in lines:
        connections.setdefault(comp1,[comp2]).append(comp2)
        connections.setdefault(comp2,[comp1]).append(comp1)

    part1 = set()
    for comp1,comps1 in connections.items():
        for comp2 in comps1:
            for comp3 in connections[comp2]:
                if (comp1 != comp3) and (comp1 in connections[comp3]):
                    part1.add(tuple(sorted([comp1,comp2,comp3])))
    if options.dbg:
        [print(i) for i in sorted(part1)]
        print(len(part1))
    print(f"part1: {sum([1 for i in [[1 for j in i if j.startswith('t')] for i in part1] if i])}")

    lans = {}
    for comp1,party1 in connections.items():
        for comp2,party2 in connections.items():
            lan = tuple(sorted(set(party1 + [comp1]) & set(party2 + [comp2])))
            if lan != tuple():
                lans[lan] = lans.setdefault(lan,0) + 1

    if options.dbg:
        [print(num, lan) for lan,num in lans.items()]

    # there's probably a better way to deal with the self matching sets, but this works too
    parties = [lan for lan,num in lans.items() if (len(lan)+num)/len(lan) == len(lan)]
    print(f"part2: {','.join(sorted(parties,key=len)[-1])}")
