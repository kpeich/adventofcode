test1 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
test2 = 'nppdvjthqldpwncqszvftbrmjlhg'
test3 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
test4 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

def pt1(data):
    for i in range(4,len(data)):
#        print(data[i-4:i])
        if len(set(data[i-4:i])) == 4:
            return i

def pt2(data):
    for i in range(14,len(data)):
#        print(data[i-14:i])
        if len(set(data[i-14:i])) == 14:
            return i

if __name__ == '__main__':
    with open('input.txt') as f:
        data = [line.strip() for line in f]

    print(f"TEST1: {pt1(test1)}")
    print(f"TEST2: {pt1(test2)}")
    print(f"TEST3: {pt1(test3)}")
    print(f"TEST4: {pt1(test4)}")
    print(pt1(data[0]))

    print(f"TEST1: {pt2(test1)}")
    print(f"TEST2: {pt2(test2)}")
    print(f"TEST3: {pt2(test3)}")
    print(f"TEST4: {pt2(test4)}")
    print(pt2(data[0]))
