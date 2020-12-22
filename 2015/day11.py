def increment_str(s):
	a = 97
	az = 123 - 97
	# 97 - 122 == a-z
	new = bytes()
	increment = True
	# while True:
	for c in s[::-1].encode():
		if increment:
			newc = ((int(c) - a + 1) % az) + a
			if newc > c:
				# we didn't wrap
				increment = False
		else:
			newc = c

		new += bytes([newc])

	return new.decode()[::-1]

import re

def has_increasing_triple(p):
	b = bytes(p.encode())
	for i in range(len(b)-2):
		if b[i] + 2 == b[i+1] + 1 == b[i+2]:
			p
			return True
	return False

def has_bad_letters(p):
	return any((i in p for i in 'iol'))

def has_two_doubles(p):
	match = re.match(r'.*([a-z])\1.*([a-z])\2', p)
	# print(match, match.groups() if match else match)
	return match is not None
	
def valid_v1(p):
	# print(f'has_increasing_triple({p}):', has_increasing_triple(p))
	# print(f'not has_bad_letters({p}):', not has_bad_letters(p))
	# print(f'has_two_doubles({p}):', has_two_doubles(p))

	return (
		has_increasing_triple(p) 
		and not has_bad_letters(p) 
		and has_two_doubles(p)
	)

def increment_until_valid(p):
	while not valid_v1(p):
		print('\r', p, end='')
		p = increment_str(p)
	print()
	return p

if __name__ == '__main__':
	assert increment_str('abcd') == 'abce'
	assert increment_str('abcz') == 'abda'

	# print(valid_v1('hijklmmn'))
	# print(valid_v1('abbceffg'))
	# print(valid_v1('abbcegjk'))
	# print(valid_v1('abcdffaa'))
	# print(increment_until_valid('abcdefgh'), 'abcdffaa')
	# print('part 1:', increment_until_valid('hxbxwxba'))   # hxbxxyzz
	print('part 2:', increment_until_valid(increment_str('hxbxxyzz')))