def get_inverse(nums):
    det = nums[0]*nums[3]-nums[1]*nums[2]
    return [nums[3], -1*nums[2], -1*nums[1], nums[0]], det

if __name__ == '__main__':

#    num_list = [[94,34,22,67,8400,5400],[26,66,67,21,12748,12176],[17,86,84,37,7870,6450],[69,23,27,71,18641,10279]]
#                ax,ay,bx,by,
    num_list = []
    with open("data.txt") as f:
        for line in f:
            num_list.append([int(i) for i in line.strip().split(',')])

    part1 = 0
    for game in num_list:
        inv_A, det = get_inverse(game[:4])
        pressA = (inv_A[0] * game[4] + inv_A[1] * game[5]) / det
        pressB = (inv_A[2] * game[4] + inv_A[3] * game[5]) / det
        cost = pressA*3 + pressB
        if int(pressA) == pressA and int(pressB) == pressB:
#            print(f"A: {pressA}, B: {pressB}, Cost: {cost}")
            part1 += cost
    print(f"Pt1: {int(part1)}")

    bignum = 10000000000000
    pt2_list = [ i[:4] + [i[4]+bignum, i[5]+bignum] for i in num_list ]
    part2 = 0
    for game in pt2_list:
        inv_A, det = get_inverse(game[:4])
        pressA = (inv_A[0] * game[4] + inv_A[1] * game[5]) / det
        pressB = (inv_A[2] * game[4] + inv_A[3] * game[5]) / det
        cost = pressA*3 + pressB
        if int(pressA) == pressA and int(pressB) == pressB:
#            print(f"A: {pressA}, B: {pressB}, Cost: {cost}")
            part2 += cost
    print(f"Pt2: {int(part2)}")
