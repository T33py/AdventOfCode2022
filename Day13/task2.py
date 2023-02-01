import sys
import io
import random


def main():
	f_in = 'task1.txt'
	raw_input = read_input(f_in)
	split = split_input(raw_input)
	packets = format_input(split)
	div_2 = [[2]]
	div_6 = [[6]]
	packets.append(div_2)
	packets.append(div_6)

	sorted = sort(packets)
	decoder_key = (sorted.index(div_2)+1) * (sorted.index(div_6)+1)

	for pack in sorted:
		print(pack)
	print()
	print(decoder_key)

	return

def sort(packets):
	if len(packets) <= 1: return packets

	smaller = []
	larger = []

	pivot = packets[random.randint(0, len(packets)-1)]

	for packet in packets:
		if compare_lists(pivot, packet):
			larger.append(packet)
		else:
			smaller.append(packet)
	smaller.remove(pivot)

	sorted = []
	for small in sort(smaller):
		sorted.append(small)
	sorted.append(pivot)
	for large in sort(larger):
		sorted.append(large)

	return sorted


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