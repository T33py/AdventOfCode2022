import sys
import io

rope = []
rope_length = 10
global head
global tail


def main():
    f_in = 'task1.txt'
    raw_input = read_input(f_in)
    split = split_input(raw_input)
    input = format_input(split)
    print(input)

    for i in range(rope_length):
        rope.append((0,0))
    
    

    all_tail_places = {}
    unique_tail_places = 0
    for move in input:
        tail_places = move_rope(move)
        for place in tail_places:
            if place in all_tail_places:
                all_tail_places[place] += 1
            else:
                all_tail_places[place] = 1
                unique_tail_places += 1

    print(all_tail_places)
    print(unique_tail_places)
    return


def move_rope(move):
    global head
    return tail_places

def format_input(input):
    moves = []
    for move in input:
        split = move.split(' ')
        moves.append((split[0], int(split[1])))
    return moves

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