import os
import sys

day = "Day2"
points = { 'X': 1, 'Y': 2, 'Z': 3 }

results = { 
	('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
	('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
	('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
}

def main():
	f_in = "task1.txt"
	f_out = ""
	print(f'input: {f_in}, output: {f_out}')

	in_filename = os.path.join(day, f'{f_in}')
	out_filename = os.path.join(day, f'{f_out}')

	raw_input = read_file(in_filename)
	strategy_guide = format_input(raw_input)
	my_points = total_points(strategy_guide)
	
	print(f'Strategy guide: {strategy_guide}')
	
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
		strat = val.split(" ")
		strats.append((strat[0], strat[1]))

	return strats


def read_file(filepath:str):
	with open(filepath) as file:
		content = file.read()
	return content

if (__name__ == "__main__"):
	main()