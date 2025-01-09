import optparse

class Circuit:
    def __init__(self, wires, gates):
        self.wires = wires
        self.gates = gates
        self.ops = {'NOT':self.NOT, 'OR':self.OR, 'AND':self.AND, 'LSHIFT':self.LSHIFT, 'RSHIFT':self.RSHIFT, 'BUF':self.BUF}

    def NOT(self, out, in1):
        self.wires[out] = ~self.wires[in1] % 2**16

    def BUF(self, out, in1):
        self.wires[out] = self.wires[in1] % 2**16

    def OR(self, out, in1, in2):
        self.wires[out] = self.wires[in1] | self.wires[in2]

    def AND(self, out, in1, in2):
        self.wires[out] = self.wires[in1] & self.wires[in2]

    def LSHIFT(self, out, in1, in2):
        self.wires[out] = self.wires[in1] << in2

    def RSHIFT(self, out, in1, in2):
        self.wires[out] = self.wires[in1] >> in2

    def print_wires(self):
        print(self.wires)

    def rst(self):
        for wire in self.wires:
            if wire != 1:
                self.wires[wire] = None
        # these are the input wires
        self.wires['b'] = 1674
        self.wires['c'] = 0
    
    def run(self):
        for out,gate in self.gates.items():
            if gate[0] in ['NOT','BUF']:
                if self.wires[gate[1]] != None:
                    self.ops[gate[0]](out,gate[1])
            else:
                op, in1, in2 = gate
                if (op in ['LSHIFT', 'RSHIFT']):
                    if (self.wires[in1] != None):
                        self.ops[op](out,in1,in2)
                elif (op == 'AND'):
                    if (None not in [self.wires[in1],self.wires[in2]]):
                        self.ops[op](out,in1,in2)
                elif (None not in [self.wires[in1],self.wires[in2]]):
                    self.ops[op](out,in1,in2)

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    wires = {1:1}
    gates = {}
    with open(options.filename) as f:
        data = [line.strip().split(' -> ') for line in f]
        for gate,out in data:
            inputs = [int(i) if i.isdigit() else i for i in gate.split(' ')]
            wires[out] = wires.setdefault(out, None)
            if len(inputs) == 3:
                if type(inputs[0]) == str:
                    wires[inputs[0]] = wires.setdefault(inputs[0], None)
                if type(inputs[2]) == str:
                    wires[inputs[2]] = wires.setdefault(inputs[2], None)
                gates[out] = (inputs[1], inputs[0], inputs[2])
            elif len(inputs) == 2:
                if type(inputs[1]) == str:
                    wires[inputs[1]] = wires.setdefault(inputs[1], None)
                gates[out] = (inputs[0], inputs[1])
            else:
                if type(inputs[0]) == int:
                    wires[out] = inputs[0]
                else:
                    wires[inputs[0]] = wires.setdefault(inputs[0], None)
                    wires[out] = wires.setdefault(wires[inputs[0]],None)
                    gates[out] = ('BUF',inputs[0])

    if options.dbg:
        pass

    network = Circuit(wires,gates)
    network.print_wires()
    tmp = 0
    while network.wires['a'] == None and tmp < 1000:
        #network.print_wires()
        network.run()
        tmp += 1
    print(f"part1: {network.wires['a']}")

    part2 = network.wires['a']
    network.rst()
    network.wires['b'] = part2
    network.print_wires()
    while network.wires['a'] == None and tmp < 1000:
        network.run()
        tmp += 1
    print(f"part2: {network.wires['a']}")
