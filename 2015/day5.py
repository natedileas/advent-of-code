
import re 

def countinstr(s, matchc):
	count = 0
	for c in s:
		if c == matchc:
			count += 1
	return count

def has_double_letter(s):
	return re.search(r'([a-z])\1', s) is not None

def doesnt_have_bad_2grams(s):
	return all((b not in s for b in ('ab', 'cd', 'pq', 'xy')))

def is_nice(s):

	isnice = True
	isnice &= sum((countinstr(s, c) for c in 'aeiou')) >= 3
	isnice &= has_double_letter(s)
	isnice &= doesnt_have_bad_2grams(s)

	return isnice


def is_nice2(s):

	isnice = True
	isnice &= re.search(r'([a-z])[a-z]\1', s) is not None
	isnice &= re.search(r'([a-z]{2}).*\1', s) is not None

	return isnice


if __name__ == '__main__':
	print('ugknbfddgicrmopn', is_nice('ugknbfddgicrmopn'))
	print('haegwjzuvuyypxyu', is_nice('haegwjzuvuyypxyu'))
	print('dvszwmarrgswjxmb', is_nice('dvszwmarrgswjxmb'))

	print(sum((is_nice(s) for s in open('input5.txt').read().splitlines())))


	print('qjhvhtzxzqqjkmpb', is_nice2('qjhvhtzxzqqjkmpb'))
	print('xxyxx', is_nice2('xxyxx'))
	print('uurcxstgmygtbstg', is_nice2('uurcxstgmygtbstg'))
	print('ieodomkazucvgmuy', is_nice2('ieodomkazucvgmuy'))

	print(sum((is_nice2(s) for s in open('input5.txt').read().splitlines())))

