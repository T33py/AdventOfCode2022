import sys
import io

cycle = 1
executing = []

def main():
    global cycle
    f_in = 'task1.txt'
    raw_input = read_input(f_in)
    split = split_input(raw_input)
    instructions = format_input(split)

    for instruction in instructions:
        (command, args) = instruction
        if command == 'addx':
            executing.append((instruction, cycle+2))
            cycle += 2
        else:
            executing.append((instruction, cycle+1))
            cycle += 1

    print(executing)
    
    for i in range(7):
        print(f'cycle {i}: x={x_at_cycle(i)}')

    x20 = x_at_cycle(20) * 20
    x60 = x_at_cycle(60) * 60
    x100 = x_at_cycle(100) * 100
    x140 = x_at_cycle(140) * 140
    x180 = x_at_cycle(180) * 180
    x220 = x_at_cycle(220) * 220
    print(f'x at: 20: {x20}, 60: {x60}, 100:{x100}, 140:{x140}, 180:{x180}, 220:{x220}')
    print(x20+x60+x100+x140+x180+x220)
    return

def x_at_cycle(cycle:int):
    x = 1

    for ((command, arg), cycle_completed) in executing:
        if cycle_completed <= cycle:
            if command == 'addx':
                x += arg

    return x

def format_input(input):
    instructions = []
    for instruction in input:
        if 'addx' in instruction:
            split = instruction.split(' ')
            instructions.append((split[0], int(split[1])))
        else:
            instructions.append((instruction, ''))

    return instructions

def split_input(input:str):
    split = input.split('\n')
    split_input = []
    for line in split:
        line = line.replace('\r', '')
        split_input.append(line)

    return split_input


def read_input(f:str):
    text = None
    with open(f, 'r') as file:
        text = file.read()
        file.close()
    return text

if __name__ == '__main__':
    main()