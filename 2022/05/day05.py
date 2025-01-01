from pathlib import Path
import re

testdata = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

def parse(filename):
    file = Path(__file__).parent / filename
    stacks, commands = (file.read_text().split('\n\n'))
    stacklist = [[stack[i+1:i+2] for i in range(0, len(stack), 4)] for stack in stacks.split('\n')[:-1]]

    stackQueues = [[] for i in range(len(stacklist[0]))]
    for stack in reversed(stacklist):
        for idx,crate in enumerate(stack):
            if crate != ' ':
                stackQueues[idx].append(crate)

    commands = [[int(i) for i in re.findall(r"(\d+)",command)] for command in commands.split('\n')[:-1]]
    
    return stackQueues, commands



def pt1(stacks, commands):
    for command in commands:
        print(f"move {command[0]} from {command[1]} to {command[2]}")
        for i in range(int(command[0])):
            stacks[command[2]-1].append(stacks[command[1]-1].pop())

    return ''.join([stack[-1] for stack in stacks])

def pt2(stacks, commands):
    for command in commands:
        print(f"move {command[0]} from {command[1]} to {command[2]}")
        temp = []
        for i in range(int(command[0])):
            temp.append(stacks[command[1]-1].pop())
        stacks[command[2]-1] += temp[::-1]

    return ''.join([stack[-1] for stack in stacks])

if __name__ == '__main__':
    stacks, commands = (testdata.split('\n\n'))
    stacklist = [[stack[i+1:i+2] for i in range(0, len(stack), 4)] for stack in stacks.split('\n')[:-1]]

    stackQueues = [[] for i in range(len(stacklist[0]))]
    for stack in reversed(stacklist):
        for idx,crate in enumerate(stack):
            if crate != ' ':
                stackQueues[idx].append(crate)

    tcommands = [[int(i) for i in re.findall(r"(\d+)",command)] for command in commands.split('\n')[:-1]]

    print(f"TEST: {pt1(stackQueues, tcommands)}")

    stacksQ, commands = parse('input.txt')
    print(pt1(stacksQ, commands))
    
    stacks, commands = (testdata.split('\n\n'))
    stacklist = [[stack[i+1:i+2] for i in range(0, len(stack), 4)] for stack in stacks.split('\n')[:-1]]

    stackQueues = [[] for i in range(len(stacklist[0]))]
    for stack in reversed(stacklist):
        for idx,crate in enumerate(stack):
            if crate != ' ':
                stackQueues[idx].append(crate)

    stacksQ, commands = parse('input.txt')
    print(f"TEST: {pt2(stackQueues, tcommands)}")
    print(pt2(stacksQ, commands))
