import re
# INPUT = ""
INPUT = open('input19.txt').read()

TEST1 = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""

TEST2 = """
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
"""

if __name__ == '__main__':
	# INPUT = TEST1
	# INPUT = TEST2
	ruletext, messagetext = INPUT.split('\n\n')
	
	messages = list(filter(None, messagetext.splitlines()))
	print(messages)

	rules = {}
	for line in filter(None, ruletext.splitlines()):
		num, rhs = line.split(':')
		rule = rules.setdefault(int(num), [])

		for possiblematch in rhs.split('|'):
			items = possiblematch.split()
			converted_items = []
			for item in items:
				match = re.match(r'"(\w+)"', item)
				if match:
					converted_items.append(match.group(1))
				else:
					converted_items.append(int(item))

			rule.append(converted_items)


	print(rules)
	def gen_rule_re(num, regex=r''):
		rule = rules[num]
		subs = []
		for seq in rule:
			sub = ''
			for item in seq:
				if isinstance(item, str):
					regex += item
					return regex
				# elif item == 8:
				# 	sub += '*'
				elif item == num:
					sub += '*'
				else:
					sub += gen_rule_re(item, r'')

			subs.append(sub)

		regex += f'({"|".join(subs)})'

		return regex


	regex = gen_rule_re(0)

	print(regex)

	print('part1:', sum((re.fullmatch(regex, m) is not None for m in messages)))

	# part 2
	"""
	8: 42 | 42 8
	11: 42 31 | 42 11 31
	"""
	def gen_rule_re2(num, regex=r''):
		if num == 8:
			return f'({gen_rule_re2(42)}+)'
		if num == 11:
			re42 =  gen_rule_re2(42)
			re31 =  gen_rule_re2(31)
			return f'({re42}{re31}|{re42}{{2}}{re31}{{2}}|{re42}{{3}}{re31}{{3}}|{re42}{{4}}{re31}{{4}}|{re42}{{5}}{re31}{{5}}|{re42}{{6}}{re31}{{6}})'

		rule = rules[num]
		subs = []
		for seq in rule:
			sub = ''
			for item in seq:
				if isinstance(item, str):
					return regex + item
				else:
					sub += gen_rule_re2(item, r'')

			subs.append(sub)

		regex += f'({"|".join(subs)})'

		return regex

	rules[8] = [[42], [42, 8]]
	rules[11] = [[42, 31], [42, 11, 31]]

	regex2 = gen_rule_re2(0)
	print(regex2)
	print('part2:', sum((re.fullmatch(regex2, m) is not None for m in messages)))

