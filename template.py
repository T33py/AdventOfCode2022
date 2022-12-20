import sys
import io


def main():
    f_in = 'ex1.txt'
    raw_input = read_input(f_in)
    split = split_input(raw_input)
    input = format_input(split)

    print(split)
    return


def format_input(input):

    return

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