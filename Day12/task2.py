import sys
import io

elevation_lookup = 'abcdefghijklmnopqrstuvwxyz'
map = []
elevations = []
reaced_in_steps = []
reached = []
todo = []

def main():
	f_in = 'task1.txt'
	raw_input = read_input(f_in)
	split = split_input(raw_input)
	for line in range(len(split)):
		map.append([])
		elevations.append([])
		reaced_in_steps.append([])
		reached.append([])
	for x in range(len(split)):
		for y in range(len(split[x])):
			map[x].append('a')
			elevations[x].append(0)
			reaced_in_steps[x].append(sys.maxsize)
			reached[x].append(0)
	
	print_map(map)
	(start, end) = format_input(split)
	(sx, sy) = start
	(ex, ey) = end

	reaced_in_steps[sx][sy] = 0
	todo.append((start, end))
	for x in range(len(reaced_in_steps)):
		for y in range(len(reaced_in_steps[x])):
			if reaced_in_steps[x][y] == 0:
				todo.append(((x,y), end))

	while len(todo) > 0:
		(s, e) = todo.pop(0)
		traverse(s, e)


	print_map(map)
	print_map(elevations)
	print_map(reaced_in_steps)
	print_map(reached)
	print(f'{(start, end)} in {reaced_in_steps[ex][ey]} steps')
	return

def traverse(start, end):
	(x, y) = start
	reached[x][y] = 1
	my_steps = reaced_in_steps[x][y]
	if start == end:
		return

	# check each neighbour to see if they are reached and reachable (elevation difference <= 1)
	# ← 
	if can_goto(start, (x-1, y)):
		x_ = x - 1
		if reaced_in_steps[x_][y] > my_steps + 1:
			reaced_in_steps[x_][y] = my_steps + 1
			todo.append(((x_,y), end))
	# →
	if can_goto(start, (x+1, y)):
		x_ = x + 1
		if reaced_in_steps[x_][y] > my_steps + 1:
			reaced_in_steps[x_][y] = my_steps + 1
			todo.append(((x_,y), end))
	# ↓
	if can_goto(start, (x, y-1)):
		y_ = y - 1
		if reaced_in_steps[x][y_] > my_steps + 1:
			reaced_in_steps[x][y_] = my_steps + 1
			todo.append(((x,y_), end))
	# ↑
	if can_goto(start, (x, y+1)):
		y_ = y + 1
		if reaced_in_steps[x][y_] > my_steps + 1:
			reaced_in_steps[x][y_] = my_steps + 1
			todo.append(((x,y_), end))

	return

def can_goto(at, to):
	(ax, ay) = at
	(tx, ty) = to

	if not tx >= 0:
		return False
	if not tx < len(map):
		return False
	if not ty >= 0:
		return False
	if not ty < len(map[0]):
		return False
	
	eat = elevations[ax][ay]
	eto = elevations[tx][ty]

	if eat - eto >= -1 :
		return True
	

	return False

def print_map(map):
	print('---------------------------')
	for line in map:
		print(line)
	print('---------------------------')
	return

def format_input(input):
	s = (0, 0)
	e = (0, 0)
	for x in range(len(input)):
		for y in range(len(input[x])):
			elevation = input[x][y]
			if elevation == 'S':
				elevation = 'a'
				s = (x, y)
			elif elevation == 'E':
				elevation = 'z'
				e = (x, y)
			
			elevations[x][y] = elevation_lookup.index(elevation)
			map[x][y] = elevation
			if elevation == 'a':
				reaced_in_steps[x][y] = 0

	return (s, e)

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