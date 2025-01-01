import optparse

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging")

    options,args = parser.parse_args()

    rules = {}
    queues = []
    with open(options.filename) as f:
        for line in f:
            if '|' in line:
                page, rule = line.strip().split('|')
                try:
                    rules[page].append(rule)
                except:
                    rules[page] = [rule]
            elif line[0].isdigit():
                queues.append(line.strip().split(','))
    if options.dbg:
        print(queues)
        print(rules)

    part1 = 0
    part2 = 0
    for queue in queues:
        queue_rules = {}
        for page in queue:
            try:
                queue_rules[page] = [ i for i in rules[page] if i in queue ]
            except KeyError:
                queue_rules[page] = []
        fixed_queue = sorted(queue_rules, key=lambda k: len(queue_rules[k]), reverse=True)
        if options.dbg:
            print(queue, fixed_queue, queue==fixed_queue)

        if queue==fixed_queue: 
            part1 += int(queue[len(queue)//2]) 
        else:
            part2 += int(fixed_queue[len(fixed_queue)//2]) 

    print(f"Part1: {part1}")
    print(f"Part2: {part2}")
