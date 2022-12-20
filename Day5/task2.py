import sys
import io


def main():
    f_in = 'task2.txt'
    raw_input = read_input(f_in)
    split = split_input(raw_input)
    # crates is {} of 1 indexed stacks
    # stacks is # of stacks
    # steps is (move, from, to)
    (crates, stacks, steps) = format_input(split)

    print(f'{crates},\n {stacks},\n {steps}')
    for step in steps:
        move_crates(crates, step)

    print_top_crates(crates)
    return

def print_crates(crates):
    print(crates)
    return

def print_top_crates(crates):
    top_crates = ''
    for stack in crates:
        top_crates = top_crates + crates[stack][len(crates[stack])-1]
    top_crates = top_crates.replace('[', '').replace(']','')
    print(top_crates)
    return


def move_crates(crates, step):
    (move_, from_, to_) = step
    crates_moving = []
    for number in range(int(move_)):
        stack_from = crates[int(from_)]
        stack_to = crates[int(to_)]
        crate = stack_from.pop(len(stack_from)-1)
        crates_moving.insert(0, crate)
    for crate in crates_moving:
        stack_to.append(crate)
    return crates


def format_input(input):
    crate_lines = []
    step_lines = []
    crates_done = False

    for line in input:
        if not crates_done:
            crate_lines.append(line)
            # we want to include the line with stack count
            if not '[' in line:
                crates_done = True
        else:
            if len(line)> 0:
                step_lines.append(line)

    stacks_line = crate_lines.pop(len(crate_lines)-1)
    stacks = 0
    stacks_split = stacks_line.split(' ')
    for thing in stacks_split:
        if thing != '':
            stacks = int(thing)
    
    crates = {}
    for line in range(stacks):
        crates[line+1] = []

    crate_lines = reversed(crate_lines)
    for line in crate_lines:
        for stack in range(stacks):
            crate = line[stack*4:stack*4+4].replace(' ', '')
            if len(crate) > 0:
                crates[stack+1].append(crate)

    steps = []
    for line in step_lines:
        info = line.split(' ')
        steps.append((info[1], info[3], info[5]))

    return (crates, stacks, steps)

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