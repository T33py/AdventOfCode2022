import sys
import io


def main():
	f_in = 'task1.txt'
	raw_input = read_input(f_in)
	split = split_input(raw_input)
	input = format_input(split)

	i = 0
	p = 1
	sum_of_correct_pairs = 0
	while i < len(input):
		left = input[i]
		right = input[i+1]
		cmp = compare_lists(left, right)

		print(f'pair{p} ordered: {cmp} | {left} : {right}')

		if cmp:
			sum_of_correct_pairs += p

		i += 2
		p += 1

	print(sum_of_correct_pairs)

	return

# Reading is hard.. just hardcode each sentence of the comparison and it works..
def compare_lists(left:list, right:list):
	# no items in left but items in right
	if len(left) == 0 and len(right) > 0:
		return True

	for i in range(len(left)):
		# right ran out
		if len(right) <= i: 
			return False

		lft = left[i]
		rgt = right[i]
		if isinstance(lft, int) and isinstance(rgt, int):
			if lft < rgt: return True
			if lft > rgt: return False
		elif isinstance(lft, list) and isinstance(rgt, list):
			cmp = compare_lists(lft, rgt)
			if cmp in [True, False]: return cmp
		elif isinstance(lft, int):
			cmp = compare_lists([lft], rgt)
			if cmp in [True, False]: return cmp
		else:
			cmp = compare_lists(lft, [rgt])
			if cmp in [True, False]: return cmp

		
		# left ran out and there is more items in the right one
		if len(left) == i + 1 and len(right) != len(left):
			return True

	return None

def format_input(input):
	output = []
	for line in input:
		if line != '':
			output.append(eval(line))
	return output

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