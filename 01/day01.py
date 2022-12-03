from pathlib import Path

def parse(filename):
    file = Path(__file__).parent.parent / filename
    data = file.read_text().split('\n\n')
    data = [[int(j) for j in i.split()] for i in data]
    return data

def pt1(data):
    return sorted([sum(elf) for elf in data])[-1]

def pt2(data):
    return sum(sorted([sum(elf) for elf in data])[-3:])

if __name__ == '__main__':
    data = parse('input.txt')

    print(pt1(data))
    print(pt2(data))
