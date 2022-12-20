import sys
import io


def main():
    f_in = 'task1.txt'
    raw_input = read_input(f_in)
    split = split_input(raw_input)
    input = format_input(split)
    print(input)

    overlaps = []
    idx = 0
    while idx < len(input):
        if (find_overlap(input[idx], input[idx+1])):
            overlaps.append([input[idx], input[idx+1]])
        idx += 2
    
    print(f'overlaps: {len(overlaps)}')
    return

def find_overlap(sections1, sections2):
    if sections1[0] in sections2 and sections1[len(sections1)-1] in sections2:
        return True
    
    if sections2[0] in sections1 and sections2[len(sections2)-1] in sections1:
        return True

    return False

def format_input(input):
    elf_sections = []
    for elf in input:
        sections = []
        section = int(elf.split('-')[0])
        end_section = int(elf.split('-')[1])
        while section <= end_section:
            sections.append(section)
            section += 1

        elf_sections.append(sections)


    return elf_sections 

def split_input(input:str):
    split = input.split('\n')
    split_input = []
    for line in split:
        line = line.replace('\r', '')
        sections = line.split(',')
        for section in sections:
            split_input.append(section)


    return split_input


def read_input(f:str):
    text = None
    with open(f, 'r') as file:
        text = file.read()
        file.close()
    return text

if __name__ == '__main__':
    main()