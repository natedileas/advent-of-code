import itertools


def testPassword(p):
	def computeBlocks(passw):
		blocklens = []
		for i, g in itertools.groupby(passw):

			blocklens.append(sum(1 for _ in g))

		return 2 in blocklens

	p = str(p)
	for i in range(len(p)-1):
		if p[i+1] < p[i]: 
			return False

	return computeBlocks(p)


if __name__=='__main__':

	print(testPassword(111111) == True)
	print(testPassword(223450) == False)
	print(testPassword(123789) == False)
	print(testPassword(112233) == True)
	print(testPassword(123444) == False)
	print(testPassword(111122) == True)

	valid = 0
	for passw in range(183564,657474):
		if testPassword(passw): valid += 1

	print(valid)