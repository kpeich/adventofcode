from pathlib import Path

priority = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

test = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

def parse(filename):
    with open(filename) as f:
        data = [line.strip() for line in f]
    #file = Path(__file__).parent.parent / filename
    #data = file.read_text().split('\n')
    return data


def pt1(data, debug=False):
    if debug:
        common_items = [set(item[:len(item)//2]).intersection(item[len(item)//2:]).pop() for item in data]
        priority_num = sum([priority.index(set(item[:len(item)//2]).intersection(item[len(item)//2:]).pop()) for item in data])
        return (common_items, priority_num)

    return sum([priority.index(set(item[:len(item)//2]).intersection(item[len(item)//2:]).pop()) for item in data])

def pt2(data):
    prios = []
    for i in range(0,len(data),3):
        prios.append(priority.index(set(data[i]).intersection(data[i+1], data[i+2]).pop()))
        
    return sum(prios)

if __name__ == '__main__':
    test_data = test.split()
    data = parse('input.txt')
    #print(data)

    print(pt1(test_data))
    print(pt1(data))
    print(pt2(test_data))
    print(pt2(data))
