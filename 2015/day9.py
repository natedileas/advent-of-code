import re


TEST1 = """
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""

def makegraph(data):
	edges = []
	graph = {}
	for line in data.splitlines():
		m = re.fullmatch(r'(\w+) to (\w+) = (\d+)', line)
		if m is not None:
			start, end, dist = m.groups()
			node = graph.setdefault(start, {})
			node[end] = int(dist)
			node2 = graph.setdefault(end, {})
			node2[start] = int(dist)
			edges.append((start, end, dist))

	return graph, edges


def find_minpath(data):
	g, e = makegraph(data)

	dists = {}
	import itertools
	for path in itertools.permutations(g.keys(), len(g.keys())):
		dists[path] = sum((g[path[i]][path[i+1]] for i in range(len(path) - 1)))

	import pprint
	# pprint.pprint(dists)
	print('min path: ', min(dists, key=lambda i:dists[i]), min(dists.values()))
	print('max path: ', max(dists, key=lambda i:dists[i]), max(dists.values()))

if __name__ == '__main__':
	find_minpath(TEST1)
	find_minpath(open('input9.txt').read())
