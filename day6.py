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


def map2tree(orbitmap):
	tree = Node('COM')

	subtrees = {'COM':tree}
	for line in orbitmap.splitlines():
		if line:
			parent, child = line.split(')')

			

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
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""

if __name__ == '__main__':
	

	tree = map2tree(TESTMAP1)
	print(RenderTree(tree, style=AsciiStyle()).by_attr())
	print(countOrbits(tree))

	tree = map2tree(open('input6.txt', 'r').read())
	print(RenderTree(tree, style=AsciiStyle()).by_attr())
	print(countOrbits(tree))
