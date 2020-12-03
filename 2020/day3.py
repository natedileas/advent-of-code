from functools import reduce

def check_slope(slope, lines):
	nlines = len(lines)
	lenlines = len(lines[0])

	y = 0
	x = 0
	ntrees = 0
	while y < len(lines) - 1:
		x = (x + slope[0]) % lenlines
		y += slope[1]
		ntrees += int(lines[y][x] == '#')

	return ntrees

with open('test3.txt', 'r') as f:
	test3lines = f.read().splitlines()

with open('input3.txt', 'r') as f:
	input3lines = f.read().splitlines()

print('Part 1 Test:', check_slope((3,1), test3lines), '==', 7)
print('Part 1 Test:', check_slope((3,1), input3lines), '==', 250)

p2t = [check_slope(slope, test3lines) for slope in ((1,1), (3,1), (5,1), (7,1), (1,2))]
print('Part 2 test: ', p2t, reduce(lambda a,b:a*b, p2t), '== [2, 7, 3, 4, 2], 366')
p2 = [check_slope(slope, input3lines) for slope in ((1,1), (3,1), (5,1), (7,1), (1,2))]
print('Part 2 test: ', reduce(lambda a,b:a*b, p2), '== 1592662500')
