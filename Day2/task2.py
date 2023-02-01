import os
import sys

day = "Day2"
points = { 'R': 1, 'P': 2, 'S': 3 }
results = { 
	('A', 'R'): 3, ('A', 'P'): 6, ('A', 'S'): 0,
	('B', 'R'): 0, ('B', 'P'): 3, ('B', 'S'): 6,
	('C', 'R'): 6, ('C', 'P'): 0, ('C', 'S'): 3,
}
choise = {
	('A', 'X'): 'S', ('A', 'Y'): 'R', ('A', 'Z'): 'P',
	('B', 'X'): 'R', ('B', 'Y'): 'P', ('B', 'Z'): 'S',
	('C', 'X'): 'P', ('C', 'Y'): 'S', ('C', 'Z'): 'R',
}

def main():
	f_in = "task1.txt"
	f_out = ""
	print(f'input: {f_in}, output: {f_out}')
	dirname = '' # os.path.dirname(__file__)
	in_filename = os.path.join(f'{dirname}', f'{f_in}')
	out_filename = os.path.join(day, f'{f_out}')

	raw_input = read_file(in_filename)
	strategy_guide = format_input(raw_input)
	my_points = total_points(strategy_guide)
	
	# print(f'Strategy guide: {strategy_guide}')
	
	print(f'Total points: {my_points}')

	return 


def total_points(strategy_guide):
	my_points = 0
	for (opponent, me) in strategy_guide:
		my_points += points[me]
		my_points += results[(opponent, me)]

	return my_points


def format_input(raw_input: str):
	strats: list = []
	split_input = raw_input.split('\n')

	for val in split_input:
		val = val.replace('\r', '')
		val_split = val.split(" ")
		strat = choise[(val_split[0], val_split[1])]
		strats.append((val_split[0], strat))

	return strats


def read_file(filepath:str):
	with open(filepath) as file:
		content = file.read()
	return content

if (__name__ == "__main__"):
	main()