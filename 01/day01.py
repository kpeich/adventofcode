if __name__ == '__main__':

    left, right = [], []
    #with open("test.txt") as f:
    with open("raw_data.txt") as f:
        for line in f:
            l, r = line.strip().split('   ')
            left.append(int(l))
            right.append(int(r))

    part1 = sum([abs(i[0] - i[1]) for i in zip(sorted(left), sorted(right))])
    print(f"Part1: {part1}")

    sim_score = {}
    part2 = 0
    for num in left:
        try:
            part2 += num * sim_score[num]
        except:
            sim_score[num] = right.count(num)
            part2 += num * sim_score[num]
    print(f"Part2: {part2}")
