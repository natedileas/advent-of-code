TEST1 = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""
import numpy as np
import sys


def find_nonmatching_element(arr, masklen=25):
	# addmat = np.array((len(INPUT), len(INPUT)))
	addmat = arr[:,np.newaxis] + arr 

	for i in range(0, len(arr) - masklen):
		if arr[i+masklen] not in addmat[i:i+masklen,i:i+masklen]:
			return arr[i+masklen]


def find_block_adds(arr, sumval):
	blocklen = 1
	while blocklen < 100:
		blocklen += 1
		for i in range(len(arr) - blocklen):
			if arr[i:i+blocklen].sum() == sumval:
				return arr[i:i+blocklen].min() + arr[i:i+blocklen].max()


def data2arr(data):
	return np.asarray([int(i) for i in data.splitlines() if i])


INPUT9 = open('input9.txt').read()

if __name__ == '__main__':
	print('part 1:', find_nonmatching_element(data2arr(INPUT9)))
	print('part 2:', find_block_adds(data2arr(INPUT9), find_nonmatching_element(data2arr(INPUT9))))
