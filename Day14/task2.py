import sys
import io


def main():
	f_in = 'task1.txt'
	raw_input = read_input(f_in)
	split = split_input(raw_input)
	slice = format_input(split)
	slice[500][0] = '+'
	print(display_grid(slice, (480,520,0,25)))

	(sx, sy) = (500, 0)
	resting_grains = 0
	sand_can_rest = True

	while sand_can_rest:
		(resting, nx, ny) = move_sand(slice, sx, sy)
		if resting is None:
			print('dropped one')
			break
		if resting:
			resting_grains += 1
			if nx == 500 and ny == 0:
				break
			sx = 500
			sy = 0
		else:
			sx = nx
			sy = ny

		slice[500][0] = '+'
	
	print(display_grid(slice, (0,999,0,180)))
	print(f'resting grains: {resting_grains}')

	return

# returns (<resting>, new_x, new_y) if the sand is in the grid
# returns (None, 0, 0) if the sand fell out of the grid
def move_sand(grid, x, y):
	if y+1 >= len(grid[x]):
		return (None, 0, 0)

	if grid[x][y+1] == '.':
		grid[x][y+1] = 'o'
		grid[x][y] = '.'
		return (False, x, y+1)
	elif grid[x-1][y+1] == '.':
		grid[x-1][y+1] = 'o'
		grid[x][y] = '.'
		return (False, x-1, y+1)
	elif grid[x+1][y+1] == '.':
		grid[x+1][y+1] = 'o'
		grid[x][y] = '.'
		return (False, x+1, y+1)
	
	return (True, x, y)

def display_grid(grid, window):
	display = ''
	(low_x, high_x, low_y, high_y) = window

	for y in range(len(grid[0])):
		for x in range(len(grid)):
			if x >= low_x and x <= high_x and y >= low_y and y <= high_y:
				display = display + grid[x][y]
				if x == high_x:
					display = display + '\n'

	return display

def format_input(input):
	grid = []
	for i in range(1000):
		grid.append([])
		for j in range(1000):
			grid[i].append('.')
	

	for rock in input:
		coords = rock.replace(' ', '').split('->')
		for i in range(len(coords)):
			coords[i] = coords[i].split(',')
		for i in range(len(coords)-1):
			(at_x, at_y) = (int(coords[i][0]),int(coords[i][1]))
			(to_x, to_y) = (int(coords[i+1][0]), int(coords[i+1][1]))

			print(f'({at_x},{at_y}) -> ({to_x},{to_y})')
			step_x = 1
			step_y = 1
			if at_x - to_x < 0:
				step_x = -1
			if at_y - to_y < 0:
				step_y = -1

			for x in range(0, at_x - to_x, step_x):
				grid[at_x - x][at_y] = '#'
				# print(f'mv x: {at_x - x},{at_y}')
			for y in range(0, at_y - to_y, step_y):
				grid[at_x][at_y - y] = '#'
				# print(f'mv y: {at_x}{at_y - y}')
			grid[to_x][to_y] = '#'

	floor = 1000
	for y in range(999, -1, -1):
		for x in range(len(grid)):
			if grid[x][y] != '.':
				floor = y+2
				break
		if floor != 1000:
			break
	for x in range(len(grid)):
		grid[x][floor] = '#'

	return grid

def split_input(input:str):
	split = input.split('\n')
	split_input = []
	for line in split:
		line = line.replace('\r', '')
		if line != '':
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