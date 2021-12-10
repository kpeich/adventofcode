with open('day10.txt') as f:
    data = [line.strip() for line in f]

test = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''
t = test.split('\n')

scoring1 = { ')':3, ']':57, '}':1197, '>':25137 }
matching = { '(':')', '[':']', '{':'}', '<':'>' }

def part1(data):
    score = 0
    for line in data:
        open_chunk = ''
        closed_chunk = ''
        for ch in line:
            if ch in '([{<':
                open_chunk += ch
            else:
                bracket = open_chunk[-1]
                open_chunk = open_chunk[:-1]
                if matching[bracket] != ch:
                    score += scoring1[ch]
                    break
    return score

print(f'Test1: {part1(t)}')
print(f'Part1: {part1(data)}')

scoring2 = { ')':1, ']':2, '}':3, '>':4 }

def part2(data):
    scores = []
    for line in data:
        score = 0
        corr = False
        open_chunk = ''
        closed_chunk = ''
        for ch in line:
            if ch in '([{<':
                open_chunk += ch
            else:
                bracket = open_chunk[-1]
                open_chunk = open_chunk[:-1]
                if matching[bracket] != ch:
                    score += scoring2[ch]
                    corr = True
                    break
                else:
                    continue
        if not corr:
            print(f'{open_chunk}')
            for i in open_chunk[::-1]:
                score = score * 5 + scoring2[matching[i]]
            scores.append(score)
    sorted_scores = sorted(scores)
    return sorted(scores), sorted_scores[len(sorted_scores)//2], len(scores)

print(f'Test2: {part2(t)')
print(f'Part2: {part2(data)')
