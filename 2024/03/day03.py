if __name__ == '__main__':

    # grep out all mul instructions : egrep -o 'mul\([0-9]{1,3},[0-9]{1,3}\)' raw_data.txt > mul_data.txt
    with open("mul_data.txt") as f:
        operands = [list(map(int, line[4:-2].strip().split(','))) for line in f]

    part1 = sum([pair[0] * pair[1] for pair in operands])
    print(f"Part1: {part1}")
    
    #grep -Po "do\(\)|don't\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)" raw_data.txt > mul_do_dont_data.txt
    ops = []
    with open("mul_do_dont_data.txt") as f:
        active = True
        for line in f:
            if ("mul" in line) and active:
                ops.append(list(map(int, line[4:-2].strip().split(','))))
            elif "don" in line: 
                active = False
            elif "do()" in line:
                active = True

    part2 = sum([pair[0] * pair[1] for pair in ops])
    print(f"Part2: {part2}")
