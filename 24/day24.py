import optparse

class Machine:
    def __init__(self,wires,gates):
        self.wires = wires
        self.gates = gates
        self.outputs = sorted([ wire for wire in wires if wire.startswith('z') ])
        self.output = [ wires[wire] for wire in self.outputs ]
        self.ops = { 'AND':self.AND, 'OR':self.OR, 'XOR':self.XOR }
        self.swaps = []

    def AND(self,out,in1,in2):
        self.wires[out] = self.wires[in1] & self.wires[in2]

    def OR(self,out,in1,in2):
        self.wires[out] = self.wires[in1] | self.wires[in2]

    def XOR(self,out,in1,in2):
        self.wires[out] = self.wires[in1] ^ self.wires[in2]
    
    def update_output(self):
        self.output = [wires[out] for out in self.outputs] 

    def rst(self):
        print("RESETTING SYSTEM")
        for wire in self.wires:
            if wire[0] not in 'xy':
                self.wires[wire] = None 
        self.update_output()

    def print_gates(self):
        for out,gate in sorted(self.gates.items()):
            print(out, gate)

    def swap_gates(self,gate1,gate2):
        print(f"SWAP {gate1} with {gate2}")
        tmp = (gates[gate1], gates[gate2])
        gates[gate2] = tmp[0]
        gates[gate1] = tmp[1]
        self.swaps += [gate1,gate2]

    def run(self):
        for out,gate in self.gates.items():
            op,in1,in2 = gate
            if None not in [wires[in1],wires[in2]]:
                self.ops[op](out,in1,in2)
        self.update_output()
            

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="input filename")
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()

    wires = {}
    gates = {}
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
                gates[out] = (gate, in1, in2)

    system = Machine(wires,gates)
    while None in system.output:
        system.run()

    part1 = ''.join(reversed([str(i) for i in system.output]))
    print(f"part1: {int(part1, base=2)}")

    xin = ''.join(reversed([str(wires[i]) for i in wires if i.startswith('x')]))
    yin = ''.join(reversed([str(wires[i]) for i in wires if i.startswith('y')]))
    expected = bin(int(xin,base=2) + int(yin,base=2))

    print(f"EXPECTED: {expected}")
    print(f"ACTUAL  : 0b{part1}")
    error_bits = [str(bit).zfill(2) for bit,vals in enumerate(zip(part1[::-1],expected[2:][::-1])) if vals[0]!=vals[1]]
    print(f"ERR BITS: {','.join(error_bits)}")
    print()
    print('ALL zGates SHOULE BE XOR (except the final carry)')
    for out,gate in sorted(gates.items()):
        if out.startswith('z') and gate[0] != 'XOR' and out != 'z45':
            for key,val in gates.items():
                test = [('XOR',f'x{out[1:]}',f'y{out[1:]}'),('XOR',f'y{out[1:]}',f'x{out[1:]}')]
                if val in test:
                    print(f"FIND XOR with {key}", end=' THEN ')
                    find_gate = key
                    break
            for key,val in gates.items():
                test = [('XOR',find_gate,f'y{out[1:]}'),('XOR',f'y{out[1:]}',f'x{out[1:]}')]
                if val[0] == 'XOR' and find_gate in val[1:]:
                    system.swap_gates(out,key)
    if options.dbg:
        system.rst()
        while None in system.output:
            system.run()

        part2 = ''.join(reversed([str(i) for i in system.output]))
        error_bits = [str(bit).zfill(2) for bit,vals in enumerate(zip(part2[::-1],expected[2:][::-1])) if vals[0]!=vals[1]]
        #system.print_gates()
        print(f"EXPECTED: {expected}")
        print(f"ACTUAL  : 0b{part2}")
        print(f"ERR BITS: {error_bits}")
    
        print("LOOK AT WIRES")
        for out,gate in sorted(gates.items()):
            if out.startswith('z'):
                print(out, end=': ')
                [print(gates[i],end=' ') if i[0] not in 'xy' else print(wires[i]) for i in gate[1:]]
                print()

    print("FOUND AND GATE ON z11 INPUT", end=' ')
    system.swap_gates('brk','dpd') # every zXX should be OR and XOR pair
    system.rst()
    while None in system.output:
        system.run()
    if options.dbg:
        part2 = ''.join(reversed([str(i) for i in system.output]))
        error_bits = [str(bit).zfill(2) for bit,vals in enumerate(zip(part2[::-1],expected[2:][::-1])) if vals[0]!=vals[1]]
        print(f"EXPECTED: {expected}")
        print(f"ACTUAL  : 0b{part2}")
        print(f"ERR BITS: {error_bits}") if error_bits else print("THE ADDER HAS BEEN FIXED")
    print(f"part2: {','.join(sorted(system.swaps))}")
