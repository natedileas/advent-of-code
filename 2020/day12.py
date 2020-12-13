
int2dir = {
	0: 'N',
	1: 'W',
	2: 'S',
	3: 'E',
}

def move(loc, instr):
	action = instr[0]
	value = int(instr[1:])

	x, y, d = loc
	if action == 'L':
		d = (d + (value // 90)) % 4
	elif action == 'R':
		d = (d - (value // 90)) % 4
	elif action == 'F':
		action = int2dir[d]

	if action == 'N':
		y += value
	elif action == 'S':
		y -= value
	elif action == 'E':
		x += value
	elif action == 'W':
		x -= value

	newloc = x, y, d
	return newloc

def get_manhattan(data):
	start = (0,0,3)
	pos = start
	for instr in data.splitlines():
		if instr:
			pos = move(pos, instr)
			print(instr,pos)

	return abs(pos[0]) + abs(pos[1])


def move_waypoint(loc, instr):
	action = instr[0]
	value = int(instr[1:])

	wx, wy, x, y = loc
	dx = wx
	dy = wy
	if instr in ('R90', 'L270'):
		wx = -dy
		wy = dx
	elif instr in ('R180', 'L180'):
		wx = -dx
		wy = -dy
	elif instr in ('R270', 'L90'):
		wx = dy
		wy = -dx

	if action == 'F':
		x += wx * value
		y += wy * value
	elif action == 'N':
		wy += value
	elif action == 'S':
		wy -= value
	elif action == 'W':
		wx += value
	elif action == 'E':
		wx -= value

	newloc = wx, wy, x, y
	return newloc

def get_manhattan_2(data):
	start = (-10,1,0,0)
	pos = start
	for instr in data.splitlines():
		if instr:
			pos = move_waypoint(pos, instr)
			print(instr,pos)

	return abs(pos[2]) + abs(pos[3])


TEST1 = """
F10
N3
F7
R90
F11
"""

INPUT = open('input12.txt').read()

if __name__ == '__main__':
	TEST1 = INPUT
	print(get_manhattan(TEST1))   # 1294
	print(get_manhattan_2(TEST1))   # 