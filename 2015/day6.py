import re

import numpy as np

def instr_to_slice(instr):
	match = re.fullmatch(r'(turn on|turn off|toggle) (\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})', instr)

	mode, y, x, yy, xx = match.groups()

	return mode, int(y), int(x), int(yy)+1, int(xx)+1

def procinstr(map, instr):
	mode,y,x,yy,xx = instr_to_slice(instr)

	if mode == 'turn on':
		map[y:yy,x:xx] = 1
	elif mode == 'turn off':
		map[y:yy,x:xx] = 0
	else:
		map[y:yy,x:xx] = 1 - map[y:yy,x:xx]

	return map

def procinstr2(map, instr):
	mode,y,x,yy,xx = instr_to_slice(instr)

	if mode == 'turn on':
		map[y:yy,x:xx] += 1
	elif mode == 'turn off':
		map[y:yy,x:xx] -= 1
		map = np.clip(map, 0, np.inf)
	else:
		map[y:yy,x:xx] += 2

	return map

if __name__ == '__main__':
	
	map = np.zeros((1000,1000))
	for instr in open('input6.txt').read().splitlines():
		map = procinstr(map, instr)

	print(map.sum())


	map = np.zeros((1000,1000), dtype=float)
	for instr in open('input6.txt').read().splitlines():
		map = procinstr2(map, instr)

	print(map.sum())
