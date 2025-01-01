import optparse
from copy import deepcopy

def find_operators(target, nums, dbg=False):
    # start with nums[0], possibilities=2**(len(nums)-1)
    totals = [nums[0] for i in range(2**(len(nums)-1))]
    nums.pop(0)
    shift = 0
    while nums:
        num = nums.pop(0)
        for idx,tot in enumerate(totals):
            if bin(idx >> shift)[-1] == '0':
                totals[idx] += num
            else:
                totals[idx] *= num
        shift += 1
    return target if target in totals else 0

def base3(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        r = n % 3
        n = n // 3
        nums.append(str(r))
    return ''.join(reversed(nums))

def find_operators_part2(target, nums, base, dbg=False):
    totals = [nums[0] for i in range(base**(len(nums)-1))]
    nums.pop(0)
    shift = -1
    while nums:
        num = nums.pop(0)
        for idx,tot in enumerate(totals):
            base3_idx = base3(idx)
            try:
                if base3_idx[shift] == '0':
                    totals[idx] += num
                elif base3_idx[shift] == '1':
                    totals[idx] *= num
                else:
                    totals[idx] = int(str(totals[idx]) + str(num))
            except IndexError:
                totals[idx] += num
            if dbg:
                print(totals)
        shift -= 1
    if dbg:
        print(target, target in totals, totals)
        
    return target if target in totals else 0

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        equations = {int(line.strip().split(':')[0]) : list(map(int,line.strip().split(':')[1].strip().split(' '))) for line in f}
            
    if options.dbg:
        print(equations)

    pt1_nums = deepcopy(equations)
    part1 = 0
    passed_part1 = [] # part2 was taking too long so I added in this.
    for target, nums in pt1_nums.items():
        part1 += find_operators(target,nums)
        passed_part1.append(target)
    print(f"Part1: {part1}")

    pt2_nums = deepcopy(equations)
    part2 = 0
    for target, nums in pt2_nums.items():
        if target in passed_part1:
            part2 += target
        else:
            part2 += find_operators_part2(target,nums,3,dbg=options.dbg)
    print(f"Part2: {part2}")
