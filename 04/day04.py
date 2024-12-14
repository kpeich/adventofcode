import optparse
# 2662 too high

if __name__ == '__main__':
    xmas = "XMAS"

    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")

    options,args = parser.parse_args()

    with open(options.filename) as f:
        data = [line.strip() for line in f]

    part1 = 0
    # this is the dumb way
    for row in range(len(data)):
        for col in range(len(data[row])):
            try:
                part1 += data[row][col] + data[row][col+1] + data[row][col+2] + data[row][col+3] == xmas # east
#                print(row,col,data[row][col] + data[row][col+1] + data[row][col+2] + data[row][col+3])
            except IndexError:
                pass
            try:
                part1 += data[row][col] + data[row][col+1] + data[row][col+2] + data[row][col+3] == xmas[::-1] # west
#                print(row,col,data[row][col] + data[row][col-1] + data[row][col-2] + data[row][col-3])
            except IndexError:
                pass
            try:
                part1 += data[row][col] + data[row+1][col] + data[row+2][col] + data[row+3][col] == xmas # south
#                print(row,col,data[row][col] + data[row+1][col] + data[row+2][col] + data[row+3][col])
            except IndexError:
                pass
            try:
                part1 += data[row][col] + data[row+1][col] + data[row+2][col] + data[row+3][col] == xmas[::-1] #north
#                print(row,col,data[row][col] + data[row-1][col] + data[row-2][col] + data[row-3][col])
            except IndexError:
                pass
            try:
                part1 += data[row][col] + data[row+1][col+1] + data[row+2][col+2] + data[row+3][col+3] == xmas # southeast
#                print(row,col,data[row][col] + data[row+1][col+1] + data[row+2][col+2] + data[row+3][col+3])
            except IndexError:
                pass
            try:
                if col-3 >= 0:
                    part1 += data[row][col] + data[row+1][col-1] + data[row+2][col-2] + data[row+3][col-3] == xmas # southwest
#                    print(row,col,data[row][col] + data[row+1][col-1] + data[row+2][col-2] + data[row+3][col-3])
            except IndexError:
                pass
            try:
                if col-3 >= 0 and row-3 >= 0:
                    part1 += data[row][col] + data[row-1][col-1] + data[row-2][col-2] + data[row-3][col-3] == xmas # northwest
#                    print(row,col,data[row][col] + data[row-1][col-1] + data[row-2][col-2] + data[row-3][col-3])
            except IndexError:
                pass
            try:
                if row-3 >= 0:
                    part1 += data[row][col] + data[row-1][col+1] + data[row-2][col+2] + data[row-3][col+3] == xmas # northeast
#                    print(row,col,data[row][col] + data[row-1][col+1] + data[row-2][col+2] + data[row-3][col+3])
            except IndexError:
                pass
    print(f"Part1: {part1}")
    
    part2 = 0
    for row in range(1,len(data)-1):
        for col in range(1,len(data[row])-1):
            if data[row][col] == "A":
                northM = (data[row-1][col-1] == 'M') and (data[row-1][col+1] == 'M') and (data[row+1][col-1] == 'S') and (data[row+1][col+1] == 'S')
                southM = (data[row+1][col-1] == 'M') and (data[row+1][col+1] == 'M') and (data[row-1][col-1] == 'S') and (data[row-1][col+1] == 'S')
                eastM = (data[row-1][col+1] == 'M') and (data[row+1][col+1] == 'M') and (data[row+1][col-1] == 'S') and (data[row-1][col-1] == 'S')
                westM = (data[row-1][col-1] == 'M') and (data[row+1][col-1] == 'M') and (data[row+1][col+1] == 'S') and (data[row-1][col+1] == 'S')

                part2 += (northM or southM or eastM or westM)

    print(f"Part2: {part2}")
