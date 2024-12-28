import optparse

def mix(num, val):
    return num ^ val

def prune(num, mod=16777216):
    return num % mod

def gen_secret(num, prices=False):
    print(num)
    num = prune(mix(num,num << 6))
    num = prune(mix(num,num >> 5))
    if prices:
        return prune(mix(num,num << 11)), prune(mix(num,num << 11)) % 10
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
    for num in lines:
        time = 0
        nums = {0 : num}
        while time < options.time:
            time +=1
            nums[time]= gen_secret(nums[time-1])
        nums2k.append(nums[options.time])

    #print(f"part1: {nums2k}")
    print(f"part1: {sum(nums2k)}")

#    if options.dbg:
#        print(lines)
#        time = 0
#        nums = {0 : (123,123%10,None)}
#        while time < options.time:
#            time += 1
#            num, price = gen_secret(nums[time-1][0], prices=True)
#            nums[time] = (num, price, price-nums[time-1][1])
#        [print(i) for i in nums.items()]

    prices2k = {}
    for idx,num in enumerate(lines):
        time = 0
        nums = {0 : (num,num%10,None)}
        while time < options.time:
            time +=1
            num, price = gen_secret(nums[time-1][0], prices=True)
            nums[time] = (num, price, price-nums[time-1][1])
        prices2k[idx] = nums

    [print(i) for i in prices2k.items()]
    #print(f"part2: {prices2k}")

