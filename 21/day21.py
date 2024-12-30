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
        self.pressed = ''

    def get_adjacent(self, pos):
        row, col = pos
        adjacent = [(row,col+1), (row-1,col), (row+1,col), (row, col-1)] # this order is important, we need to minimize the directional keypad movements
        return [(x,y) for x,y in adjacent if (x,y) in self.pad]

    def move(self, button):
        '''
        not functional, need to generalize the priority moves
        '''
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
                moves = ''.join([move_dict[move] for move in path])
                while self.pad[self.position] in moves:
                    self.pressed.append(self.pad[self.position])
                    moves.pop(moves.index(self.pad[self.position]))
                self.pressed = self.pressed + moves + 'A'
                self.position = loc
#                print(f"FOUND {button} with {self.pressed} now at {self.position}")
                return

    def print_movement(self):
        print(self.name, len(self.pressed), self.pressed)

    def reset(self):
        self.pressed = ''
        self.alive = True
        self.seq = None

class Directional(Robot):
    def __init__(self, name):
        super().__init__(name)
        self.position = (1,2)
        self.pad ={           (1,1):'^', (1,2):'A', 
                   (0,0):'<', (0,1):'v' ,(0,2):'>' }

        self.best_moves = {'A': {'<':'v<<', '>':'v', '^':'<', 'v':'<v'}, 
                           '^': {'A':'>', '<':'v<', '>':'v>', 'v':'v'},
                           'v': {'A':'^>', '<':'<', '>':'>', '^':'^'},
                           '<': {'A':'>>^', '>':'>>', '^':'>^', 'v':'>'}, 
                           '>': {'A':'^', '<':'<<', '^':'<^', 'v':'<'}} 
    def move(self, button):
        if self.pad[self.position] == button:
            self.pressed = self.pressed + 'A'
        else:
            self.pressed = self.pressed + self.best_moves[self.pad[self.position]][button] + 'A'
        self.position =  [pos for pos,val in self.pad.items() if val == button][0]

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

        # not sure if this is entirely correct, but it passes my input/test
        # make sure to prioritize the double move between < <-> A in the following steps
            # basically if you have < it should be at the beginning or end of a sequence
            # but also preserve double taps
        self.best_moves = {'A': {'0':'<', '1':'^<<', '2':'<^', '3':'^', '4':'^^<<', '5':'^^<', '6':'^^', '7':'^^^<<', '8':'<^^^', '9':'^^^'}, 
                           '0': {'A':'>', '1':'^<', '2':'^', '3':'>^', '4':'^^<', '5':'^<', '6':'>^', '7':'^^^<', '8':'^^^', '9':'>^^^'},
                           '1': {'0':'>v', 'A':'>>v', '2':'>', '3':'>>', '4':'^', '5':'>^', '6':'>>^', '7':'^^', '8':'>^^', '9':'>>^^'},
                           '2': {'0':'v', '1':'<', 'A':'v>', '3':'>', '4':'^<', '5':'^', '6':'>^', '7':'<^^', '8':'^^', '9':'>^^'},
                           '3': {'0':'<v', '1':'<<', '2':'<', 'A':'v', '4':'<<^', '5':'<^', '6':'^', '7':'<<^^', '8':'<^^', '9':'^^'},
                           '4': {'0':'>vv', '1':'v', '2':'>v', '3':'>>v', 'A':'>>vv', '5':'>', '6':'>>', '7':'^', '8':'>^', '9':'>>^'},
                           '5': {'0':'vv', '1':'<v', '2':'v', '3':'>v', '4':'<', 'A':'vv>', '6':'>', '7':'<^', '8':'^', '9':'^>'},
                           '6': {'0':'<vv', '1':'<<v', '2':'<v', '3':'v', '4':'<<', '5':'<', 'A':'vv', '7':'<<^', '8':'<^', '9':'^'},
                           '7': {'0':'>vvv', '1':'vv', '2':'>vv', '3':'vv>>', '4':'v', '5':'>v', '6':'v>>', 'A':'>>vvv', '8':'>', '9':'>>'},
                           '8': {'0':'vvv', '1':'<vv', '2':'vv', '3':'vv>', '4':'<v', '5':'v', '6':'>v', '7':'<', 'A':'vvv>', '9':'>'},
                           '9': {'0':'vvv<', '1':'<<vv', '2':'<vv', '3':'vv', '4':'<<v', '5':'<v', '6':'v', '7':'<<', '8':'<', 'A':'vvv'}}
    def move(self, button):
        if self.pad[self.position] == button:
            self.pressed = self.pressed + 'A'
        else:
            self.pressed = self.pressed + self.best_moves[self.pad[self.position]][button] + 'A'
        self.position =  [pos for pos,val in self.pad.items() if val == button][0]

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
    #space = Numeric('NoOxy', test)
    space = Numeric('NoOxy', data)

    robots = [space,cold,rad]
    complexities = {}
    for code in robots[0].codes:
        robots[0].reset()
        for button in code:
            robots[0].move(button)
        for idx,robot in enumerate(robots[1:]):
            robot.reset()
            for press in robots[idx].pressed:
                robot.move(press)
        print(f"{code}: {len(robots[-1].pressed)} * {int(code[:-1])} = {int(code[:-1]) * len(robots[-1].pressed)}")
        complexities[code] = int(code[:-1]) * len(rad.pressed)
    print(f"part1: {sum([num for code,num in complexities.items()])}") #169390

