
key1 = 3418282
key2 = 8719412
# TEST
# key1 = 5764801
# key2 = 17807724

def find_loopsize(key, sn=7):
	loopsize = 0
	value = 1
	while value != key:
		# print(loopsize, value)
		value *= sn
		value = value % 20201227
		loopsize += 1

	return loopsize

def apply_loop(loopsize, sn=7):
	value = 1

	for i in range(loopsize):
		value *= sn
		value = value % 20201227

	return value

l1 = find_loopsize(key1)
l2 = find_loopsize(key2)

print(l1, l2)

key = apply_loop(l2, key1)

print(key)