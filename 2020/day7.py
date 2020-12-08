TEST1 = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

TEST2 = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

import re

def makegraph(data):
	graph = {}
	for line in data.splitlines():
		if line:
			lhs, rhs = line.split('contain')
			inbag, = re.fullmatch(r'([a-z]+ [a-z]+) bags', lhs.strip()).groups()

			outbags = [re.match(r'(\d+) ([a-z]+ [a-z]+) bags?', bag.strip()).groups() for bag in rhs.split(',') if bag != " no other bags."]

			node = graph.setdefault(inbag, [])
			node.extend(outbags)

	import pprint
	# pprint.pprint(graph)
	return graph

def p1(data):
	graph = makegraph(data)

	def coutn_cntn(matchcolor, colors_contain_goldbag=set()):

		for node, contains in graph.items():
			# if node in colors_contain_goldbag:
			# 	continue

			for count, color in contains:
				if color == matchcolor:
					colors_contain_goldbag.add(node)
					graph[node] = []
					coutn_cntn(node, colors_contain_goldbag)

		return colors_contain_goldbag

	return coutn_cntn('shiny gold', set())

def p2(data):
	# count the number of bags going down from a shiny gold bag
	graph = makegraph(data)

	def count_bags(node='shiny gold', total_count=0):
		if len(graph[node]) == 0:
			return 1

		for count, color in graph[node]:
			# print(count, color, total_count)
			total_count += int(count) * count_bags(color, 1)# + int(count)

		return total_count

	return count_bags()


if __name__ == '__main__':
	print(p1(TEST1))
	print(len(p1(open('input7.txt').read())))
	print(p2(TEST1), 32)
	print(p2(TEST2), 126)
	print(p2(open('input7.txt').read()))
