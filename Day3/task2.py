import sys
import io

item_checknumbers = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    f_in = 'ex1.txt'
    raw_input = read_input(f_in)
    split = split_input(raw_input)
    input = format_input(split)
    group_items = []

    print(f'groups: {input}')

    for group in input:
        group_items.append(find_group_item(group))

    print(f'group items: {group_items}')

    checksum = 0
    for item in group_items:
        # numbers are not zeroindexed
        checksum += item_checknumbers.index(item) + 1 

    print(f'checksum: {checksum}')

    return

def find_group_item(group):
    for item in group[0]:
        if item in group[1] and item in group[2]:
            return item

    return None

def format_input(input):
    sets = []
    current_set = []
    
    for rucksack in input:
        current_set.append(rucksack)
        if len(current_set) == 3:
            sets.append(current_set)
            current_set = []
        
    return sets

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