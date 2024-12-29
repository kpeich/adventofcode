import optparse

def mix(num, val):
    return num ^ val

def prune(num, mod=16777216):
    return num % mod

def gen_secret(num):
    num = prune(mix(num,num << 6))
    num = prune(mix(num,num >> 5))
    return prune(mix(num,num << 11))
    

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)
    parser.add_option("-t", "--time", dest="time", help="simulation time", default=10, type=int)

    options,args = parser.parse_args()

    with open(options.filename) as f:
        lines = [int(line.strip()) for line in f]

    if options.dbg:
        print(lines)
        time = 0
        nums = {0 : 123}
        while time < options.time:
            time += 1
            nums[time]= gen_secret(nums[time-1])
        print(nums)

    nums2k = []
    profit = {}
    for num in lines:
        price = {}
        time = 0
        nums = [None,None,None,num]
        diffs = [None,None,None,None]
        while time < options.time:
            time +=1
            nums.pop(0)
            nums.append(gen_secret(nums[-1]))

            diffs.pop(0)
            diffs.append(nums[-1]%10 - nums[-2]%10)
            if None not in diffs:
                price[tuple(diffs)] = price.setdefault(tuple(diffs), nums[-1] % 10)
        for key,val in price.items():
            profit[key] = profit.setdefault(key, 0) + val
        nums2k.append(nums[-1])

    print(f"part1: {sum(nums2k)}")
    sales_key = max(profit,key=profit.get)
    print(f"part2: {profit[sales_key]} bananas at {sales_key}")

