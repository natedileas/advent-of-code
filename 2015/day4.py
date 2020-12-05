import hashlib

def p1(key='iwrupvqb', maxi=10**8):
	i = 0
	print()
	while True:
		print('\r', i, end='')
		md5 = hashlib.md5()
		md5.update((key + str(i)).encode())
		digest = md5.hexdigest()
		if digest.startswith('00000'):
			break
		elif i > maxi:
			break
		i += 1

	print()

	return i

def p2(key='iwrupvqb', maxi=10**8):
	i = 346386
	print()
	while True:
		print('\r', i, end='')
		md5 = hashlib.md5()
		md5.update((key + str(i)).encode())
		digest = md5.hexdigest()
		if digest.startswith('000000'):
			break
		elif i > maxi:
			break
		i += 1

	print()

	return i

def p2m(n, key='iwrupvqb'):
	md5 = hashlib.md5()
	md5.update((key + str(n)).encode())
	digest = md5.hexdigest()
	return n if digest.startswith('000000') else None

def p2mm():
	import multiprocessing as mp

	pool = mp.Pool()
	results = pool.imap(p2m, range(300000,10**7), chunksize=10**5)
	result = list(filter(None, results))
	return result

if __name__ == '__main__':
	# print(p1('abcdef'))
	# print(p1())
	print(p2mm())
	# print(p2())

