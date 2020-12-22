TEST1 = """
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
"""

INPUT = open('input13.txt').read()

REGEX = r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)\."

import re
import itertools
import pprint
# print = pprint.pprint

if __name__ == '__main__':
	# INPUT = TEST1
	graph = {}
	for line in filter(None, INPUT.splitlines()):
		p1, sign, amount, p2 = re.fullmatch(REGEX, line).groups()

		graph.setdefault(p1, {})
		graph[p1][p2] = int(amount) if sign == 'gain' else -int(amount)

	print(graph)

	def calc_happiness(order):
		happiness = 0

		for i in range(-1, len(order)-1):
			happiness += graph[order[i]][order[i+1]]
			happiness += graph[order[i+1]][order[i]]

		return happiness
	
	max_happy = 0
	people = list(graph.keys())
	for order in itertools.permutations(people[1:]):
		# print((people[0], order))
		order = [people[0]] + list(order)
		happy = calc_happiness(order)
		max_happy = max(happy, max_happy)
		# print(order, happy)

	print('part1:', max_happy)


	# add myself
	graph['me'] = {k:0 for k in graph}
	for k in graph:
		graph[k]['me'] = 0

	people = list(graph.keys())
	print('part2:', max((calc_happiness(order) for order in itertools.permutations(people))))