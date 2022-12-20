import sys
import io


def main():
    f_in = 'task1.txt'
    raw_input = read_input(f_in)
    split = split_input(raw_input)
    input = format_input(split)
    print(input)
    marker = get_start_marker(input)
    print(marker)


    return


def get_start_marker(input):
    marker = 0
    buffer = []

    for char in input:
        buffer.append(char)
        marker += 1
        if len(buffer) > 4:
            buffer.pop(0)
        if not contains_duplicate(buffer) and len(buffer) == 4:
            return marker

    return marker

def contains_duplicate(input):
    for i in range(len(input)):
        for j in range(len(input)):
            if i != j and input[i] == input[j]:
                return True
    return False

def format_input(input):
    
    return input[0]

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