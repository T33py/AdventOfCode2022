import sys
import io


def main():
	f_in = 'task1.txt'
	raw_input = read_input(f_in)
	split = split_input(raw_input)
	monkeys = format_input(split)

	for round in range(20):
		print(f'---Round {round}---')
		for monkey in monkeys:
			throw_things(monkey, monkeys)
		for monkey in monkeys:
			print_monkey(monkey)
			
	# find top 2 monkeys in terms of inspections
	throws = [0, 0]
	for monkey in monkeys:
		inspections = int(monkey['inspections'])
		if inspections > throws[0]:
			throws[1] = throws[0]
			throws[0] = inspections
		elif inspections > throws[1]:
			throws[1] = inspections

	print(f'monkeybusiness = { throws[0] * throws[1]}')

	return

def throw_things(monkey, monkeys):
	if len(monkey['items']) == 0:
		return

	for item in monkey['items'].split(', '):
		monkey['inspections'] = str(int(monkey['inspections'])+1)
		worry_level = calculate_new_worry_level(monkey['operation'] ,int(item))
		worry_level = int(worry_level / 3)
		if worry_level % int(monkey['test']) == 0:
			# print('monkey ' + monkey['number'] + ' throws ' + str(worry_level) + ' to ' + monkey[True])
			throw_to_monkey(worry_level, monkey[True], monkeys)
		else:
			# print('monkey ' + monkey['number'] + ' throws ' + str(worry_level) + ' to ' + monkey[False])
			throw_to_monkey(worry_level, monkey[False], monkeys)
		
	monkey['items'] = ''
	return worry_level

def calculate_new_worry_level(operation, worry):
	op = operation.split(' ')
	operation = op[len(op)-2]
	operand = op[len(op)-1]
	
	if operand == 'old':
		operand = str(worry)

	if operation == '*':
		worry = worry * int(operand)
	elif operation == '+':
		worry = worry + int(operand)

	return worry

def throw_to_monkey(item, throw_to, monkeys):
	for monkey in monkeys:
		if throw_to == monkey['number']:
			if len(monkey['items'])>0: 
				monkey['items'] = monkey['items'] + ', '
			monkey['items'] = monkey['items'] + str(item)
	return

def print_monkey(monkey):
	print('Monkey '+ monkey['number'] + ': ' + monkey['items'])
	return

def format_input(input):
	monkeys = []
	monkey = {}
	for line in input:
		print(line)
		if 'Monkey' in line:
			monkey = {}
			monkeys.append(monkey)
			monkey['number'] = line.split(' ')[1].replace(':', '')
			monkey['inspections'] = '0'
			print('Monkey '+ monkey['number'])
		if 'Starting items:' in line:
			items_str = line.split(': ')[1]
			monkey['items'] = items_str
			print('  items: ' + monkey['items'])
		if 'Operation:' in line:
			operation = line.split(': ')[1]
			monkey['operation'] = operation
			print('  operation: ' + monkey['operation'])
		if 'Test:' in line:
			test = line.split(': ')[1].split(' ')
			monkey['test'] = test[len(test)-1]
			print('  test: ' + monkey['test'])
		if 'If true:' in line:
			on_true = line.split(' ')
			monkey[True] = on_true[len(on_true) - 1]
			print('    true: ' + monkey[True])
		if 'If false:' in line:
			on_false = line.split(' ')
			monkey[False] = on_false[len(on_false) - 1]
			print('    false: ' + monkey[False])

	return monkeys

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