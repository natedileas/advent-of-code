
INPUT = open('input10.txt').read()


TEST1 = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

TEST2 = """
16
10
15
5
1
11
7
19
6
12
4
"""

import math


def combs(blocklen): 
	# return blocklen
	if blocklen == 1:
		return 1

	if blocklen == 2:
		return 2
	if blocklen == 3:
		return 4

	if blocklen == 4:
		return 8

	return sum((math.comb(blocklen, k) for k in range(blocklen + 1)))


def countlist(random_list):
    retlist = []
    count = 1
    for i in range(len(random_list) - 1):
        if random_list[i] == random_list[i+1]:
            count += 1
        else:
            # If it is not append the count and restart counting
            retlist.append((count, random_list[i]))
            count = 1

    # Since we stopped the loop one early append the last count
    retlist.append((count, random_list[-1]))
    return retlist


def total_chances(arr):
	all_chances = []
	for count, item in countlist(arr):
		if item == 1:
			all_chances.append(combs(count))

	print(all_chances)

	return np.prod(np.asarray(all_chances))


if __name__ == '__main__':
	import numpy as np
	arr = np.asarray([int(i) for i in TEST1.splitlines() if i])
	arr = np.append(arr, [0, max(arr) + 3])
	arr.sort()

	df = np.diff(arr)

	print(arr, df)

	print(sum(df == 1), sum(df == 3))

	import itertools
	n_valid = 0
	# for i in range(2, len(arr)):
	# 	print(i)
	# 	for indices in itertools.combinations(list(range(len(arr))), i):
	# 		if np.any(np.diff(arr[np.array(sorted(indices))]) > 3):
	# 			continue
	# 		else:
	# 			n_valid += 1



	print(total_chances(df))
	print(countlist(df))