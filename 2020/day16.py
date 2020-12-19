TEST1 = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

TEST2 = """
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""

INPUT = open('input16.txt').read()

import re

def rule2func(rule):
	label, ranges = rule.split(':')

	match = re.fullmatch(r'(\d+)-(\d+) or (\d+)-(\d+)', ranges.strip())
	a, b, c, d = match.groups()

	def func(value):
		return int(a) <= value <= int(b) or int(c) <= value <= int(d)

	return label, func

def applyrules(rules, ticket):

	values = [int(i.strip()) for i in ticket.split(',')]

	sum_invalid = 0
	for val in values:
		if not any((rule(val) for rule in rules)):
			sum_invalid += val

	return sum_invalid


def find_rule_order(ruledict, tickets):
	all_tickets = [[int(i.strip()) for i in ticket.split(',')] for ticket in tickets if ticket]

	matching_rules = {}
	# while ruledict:
	# print('\r', len(ruledict), len(ruleorder), end='')
	for i in range(len(all_tickets[0])):
		# find the rule for which all_tickets[:][0] is valid

		if i in ruledict:
			continue

		matching_rules.setdefault(i, [])
		for rulename, rulefunc in ruledict.items():
			if all((rulefunc(ticket[i]) for ticket in all_tickets)):
				matching_rules[i].append(rulename)

			# if len(matching_rules) == 1:
				# # print(matching_rules[0],i)
				# rulename = matching_rules[0]
				# ruleorder[i] = rulename
				# del ruledict[rulename]

	all_matching_rulnames = [rulename for rules in matching_rules.values() for rulename in rules ]
	all_rules = {rule:rule in all_matching_rulnames for rule in ruledict}
	assert all(all_rules.values())
	print(all_rules)
	print(all_matching_rulnames)
	print(matching_rules)

	# matching_rules_sorted = sorted(matching_rules.items(), key=lambda i: len(i[1]))

	ruleorder = {}
	while any((len(m) for m in matching_rules.values())):
		print('\r', len(ruleorder), end='')
		nextmatch = None
		for i, matches in matching_rules.items():
			if len(matches) == 1:
				nextmatch = matches[0]
				ruleorder[i] = nextmatch
				break
				# remove it from the rest of the options

		if nextmatch:
			for i, matches in matching_rules.items():
				try:
					matches.remove(nextmatch)
				except ValueError:
					pass

	print()
	return ruleorder

if __name__ == '__main__':
	rules, myticket, nearbytickets = INPUT.split('\n\n')
	# rules, myticket, nearbytickets = TEST2.split('\n\n')

	rulefuncs = dict([rule2func(rule) for rule in rules.splitlines() if rule])

	print(sum((applyrules(rulefuncs.values(), ticket) for ticket in nearbytickets.splitlines()[1:] if ticket)))

	valid_nearby_tickets = [ticket for ticket in nearbytickets.splitlines()[1:] if not applyrules(rulefuncs.values(), ticket)]
	valid_nearby_tickets.append(myticket.splitlines()[1])

	print(len(nearbytickets.splitlines()[1:]), len(valid_nearby_tickets))

	ruleorder = find_rule_order(rulefuncs, valid_nearby_tickets)

	print(ruleorder)

	myvalues = {ruleorder.get(i, str(i)):int(v) for i,v in enumerate(myticket.splitlines()[1].split(','))}

	print(myvalues, len(myvalues))

	prod = 1
	for key, value in myvalues.items():
		if key.startswith('departure'):
			prod *= value

	print(prod)


