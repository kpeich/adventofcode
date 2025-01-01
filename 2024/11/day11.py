import optparse
import functools

test = "0 1 10 99 999"
test2 = "125 17"
data = "5 62914 65 972 0 805922 6521 1639064"

@functools.lru_cache(maxsize=None)
def update_stone(stone):
    ndigits = len(str(stone))
    #If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    if stone == 0:
        return (1,)
    elif ndigits % 2 == 0:
        #If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
        #The left half of the digits are engraved on the new left stone
        #The right half of the digits are engraved on the new right stone.
        #The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.
        lstone = int(stone // 10**(ndigits/2))
        rstone = int(stone % 10**(ndigits/2))
        return (lstone,rstone)
    else: #If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
        return (stone * 2024,)

@functools.lru_cache(maxsize=None)
def watch_stone(stone, time):
    new_stone = update_stone(stone)

    if time == 1:
        return len(new_stone)
    else:
        return sum([watch_stone(next_stone, time-1) for next_stone in new_stone])

if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)
    parser.add_option("-n", "--numBlinks", dest="blinks", help="number of times to blink", type=int, default=25)

    options,args = parser.parse_args()

    if options.dbg:
        #test_stones = [int(stone) for stone in test2.split()]
        test_stones = [0]
        stones = { 0 : test_stones }
        blink = 0
        print(len(stones[blink]))
        [print(stone) for stone in stones.items()]

    # part1
    time = { 0:[int(stone) for stone in data.split()] }
    blink = 0
    while blink != 25:
        blink += 1
        time[blink] = []
        for stone in time[blink-1]:
            new_stone = update_stone(stone)
            for stone in new_stone:
                time[blink].append(stone) 
    print(f"You have {len(time[blink])} stones after {blink} blinks")

    # part2, recurse and cache
    part2 = sum([watch_stone(stone,options.blinks) for stone in time[0]])
    print(f"You have {part2} stones after {options.blinks} blinks")
