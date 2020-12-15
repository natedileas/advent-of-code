INPUT = open('input13.txt').read()

TEST1 = """939
7,13,x,x,59,x,31,19
"""

import numpy as np
import math

def earliest_time_bus(data):
	starttime,busses, = data.splitlines()
	starttime = int(starttime)
	busses = [int(b) for b in busses.split(',') if b != 'x']
	times = [(starttime-((math.ceil(starttime//b)+1)*b),b) for b in busses]

	print(times)
	return max(times, key=lambda i:i[0])

def p1(data):
	t, b = earliest_time_bus(data)
	return abs(t) * b

def p2(data, start=0):
	starttime,busses, = data.splitlines()
	busses = [(i, int(b)) for i, b in enumerate(busses.split(',')) if b != 'x']
	busses = sorted(busses, key=lambda i:i[1], reverse=True)

	print(busses)
	# return
	t = start - busses[0][0]
	while True:
		print('\r', t, end='')
		matches = True
		for i, b in busses:
			matches &= (t + i) % b == 0

		if matches: break
		t += busses[0][1]

	print()
	return t

def gcd_rem(a,b,rem=0):

	m = max(a,b)
	n = min(a,b)
	r = n
	while r != rem:
		n = r
		# print(m, n)
		q = m // n
		r = m % n
		m = n
	
	return n


# 3417
TEST2 = """
17,x,13,19
"""

# 754018
TEST3 = """
67,7,59,61
"""

# 779210
TEST4 = """
67,x,7,59,61
"""

TEST5 = """
67,7,x,59,61
"""

TEST6 = """
1789,37,47,1889
"""

def p2m(t, busses=[17, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 37, 'x', 'x', 'x', 'x', 'x', 439, 'x', 29, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 13, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 23, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 787, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 41, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 19]):
	matches = True
	for i, b in enumerate(busses):
		if b == 'x': 
			continue
		# print(t, b, i, (math.ceil(t/b)), ((math.ceil(t/b))*b) - t == i)
		matches &= ((math.ceil(t/b))*b) - t == i

	if matches: 
		return t	


def p2mm():
	import multiprocessing as mp

	pool = mp.Pool()
	results = pool.imap(p2m, range(99999999999992,10**15,17), chunksize=10**6)

	for ii, i in enumerate(results):
		if i is not None: break
		print('\r', ii, end='')
	print()
	# result = list(filter(None, results))
	return i



if __name__ == '__main__':
	# print(p1(INPUT))
	# print(p1(TEST1))
	# print(p2(TEST1))
	# print(p2(TEST2))
	# print(p2(TEST3))
	# print(p2(TEST4))
	# print(p2(TEST5))
	# print(p2(TEST6))   # 1202161486
	print(p2(INPUT, start=99999999999992))     # 100000000000000
	# print(p2mm())