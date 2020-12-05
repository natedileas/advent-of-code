
input3 = open('input3.txt').read()

def count_dupe_houses(instructions):
	start = (0,0)   # y, x
	all_locs = [start]

	old = start
	for i in instructions:
		if i == '^':
			new = (old[0] + 1, old[1])
		elif i == 'v':
			new = (old[0] - 1, old[1])	
		elif i == '<':
			new = (old[0], old[1] - 1)
		elif i == '>':
			new = (old[0], old[1] + 1)

		old = new
		all_locs.append(new)

	return 	len(set(all_locs))


def count_dupe_houses2(instructions):
	start = (0,0)   # y, x
	all_locs = [start] * 2

	s1 = start
	s2 = start
	# print(s1, s2)
	for idx, i in enumerate(instructions):

		if idx % 2 == 0:
			old = s1
		else:
			old = s2

		if i == '^':
			new = (old[0] + 1, old[1])
		elif i == 'v':
			new = (old[0] - 1, old[1])	
		elif i == '<':
			new = (old[0], old[1] - 1)
		elif i == '>':
			new = (old[0], old[1] + 1)

		
		if idx % 2 == 0:
			s1 = new
		else:
			s2 = new

		# print(s1, s2)
		all_locs.append(new)

	# print(all_locs)
	return len(set(all_locs))


print(count_dupe_houses('>'))
print(count_dupe_houses('^>v<'))
print(count_dupe_houses('^v^v^v^v^v'))
print(count_dupe_houses(input3))
			

print(count_dupe_houses2('^v'))
print(count_dupe_houses2('^>v<'))
print(count_dupe_houses2('^v^v^v^v^v'))
print(count_dupe_houses2(input3))
