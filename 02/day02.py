def check_safe(diff_data, dbg=False):
    if dbg:
        # (increasing, decreasing, close)
        print(f"{diff_data}")
        print(f"DBG: {[(data[0] and data[2]) for data in diff_data]} {[(data[1] and data[2]) for data in diff_data]}")
    return all( (data[0] and data[2]) for data in diff_data ) or all( (data[1] and data[2]) for data in diff_data )

if __name__ == '__main__':

    #with open("test.txt") as f:
    with open("raw_data.txt") as f:
        reports = [list(map(int, line.strip().split(' '))) for line in f]
    
    part1 = []
    part2 = []
    for report in reports:
        print(f"REPORT: {report}")
        # part1 didn't need the extra data
        #diffs = [ i[1]-i[0] for i in zip(report, report[1:]) ]
        #safe = all(-4 < num < 0 for num in diffs) or all(0 < num < 4 for num in diffs)

        # part 2
        # (increasing, decreasing, close)
        diffs = [ (0 < i[1]-i[0], 0 > i[1]-i[0], 0 < abs(i[0] - i[1]) < 4) for i in zip(report, report[1:]) ]
        safe = check_safe(diffs)
        if safe: print("PASSED WITH NO HELP\n")
        part1.append(safe)
       
        if safe == False:
            old_inc, old_dec = None, None
            for idx, tup in enumerate(diffs):
                # tup is the difference data for report[idx] - report[idx+1]
                inc, dec, close = tup

                # is it failing for not being close?
                if (close == False) or (old_inc != inc) or (old_dec != dec):
                    # idx->idx+1 is not close, try idx+1->idx+2
                    new_report = report[0:idx] + report[idx+1:]
                    print(f"ERROR: ({report[idx]}->{report[idx+1]}) TRY: {new_report}")
                    diffs = [ (0 < i[1]-i[0], 0 > i[1]-i[0], 0 < abs(i[0] - i[1]) < 4) for i in zip(new_report, new_report[1:]) ]
                    safe = check_safe(diffs)
                    if safe == True:
                        print(f"FIXED: {new_report}\n")
                        break
                    else:
                        # idx+1->idx+2 is also not close, what about idx->idx+2?
                        new_report = report[0:idx+1] + report[idx+2:]
                        print(f"2nd TRY: {new_report}")
                        diffs = [ (0 < i[1]-i[0], 0 > i[1]-i[0], 0 < abs(i[0] - i[1]) < 4) for i in zip(new_report, new_report[1:]) ]
                        safe = check_safe(diffs)
                        if safe == True:
                            print(f"FIXED: {new_report}\n")
                        elif old_inc != None:
                            # if this isn't the first pair we're done, otherwise it might have been the wrong direction
                            print(f"IMPOSSIBLE {report}\n")
                            break
                old_inc = inc
                old_dec = dec

        part2.append(safe)

    print(f"Part1: {sum(part1)}")
    print(f"Part2: {sum(part2)}")
