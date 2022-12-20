import sys
import io

trees = []

def main():
    f_in = 'task1.txt'
    raw_input = read_input(f_in)
    split = split_input(raw_input)
    input = format_input(split)
    print(input)

    visible_trees = 0
    for x in range(len(trees)):
        for y in range(len(trees[x])):
            if  is_visible(x,y):
                visible_trees += 1

    print (visible_trees)

    return

def is_visible(x,y):
    return is_visible_left(x,y) or is_visible_right(x,y) or is_visible_up(x,y) or is_visible_down(x,y)

# check whether tree is visible from the left
def is_visible_left(x,y):
    if x == 0:
        return True

    for _x in range(x):
        # if the tree is lower than one to the left
        if trees[_x][y] >= trees[x][y]:
            return False

    return True

# check whether tree is visible from the right
def is_visible_right(x,y):
    if x == len(trees):
        return True

    for _x in range(len(trees)):
        # if the tree is lower and to the right of the one we are looking at
        if trees[_x][y] >= trees[x][y] and _x > x:
            return False

    return True

# check whether tree is visible from the top
def is_visible_up(x,y):
    if y == 0:
        return True

    for _y in range(y):
        # if the tree is lower than one above
        if trees[x][_y] >= trees[x][y]:
            return False
    return True

# check whether tree is visible from the bottom
def is_visible_down(x,y):
    if x == len(trees):
        return True

    for _y in range(len(trees[y])):
        # if the tree is lower and above of the one we are looking at
        if trees[x][_y] >= trees[x][y] and _y > y:
            return False
    return True


def format_input(input):
    first_line = input[0]
    for tree in first_line:
        trees.append([])
    print(trees)

    for y in range(len(input)):
        for x in range(len(input[y])):
            trees[x].append(int(input[y][x]))

    return trees


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