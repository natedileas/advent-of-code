

def lookandsay(start):
	nums = [int(i) for i in start] + [None]
	outnums = []

	currnum = None
	count = 0
	for n in nums:
		if n != currnum:
			if currnum is not None:
				outnums.append(count)
				outnums.append(currnum)
				count = 0

			currnum = n

		count += 1

	return ''.join((str(s) for s in outnums))


def iter_looknsay(start, n_iter):
	old = start
	for i in range(n_iter):
		new = lookandsay(old)
		# print(old, new)
		old = new

	return old

if __name__ == '__main__':
	print('test 1:', iter_looknsay('1', 5))
	print('part 1:', len(iter_looknsay('1113122113', 40)))
	print('part 2:', len(iter_looknsay('1113122113', 50)))