import sys
import io
import re

def main():
	f_in = 'task1.txt'
	raw_input = read_input(f_in)
	split = split_input(raw_input)
	(grid, sensors) = format_input(split)

	# for sensor in sensors:
	# 	draw_manhattan_exclusion(grid, sensor)
	# print(display_grid(grid, (475, 550, 475, 525)))

	x_low = -2590982
	x_high = 25916996
	y_level = 2000000
	excluded_squares = 0
	for x in range(x_low, x_high):
		for sensor in sensors:
			if is_beacon(sensors, x, y_level):
				break
			if covers_square(sensor, x, y_level):
				excluded_squares += 1
				break
	# for x in range(-500, 500):
	# 	if grid_get(grid, x, 10) not in ['.', 'B']:
	# 		excluded_squares += 1

	print(excluded_squares)
	return

def is_beacon(sensors, x, y):
	for sensor in sensors:
		(sx, sy, bx, by) = sensor
		if x == bx and y == by:
			return True
	return False

def covers_square(sensor, x, y):
	(sx, sy, bx, by) = sensor
	md = abs(sx - bx) + abs(sy - by)
	
	# (x_low, x_high) = (sx - md, sx + md)
	# (y_low, y_high) = (sy - md, sy + md)

	# if in range
	if abs(y - sy) + abs(x - sx) <= md:
		return True


	return False

def draw_manhattan_exclusion(grid, sensor):
	(sx, sy, bx, by) = sensor
	md = abs(sx - bx) + abs(sy - by)

	for dx in range(-md, md+1):
		for dy in range(-md + abs(dx), md+1 - abs(dx)):
			if grid_get(grid, sx+dx, sy+dy) == '.':
				grid_set(grid, sx+dx, sy+dy, '#')

	return

# grid will be offset to account for negative coordinates - use getter setter
def format_input(input):
	# grid = []
	sensors = []
	# for i in range(1001):
	# 	grid.append([])
	# 	for j in range(1001):
	# 		grid[i].append('.')
	
	for sensor in input:
		[s, b] = sensor.split(':')
		sx = int(re.findall(r'x=(-?\d+)', s)[0])
		sy = int(re.findall(r'y=(-?\d+)', s)[0])
		bx = int(re.findall(r'x=(-?\d+)', b)[0])
		by = int(re.findall(r'y=(-?\d+)', b)[0])
		# grid_set(grid, sx, sy, 'S')
		# grid_set(grid, bx, by, 'B')
		sensors.append((sx,sy,bx,by))


	return ('grid', sensors)

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

def grid_get(grid, x, y):
	return grid[x+500][y+500]

def grid_set(grid, x, y, val):
	grid[x+500][y+500] = val
	return

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