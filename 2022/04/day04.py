import re
from pathlib import Path

test = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

def pt1(data):
    return sum([( (i[0]<=i[2]<=i[3]<=i[1]) or (i[2]<=i[0]<=i[1]<=i[3]) ) for i in data])

def pt2(data):
    return sum([( (i[0]<=i[2]<=i[1]) or (i[2]<=i[0]<=i[3]) ) for i in data])

if __name__ == '__main__':
    file = Path(__file__).parent / 'input.txt'
    data = [ [int(j) for j in i] for i in re.findall(r"(\d+)-(\d+),(\d+)-(\d+)", file.read_text()) ]

    tdata = [ [int(j) for j in i] for i in re.findall(r"(\d+)-(\d+),(\d+)-(\d+)", test) ]

    print(f"TEST: {pt1(tdata)}")
    print(pt1(data))

    print(f"TEST: {pt2(tdata)}")
    print(pt2(data))
