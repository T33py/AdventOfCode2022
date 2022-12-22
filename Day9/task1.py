import sys
import io

grid = []
global head
head = (0, 0)
global tail
tail = (0, 0)


def main():
    f_in = 'task1.txt'
    raw_input = read_input(f_in)
    split = split_input(raw_input)
    input = format_input(split)
    print(input)

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
    global tail
    (dir, dist) = move
    # direction
    (x, y) = (0, 0)
    if dir == 'R':
        x = 1
    elif dir == 'L':
        x = -1
    elif dir == 'U':
        y = 1
    elif dir == 'D':
        y = -1

    (hx, hy) = head
    (tx, ty) = tail
    tail_places = []
    for step in range(dist):
        hx += x
        hy += y
        if abs(tx - hx) > 1 or abs(ty - hy) > 1:
            tx = hx-x
            ty = hy-y
        tail_places.append((tx, ty))
        # print(f'H: {(hx, hy)}, T: {(tx, ty)}')

    head = (hx, hy)
    tail = (tx, ty)
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