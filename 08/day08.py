with open('day08.txt') as f:
    data = [line.strip() for line in f]
    sseg = [display.split(' | ') for display in data]

ex = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'
ex = [ex.split(' | ') for i in ex.split('\n')]

test = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''

t = [i.split(' | ') for i in test.split('\n')]
#print(t)

def part1(data):
    count = 0
    for i in data:
        for digit in i[1].split():
            if len(digit) in [2,4,3,7]:
                count += 1
    return count

print(f'Test1: {part1(t)}')
print(f'Part1: {part1(sseg)}')

def get_unique(signal):
    unique_digits = {}
    for i in signal.split():
        if len(i) == 2:
            unique_digits[1] = set(i)
        elif len(i) == 4:
            unique_digits[4] = set(i)
        elif len(i) == 3:
            unique_digits[7] = set(i)
        elif len(i) == 7:
            unique_digits[8] = set(i)
    return unique_digits

def get_digits(signal):
    digits = get_unique(signal)
    for digit in signal.split():
        if len(digit) == 6:
            if len(digits[1] - set(digit)) == 1:
                digits[6] = set(digit)
            elif len(digits[4] - set(digit)) == 1:
                digits[0] = set(digit)
            else:
                digits[9] = set(digit)
        elif len(digit) == 5:
            if len(set(digit) - digits[4]) == 3:
                digits[2] = set(digit)
            elif len(set(digit) - digits[1]) == 4:
                digits[5] = set(digit)
            elif len(set(digit) - digits[1]) == 3:
                digits[3] = set(digit)
        else:
            continue
    return digits

def part2(data):
    nums = []
    for signal in data:
        sig_in, sig_out = signal
        digits = get_digits(sig_in)
        num = ''
        for digit in sig_out.split():
            num += str([key for key,value in digits.items() if set(digit) == value][0])
        nums.append(int(num))
    return sum(nums)

print(f'Test2: {part2(t)}')
print(f'Part2: {part2(sseg)}')
