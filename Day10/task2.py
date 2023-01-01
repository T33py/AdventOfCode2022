import sys
import io

cycle = 1
executing = []

crt = []

def main():
    global cycle
    f_in = 'task1.txt'
    raw_input = read_input(f_in)
    split = split_input(raw_input)
    instructions = format_input(split)
    
    for i in range(6):
        row = []
        crt.append(row)
        for j in range(40):
            row.append('.')

    for instruction in instructions:
        (command, args) = instruction
        if command == 'addx':
            executing.append((instruction, cycle+2))
            cycle += 2
        else:
            executing.append((instruction, cycle+1))
            cycle += 1


    # draw crt
    row = [] # placeholder
    for c in range(240):
        if c < 40: row = crt[0]
        elif c < 80: row = crt[1]
        elif c < 120: row = crt[2]
        elif c < 160: row = crt[3]
        elif c < 200: row = crt[4]
        else: row = crt[5]

        pixel = c%40
        x = x_at_cycle(c+1) # cycles 1-index
        sprite = [x-1, x, x+1]
        if pixel in sprite:
            row[pixel] = '#'

        
    # print the crt
    for line in crt:
        prt = ''
        for char in line:
            prt = prt + char
        print(prt)

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