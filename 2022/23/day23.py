def pt1(data):
    continue

def pt2(data):
    continue

if __name__ == '__main__':
    with open('input.txt') as f:
        data = [line.strip() for line in f]

    print(f"TEST: {pt1()}")
    print(pt1(data))

    print(f"TEST: {pt2()}")
    print(pt2(data))
