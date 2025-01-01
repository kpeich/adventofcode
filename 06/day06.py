with open('day06.txt') as f:
    school = [line.strip() for line in f]
    fish = [int(i) for i in school[0].split(',')]

test = [3,4,3,1,2]

def simulate(fish, days):
    reproduction = {i:fish.count(i) for i in range(9)}
    day = 0
    while (day < days):
        # spawner
        reproduction[9] = reproduction[0]
        for key in list(reproduction)[:-1]:
            reproduction[key] = reproduction[key+1]
        reproduction[6] += reproduction[9]
        day += 1
        #print(f'Day {day}: {reproduction.values()}')
    return sum(reproduction.values()) - reproduction[9]

print(f'Test 18 Days: {simulate(test, 18)}')
print(f'Part 1: {simulate(fish, 80)}')
print(f'Part 2: {simulate(fish, 256)}')

'''
Part 1 solution:

def populate(fish):
    new_fish = fish.count(0)
    fish[:] = [i-1 if i > 0 else 6 for i in fish]
    return fish + [8]*new_fish
def simulate(fish, days):
    day = 0;
    while (day < days):
        fish = populate(fish)
        #print(fish)
        day += 1
    return len(fish)

print(f'Test 18 Days: {simulate(test, 18)}')
print(f'Part 1: {simulate(fish, 80)}')
'''

