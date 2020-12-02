import re
# day 6 
from anytree import Node, RenderTree, AsciiStyle, findall, LevelOrderIter

def countOrbits(tree):
	def countOrbitsForNode(node, count=0):
		if node.parent:
			return countOrbitsForNode(node.parent, count+1)
		else:
			return count

	n_orbits = 0
	for node in LevelOrderIter(tree):
		n_orbits += countOrbitsForNode(node)

	return n_orbits

def parse_nanofactory(item):
	match = re.search('(\d{1,10}) (\w{1,10})', item)

	if match:
		amount, name = match.groups()
		return int(amount), name 


def reactions2tree(orbitmap, rootname='FUEL', delim='=>'):
	root = Node(rootname, amount=1)

	map = [l.split(delim) for l in orbitmap.splitlines() if l]
	raw_children, raw_parents = (list(i) for i in zip(*map))

	parents = []
	children = []
	for i in range(len(raw_parents)):
		children = []
		for child in raw_children:
			subchildren = child.split(',')
			children.append([parse_nanofactory(subchild) for subchild in subchildren])

		children_names, children_amts = zip(*children)

		parents = []
		for parent in raw_parents:
			parents.append(parse_nanofactory(parent))

		parent_names, parent_amts = zip(*parents)

	while parents:
		for node in LevelOrderIter(root):
			while True:
				try:
					idx = parents.index(node.name)

					for child_amt, child_name in children[idx]:
						Node(child_name, parent=node, amount=child_amt)

					del parents[idx]
					del children[idx]
				except:
					break
	return root

	# 		parentnode = []
	# 		for subtree in subtrees.values():
	# 			parentnode.append(findall(subtree, filter_=lambda node: node.name == parent))

	# 		parentnode = list(filter(None, parentnode))
	# 		if parentnode:
	# 			Node(child, parent=parentnode[0][0])
	# 		else:
	# 			subtrees[parent] = Node(child)

	# niter = 0
	# while len(subtrees) > 1 and niter < 1000:
	# 	niter += 1
	# 	subtreenames = list(subtrees.keys())
	# 	for i, name in enumerate(subtreenames):
	# 		for j, name2 in enumerate(subtreenames):
	# 			# look in subtrees[name2] for the parent node of
	# 			parentnode = findall(subtrees[name2], filter_=lambda node: node.name == name)
	# 			try:
	# 				if parentnode:
	# 					parentnode[0].parent = subtrees[name]
	# 					subtrees.pop(name)
	# 					subtreenames.remove(name)
	# 					break
	# 			except:
	# 				continue
	# return tree

TESTMAP1 = """
10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL
"""

if __name__ == '__main__':
	

	tree = reactions2tree(TESTMAP1)
	print(RenderTree(tree, style=AsciiStyle()).by_attr())
	print(countOrbits(tree))

	# tree = map2tree(open('input6.txt', 'r').read())
	# print(RenderTree(tree, style=AsciiStyle()).by_attr())
	# print(countOrbits(tree))
