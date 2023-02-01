import os
import sys

def main():
	f_in = "task1.txt"
	f_out = ""
	print(f'input: {f_in}, output: {f_out}')

	dirname = '' # os.path.dirname(__file__)
	in_filename = os.path.join(dirname, f'{f_in}')
	out_filename = os.path.join(dirname, f'{f_out}')

	raw_input = read_file(in_filename)
	calorie_list = format_input(raw_input)
	# print(f'Calorie list: {calorie_list}')
	max_calories = find_top1_calories(calorie_list)
	top3_calories = find_top3_calories(calorie_list)

	print(f'Max calories: {max_calories}')
	print(f'Top 3 calories: {top3_calories}')
	print(f'Top 3 total: {top3_calories[0] + top3_calories[1] + top3_calories[2]}')
	return 

def find_top3_calories(calorie_list):
	top3_calories: list = [0, 0, 0]

	for calories in calorie_list:
		if calories >= top3_calories[0]:
			top3_calories[2] = top3_calories[1]
			top3_calories[1] = top3_calories[0]
			top3_calories[0] = calories
		elif calories >= top3_calories[1]:
			top3_calories[2] = top3_calories[1]
			top3_calories[1] = calories
		elif calories >= top3_calories[2]:
			top3_calories[2] = calories

	return top3_calories

def find_top1_calories(calorie_list):
	max_calories = 0
	for calories in calorie_list:
		if calories > max_calories:
			max_calories = calories
	return max_calories


def format_input(raw_input: str):
	elf_calorie_counts: list = []
	split_input = raw_input.split('\n')

	current_count = 0

	for val in split_input:
		val = val.replace('\r', '')
		if val == '':
			elf_calorie_counts.append(current_count)
			current_count = 0
		else:
			current_count += int(val)

	elf_calorie_counts.append(current_count)
	

	return elf_calorie_counts


def read_file(filepath:str):
	with open(filepath) as file:
		content = file.read()
	return content

if (__name__ == "__main__"):
	main()