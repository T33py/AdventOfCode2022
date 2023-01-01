import sys
import io

# task is to approximately simulate rope by moving knots along the length of the rope relative to each other

rope = []
rope_length = 10


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
        print(rope)
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
    print((dir, dist))

    tail_places = []
    while dist > 0:
        move_head((x, y))
        move_rest()
        dist -= 1
        print(rope)
        tail_places.append(rope[len(rope)-1])

    return tail_places

def move_head(move):
    (x, y) = move
    (hx, hy) = rope[0]
    rope[0] = (hx + x, hy + y)
    return


def move_rest():
    knot = 1

    while knot < len(rope):
        # knot we are moving
        (kx, ky) = rope[knot]
        # the previous knot that this knot should move towards
        (hx, hy) = rope[knot -1]

        # delta used to determine how to move
        xDiff = hx - kx
        yDiff = hy - ky
        # print(f'  {knot}={(kx, ky)} -> {(hx, hy)} | dist={(abs(dx), abs(dy))}')

        if abs(xDiff) > 1 or abs(yDiff) > 1:
            if abs(xDiff) > abs(yDiff):
                kx += xDiff - int((xDiff/abs(xDiff)))
                ky = hy
            elif abs(xDiff) < abs(yDiff):
                ky += yDiff - int((yDiff/abs(yDiff)))
                kx = hx
            else:
                kx += xDiff - int((xDiff/abs(xDiff)))
                ky += yDiff - int((yDiff/abs(yDiff)))
            

        
        rope[knot] = (kx, ky)
        knot +=1

    return

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