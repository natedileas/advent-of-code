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

if __name__ == '__main__':
	INPUT = np.asarray([int(i) for i in open('input9.txt').read().splitlines() if i])
	# INPUT = np.asarray([int(i) for i in TEST1.splitlines() if i])
	print(INPUT)

	addmat = np.array((len(INPUT), len(INPUT)))
	addmat = INPUT[:,np.newaxis] + INPUT 

	print(addmat)

	masklen = 25
	for i in range(0, len(INPUT) - masklen):
		if INPUT[i+masklen] not in addmat[i:i+masklen,i:i+masklen]:
			print (i, INPUT[i+masklen])
			break

	target = 15690279
	blocklen = 0
	while blocklen < 100:
		blocklen += 1
		for i in range(len(INPUT) - blocklen):
			if sum(INPUT[i:i+blocklen]) == target:
				print(i, blocklen, INPUT[i:i+blocklen].min() + INPUT[i:i+blocklen].max())
				break
				sys.exit(0)