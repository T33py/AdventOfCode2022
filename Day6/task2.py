import sys
import io

message_marker = 14
packet_marker = 4

def main():
    f_in = 'task2.txt'
    raw_input = read_input(f_in)
    split = split_input(raw_input)
    input = format_input(split)
    print(input)
    marker = get_marker(input, message_marker)
    print(marker)


    return


def get_marker(input, marker_length:int):
    marker = 0
    buffer = []

    for char in input:
        buffer.append(char)
        marker += 1
        if len(buffer) > marker_length:
            buffer.pop(0)

        if not contains_duplicate(buffer) and len(buffer) == marker_length:
            return marker

    return None

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