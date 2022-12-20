import sys
import io
from terminal import terminal
from fs import file
from fs import directory

device = terminal()

# 1540861

def main():
    f_in = 'task2.txt'
    raw_input = read_input(f_in)
    split = split_input(raw_input)
    input = format_input(split)
    print(input)

    for line in input:
        if device.is_command(line):
            device.execute_command(line)
        elif line.split(' ')[0] == 'dir':
            device.create_dir(line.split(' ')[1])
        else:
            device.create_file(line.split(' ')[1], int(line.split(' ')[0]))

    print(f'\n setup done\n')
    device.execute_command('cd /')
    base_directory = device.current_directory
    device.execute_command('tree')

    sizes = {}
    find_total_sizes_of_each_subdir(base_directory, '', sizes)
    print(sizes)
    total_space = 70000000
    space_needed = 30000000
    total_used = sizes['/']
    total_free = total_space - total_used
    print (f'total free: {total_free}')

    dir_to_delete = None
    for dir in sizes:
        if total_free + sizes[dir] > space_needed:
            if dir_to_delete is None:
                dir_to_delete = dir
            elif sizes[dir] < sizes[dir_to_delete]:
                dir_to_delete = dir
    print(f'delete {dir_to_delete} {sizes[dir_to_delete]}')

    return

def find_total_sizes_of_each_subdir(dir:directory, chain:str, sizes):
    sizes[chain+dir.name] = total_size(dir)

    for subdir in dir.directories:
        find_total_sizes_of_each_subdir(subdir, f'{chain}{dir.name}/', sizes)

    return sizes

def total_size(dir:directory):
    total = 0

    for file in dir.files:
        total += file.size
    for subdir in dir.directories:
        total += total_size(subdir)

    return total


def format_input(input):

    return input

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