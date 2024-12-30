import optparse

data = ['459A','671A','846A','285A','083A']
test = ['029A','980A','179A','456A','379A']

class Robot():
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.position = None
        self.pad = None
        self.seq = None
        self.pressed = []

    def get_adjacent(self, pos):
        row, col = pos
        adjacent = [(row,col+1), (row-1,col), (row+1,col), (row, col-1)] # this order is important, we need to minimize the directional keypad movements
        return [(x,y) for x,y in adjacent if (x,y) in self.pad]

    def move(self, button):
        #move_dict = { '<':(0,-1), '>':(0,1), '^':(1,0), 'v':(-1,0) }
        move_dict = { (0,-1):'<', (0,1):'>', (1,0):'^', (-1,0):'v' }

        queue = [(self.position,[])]
        visited = set()
#        print(f"SEARCH FOR {button}")
        while queue:
            loc, path = queue.pop(0)
            if (self.pad[loc] != button):
                if (loc in visited) or (loc not in self.pad) :
                    continue
                else:
                    queue.extend([ (i, path + [ (i[0]-loc[0],i[1]-loc[1]) ]) for i in self.get_adjacent(loc) ])
                    visited.add(loc)
            else:
                if (self.position[1] - loc[1] == 2) and ( ((0,0) not in self.pad and self.position[0] != 0) or ((0,0) in self.pad and self.position[0] == 1)):
                    # move left first if we need to do it twice, but mind the gap (there is something more to the order here)
                    self.pressed = self.pressed + [move_dict[move] for move in path][::-1] + ['A']
                else:
                    self.pressed = self.pressed + [move_dict[move] for move in path] + ['A']
                self.position = loc
#                print(f"FOUND {button} with {self.pressed} now at {self.position}")
                return

    def print_movement(self):
        print(''.join(self.pressed))

    def reset(self):
        self.pressed = []
        self.alive = True
        self.seq = None

class Directional(Robot):
    def __init__(self, name):
        super().__init__(name)
        self.position = (1,2)
        self.pad ={           (1,1):'^', (1,2):'A', 
                   (0,0):'<', (0,1):'v' ,(0,2):'>' }
    def reset(self):
        super().reset()
        self.position = (1,2)

class Numeric(Robot):
    def __init__(self, name, codes):
        super().__init__(name)
        self.codes = codes
        self.position = (0,2)
        self.pad = {(3,0):'7', (3,1):'8' ,(3,2):'9',
                    (2,0):'4', (2,1):'5', (2,2):'6',
                    (1,0):'1', (1,1):'2', (1,2):'3',
                               (0,1):'0', (0,2):'A'}
    def get_moves(self):
        for code in self.codes:
            for button in code:
                self.move(button)
    def reset(self):
        super().reset()
        self.position = (0,2)


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    if options.dbg:
        print(test)

    rad = Directional('Brad')
    cold = Directional('Iceman')
    space = Numeric('NoOxy', test)
    #space = Numeric('NoOxy', data)

    complexities = {}
    for code in space.codes:
        space.reset()
        for button in code:
            space.move(button)
            cold.reset()
        for button in ''.join(space.pressed):
            cold.move(button)
            rad.reset()
        for button in ''.join(cold.pressed):
            rad.move(button)

        rad.print_movement()
        cold.print_movement()
        space.print_movement()
        print(code)
        print(f"{len(rad.pressed)} * {int(code[:-1])} = {int(code[:-1]) * len(rad.pressed)}")
        complexities[code] = int(code[:-1]) * len(rad.pressed)
        #178770 too high
    print(f"part1: {sum([num for code,num in complexities.items()])}")

    part2 = 0
    print(f"part2: {part2}")
