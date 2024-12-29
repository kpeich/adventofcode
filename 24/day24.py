import optparse

class Machine:
    def __init__(self,wires,gates):
        self.wires = wires
        self.gates = gates
        self.outputs = sorted([ wire for wire in wires if wire.startswith('z') ])
        self.output = [ wires[wire] for wire in self.outputs ]
        self.ops = { 'AND':self.AND, 'OR':self.OR, 'XOR':self.XOR }

    def AND(self,out,in1,in2):
        self.wires[out] = self.wires[in1] & self.wires[in2]

    def OR(self,out,in1,in2):
        self.wires[out] = self.wires[in1] | self.wires[in2]

    def XOR(self,out,in1,in2):
        self.wires[out] = self.wires[in1] ^ self.wires[in2]
    
    def update_output(self):
        self.output = [wires[out] for out in self.outputs] 

    def run(self):
        for gate in self.gates:
            op,out,in1,in2 = gate
            if None not in [wires[in1],wires[in2]]:
                self.ops[op](out,in1,in2)
        self.update_output()
            

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    wires = {}
    gates = []
    with open(options.filename) as f:
        for line in f:
            if ':' in line:
                wire, signal = line.strip().split(': ')
                wires[wire] = int(signal)
            elif line[0] != '\n':
                in1, gate, in2, arrow, out = line.strip().split(' ')
                wires[in1] = wires.setdefault(in1, None)
                wires[in2] = wires.setdefault(in2, None)
                wires[out] = wires.setdefault(out, None)
                gates.append((gate,out,in1,in2))

    system = Machine(wires,gates)
    while None in system.output:
        system.run()

    part1 = ''.join(reversed([str(i) for i in system.output]))
    print(f"part1: {int(part1, base=2)}")
