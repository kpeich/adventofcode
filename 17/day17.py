import optparse

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-d", "--debug", dest="dbg", help="enable debugging", action="store_true", default=False)

    options,args = parser.parse_args()
    '''
    Instructions:
    0: adv : mem[4] // 2**opA -> mem[4]
    1: bxl : mem[5] ^ opA -> mem[5]
    2: bst : mem mod8 -> mem[5]
    3: jnz : nop if regA=0 else ip -> opA (IP not increased by 2)
    4: bxc : mem[5] ^ mem[6] -> mem[5]
    5: out : mem mod8 -> outputs value
    6: bdv : regA // 2*opA -> mem[5]
    7: cdv : regA // 2*opA -> mem[6]
    '''
    class CPU:
        def __init__(self, regA, regB, regC, program, dbg=False, part2=False):
            self.ip = 0
            #regA mem[5] mem[6] are in mem memory
            self.output = []
            self.program = program
            self.mem = {0: 0 , 1: 1, 2: 2, 3: 3, 4: regA, 5: regB, 6: regC, 7: regA}
            self.opcodes = {0: self.adv, 1: self.bxl, 2: self.bst, 3: self.jnz, 4: self.bxc, 5: self.out, 6: self.bdv, 7: self.cdv}
            self.dbg = dbg
            self.part2 = part2
            
        def adv(self):
            #self.mem[4] = self.mem[4] // 2**self.mem[self.program[self.ip+1]]
            self.mem[4] = self.mem[4] >> self.mem[self.program[self.ip+1]]
            self.ip += 2
        def bxl(self):
            self.mem[5] = self.mem[5] ^ self.program[self.ip+1]
            self.ip += 2
        def bst(self):
            self.mem[5] = self.mem[self.program[self.ip+1]] & 7
            self.ip += 2
        def jnz(self):
            if self.mem[4] != 0:
                self.ip = self.program[self.ip+1]
            else: 
                self.ip += 2
        def bxc(self):
            self.mem[5] = self.mem[5] ^ self.mem[6]
            self.ip += 2
        def out(self):
            self.output.append(str(self.mem[self.program[self.ip+1]] & 7))
            # if the program doesn't match, HALT
            if (self.part2) and (int(self.output[-1]) != self.program[len(self.output)-1]):
                self.ip = len(self.program) + 1
            else:
                if self.dbg:
                    print(f"OUT{len(self.output)}: {self.output[-1]}, regA: {self.mem[7]} ({bin(self.mem[7])}) PROG: {self.program[len(self.output)-1]}")
                self.ip += 2
        def bdv(self):
            #self.mem[5] = self.mem[4] // 2**self.mem[self.program[self.ip+1]]
            self.mem[5] = self.mem[4] >> self.mem[self.program[self.ip+1]]
            self.ip += 2
        def cdv(self):
            #self.mem[6] = self.mem[4] // 2**self.mem[self.program[self.ip+1]]
            self.mem[6] = self.mem[4] >> self.mem[self.program[self.ip+1]]
            self.ip += 2
        def run(self):
            if self.dbg and self.part2==False:
                print(f"OP: {self.opcodes[self.program[self.ip]].__name__} LITERAL: {self.program[self.ip+1]} MEM: {self.mem[self.program[self.ip+1]]:08} (MEM%8: {self.mem[self.program[self.ip+1]]%8}) regA: {self.mem[4]} ({bin(self.mem[4])[-3:]}) regB: {self.mem[5]} regC: {self.mem[6]}")
            self.opcodes[self.program[self.ip]]()

#    test1 = (0,0,9,[2,6])
#    test2 = (10,0,0,[5,0,5,1,5,4])
#    test3 = (2024, 0, 0, [0,1,5,4,3,0])
#    test4 = (0,29,0,[1,7])
#    test5 = (0,2024,43690,[4,0])
#    test6 = (729, 0, 0, [0,1,5,4,3,0])
#
#    test1CPU = CPU(test1[0], test1[1], test1[2], test1[3])
#    while (test1CPU.ip < len(test1CPU.program)):
#        test1CPU.run()
#    print(f"Test: {test1CPU.mem[5]} == 1")
#    test2CPU = CPU(test2[0], test2[1], test2[2], test2[3])
#    while (test2CPU.ip < len(test2CPU.program)):
#        test2CPU.run()
#    print(f"Test2: {''.join(test2CPU.output)} == 012")
#    test3CPU = CPU(test3[0], test3[1], test3[2], test3[3])
#    while (test3CPU.ip < len(test3CPU.program)):
#        test3CPU.run()
#    print(f"Test3: {test3CPU.mem[4]} == 0 ; {''.join(test3CPU.output)} == 42567777310")
#    test4CPU = CPU(test4[0], test4[1], test4[2], test4[3])
#    while (test4CPU.ip < len(test4CPU.program)):
#        test4CPU.run()
#    print(f"Test4: {test4CPU.mem[5]} == 26")
#    test5CPU = CPU(test5[0], test5[1], test5[2], test5[3])
#    while (test5CPU.ip < len(test5CPU.program)):
#        test5CPU.run()
#    print(f"Test5: {test5CPU.mem[5]} == 44354")
#    test6CPU = CPU(test6[0], test6[1], test6[2], test6[3])
#    while (test6CPU.ip < len(test6CPU.program)):
#        test6CPU.run()
#    print(f"Test6: {''.join(test6CPU.output)} == 4635635210 ")
#
#
    part1= (48744869, 0, 0, [2,4,1,2,7,5,1,3,4,4,5,5,0,3,3,0])
    part1CPU = CPU(part1[0], part1[1], part1[2], part1[3], dbg=options.dbg)
    while (part1CPU.ip < len(part1CPU.program)):
        part1CPU.run()
    print(f"Part1: {','.join(part1CPU.output)}")

#    test7 = (117440,0,0,[0,3,5,4,3,0])
#    # regA should be 117440
#    test7CPU = CPU(test7[0], test7[1], test7[2], test7[3])
#    while (test7CPU.ip < len(test7CPU.program)):
#        test7CPU.run()
#    print(f"Test7: {test7CPU.output}")

    # find regA such that output = [2,4,1,2,7,5,1,3,4,4,5,5,0,3,3,0]
    chain = [2,4,1,2,7,5,1,3,4,4,5,5,0,3,3,0] # length = 16
    part2 = ''
    done = False

    # MAX 48 bit number (every output needs 3 bits minimum)
    regA = 0
    increment = 0 # power of 2 to increment by (also number of already good bits)
    while (done != True):
        part2CPU = CPU(regA, 0, 0, chain, dbg=options.dbg, part2=True)
        while (part2CPU.ip < len(part2CPU.program)):
            part2CPU.run()
        # 5 numbers =  3 good bits [2:0], increment by 2**3
        # 6 numbers =  6 good bits [5:0], increnemt by 2**6
        # 7 numbers =  9 good bits [9:0], increment by 2**9
        # 8 numbers =  12 good bits [11:0], increment by 2**12
        # 9 numbers =  15 good bits [14:0], increment by 2**15
        # 10 numbers = 18 good bits [17:0], increment by 2**18
        # 11 numbers = 21 good bits [20:0], increment by 2**21
        # 12 numbers = 24 good bits [23:0], increment by 2**24
        # 13 numbers = 27 good bits [26:0], increment by 2**27
        # 14 numbers = 30 good bits [29:0], increment by 2**30
        # 15 numbers = 33 good bits [32:0], increment by 2**33
        # 16 numbers = 36 good bits [35:0], increment by 2**36
        good_bits = 3*(len(part2CPU.output)-5)
        if options.dbg:
            print(f"{regA} num good bits {good_bits}, Part2: {part2} {len(part2)}")
        if ( good_bits > len(part2) ):
            part2 = bin(regA)[-good_bits:]
            #regA = int(8**len(part2CPU.output)) + int(part2, base=2)
            regA = 35184372088832 + int(part2, base=2)
            increment = good_bits
            if options.dbg:
                print(f"LOCKED : {bin(regA)[-good_bits:]}, {part2}, {increment}, {regA}")
            done = len(part2CPU.output) == len(chain)
        regA += int( 2**increment )
    print(f"seed: {part2CPU.mem[7]} OUT: {','.join(part2CPU.output)}")

## Trying a Map but I think I'm done for now
#    bits = ['0' for i in range((3*(16+3)))]  # +3 because the MSB technically needs to be able to look ahead 
#
#    # dependencies for bit sequence (a2,a1,a0)
#    # key : bits in number
#    # val : bit to xor with
#    seqmap = {0: (4,3,2),  # '000' -> (a4,a3,1)
#              1: (5,4,3),  # '001' -> (a5,a4,a3)
#              2: (2,1,0),  # '010' -> (0,0,0)
#              3: (3,2,1),  # '011' -> (a3,1,1)
#              4: (8,7,6),  # '100' -> (!a8,a7,!a6)
#              5: (9,8,7),  # '101' -> (!a9,a8,a7)
#              6: (6,5,4),  # '110' -> (!a6,!a5,!a4)
#              7: (7,6,5) } # '111' -> (!a7,!a6,a5)
#    for idx, num in enumerate(chain[::-1]):
#        bit = 45 - idx
#        print(idx, num)
#        for key,rel_bit in seqmap.items():
#            bin_key = format(key, '03b')
#            bin_key_ints = [int(i) for i in bin_key]
#            
#            msb = bits[bin_key_ints[0]]^bits[rel_bit[0]]
#            middle = bits[bin_key_ints[1]]^bits[rel_bit[1]]
#            lsb = bits[bin_key_ints[2]]^bits[rel_bit[2]]
#            print(msb, type(msb)
#    print(bits)

