import sys
import io

trees = []

def main():
    f_in = 'task1.txt'
    raw_input = read_input(f_in)
    split = split_input(raw_input)
    input = format_input(split)
    print(input)

    top_score = 0
    for x in range(len(trees)):
        for y in range(len(trees[x])):
            score = scenic_score(x,y)
            if score > top_score:
                top_score = score

    print (top_score)

    return

def scenic_score(x,y):
    # print(f'tree [{x},{y}]')
    l = score_left(x,y)
    r = score_right(x,y)
    u = score_up(x,y)
    d = score_down(x,y)
    # print(f'  left: {l}')
    # print(f' right: {r}')
    # print(f'    up: {u}')
    # print(f'  down: {d}')
    return l * r * u * d

# score the tree from the left
def score_left(x,y):
    if x == 0:
        return 0
    score = 0
    

    for _x in range(x-1, -1, -1):
        if trees[_x][y] < trees[x][y]:
            score += 1
        else: 
            score += 1
            break

    return score

# score the tree from the right
def score_right(x,y):
    if x == len(trees):
        return 0
    score = 0

    for _x in range(x+1, len(trees)):
        if trees[_x][y] < trees[x][y]:
            score += 1
        else: 
            score += 1
            break

    return score 

# score the tree from the top
def score_up(x,y):
    if y == 0:
        return 0
    score = 0

    for _y in range(y-1, -1, -1):
        if trees[x][_y] < trees[x][y]:
            score += 1
        else: 
            score += 1
            break
    return score

# score the tree from the bottom
def score_down(x,y):
    if y == len(trees):
        return 0
    score = 0

    for _y in range(y+1, len(trees[y])):
        if trees[x][_y] < trees[x][y]:
            score += 1
        else: 
            score += 1
            break
    return score


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