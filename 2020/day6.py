from functools import reduce

if __name__ == '__main__':
	data = open('input6.txt').read()

	groups = data.split('\n\n')

	sumuniq = 0
	for group in groups:
		uniq = set(group.replace('\n', ''))
		sumuniq += len(uniq)

	print(sumuniq)

	sumall = 0
	for group in groups:
		sets = [set(person) for person in group.split('\n')]

		sett = reduce(lambda a,b:a.intersection(b), sets)
		sumall += len(sett)

	print(sumall)