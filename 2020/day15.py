import numpy as np
import re
import itertools as it

INPUT = "0,14,1,3,7,9"
TEST1 = "0,3,6"

def findright(l, e):
	for i, ee in enumerate(l[::-1]):
		if ee == e:
			return len(l) - i


def memgame(startdata, end=2020):

	numbers = [int(i) for i in startdata.split(",") if i]

	i = len(numbers)
	while i < end:
		lastnum = numbers[-1]

		if lastnum not in numbers[:-1]:
			# print(0)
			numbers.append(0)
			print(i, 0)
		else:
			nextnum = i - findright(numbers[:-1], lastnum)
			print(i, nextnum)
			numbers.append(nextnum)
		
		i += 1

	# print(numbers)
	return numbers


def memgame_big(startdata, target=30000000):

	numbers = [int(i) for i in startdata.split(",") if i]

	lasttime = {n:i for i, n in enumerate(numbers[:-1])}

	# for i, n in enumerate(numbers):
	# 	print(i, n)

	# print(lasttime)

	lastnum = numbers[-1]
	for i in range(len(numbers)-1, target-1):
		if i % 10**4 == 0: print('\r', i, end='') 
		# print(i, lastnum, lasttime)
		if lastnum not in lasttime:
			lasttime[lastnum] = i
			lastnum = 0
		else:
			lastidx = lasttime[lastnum]
			lasttime[lastnum] = i
			lastnum = i - lastidx
		
		# i += 1

	print()
	return lastnum


if __name__ == '__main__':
	# memgame(TEST1)
	# print('end', memgame(TEST1, 10))
	# print('end', memgame(TEST1, 2020))
	# print('end', memgame(INPUT, 2020))
	print('end', memgame_big(INPUT), 175594)