score = {'r':1, 'p':2, 's':3, 'w':6, 'l':0, 't':3}
test = ['A Y', 'B X', 'C Z']

def pt1(data):
    # x = rock, y = paper, z = scissors
    # tie, win, lose 
    # lose, tie, win
    # win, lose, tie
    scoring = {'A X': score['t'] + score['r'], 'A Y': score['w'] + score['p'], 'A Z': score['l'] + score['s'], \
            'B X': score['l'] + score['r'], 'B Y' : score['t'] + score['p'], 'B Z': score['w'] + score['s'], \
            'C X': score['w'] + score['r'], 'C Y': score['l'] + score['p'], 'C Z': score['t'] + score['s'] }

    return sum([scoring[rd] for rd in data])

def pt2(data):
    # x = lose; y = tie, z = win
    # scissors, rock, paper 
    # rock, paper, scissors
    # paper, scissors, rock
    scoring = {'A X': score['s'] + score['l'], 'A Y': score['r'] + score['t'], 'A Z': score['p'] + score['w'], \
            'B X': score['r'] + score['l'], 'B Y' : score['p'] + score['t'], 'B Z': score['s'] + score['w'], \
            'C X': score['p'] + score['l'], 'C Y': score['s'] + score['t'], 'C Z': score['r'] + score['w'] }
    return sum([scoring[rd] for rd in data])

if __name__ == '__main__':
    with open('input.txt') as f:
        data = [line.strip() for line in f]

    print(f"TEST: {pt1(test)}")
    print(pt1(data))

    print(f"TEST: {pt2(test)}")
    print(pt2(data))
