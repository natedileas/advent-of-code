INPUT = open('input20.txt').read()
TEST1 = open('test20.txt').read()

import numpy as np

if __name__ == '__main__':
	INPUT = TEST1

	# turn into tiles
	tiles = {}
	for tiletext in INPUT.split('\n\n'):
		lines = tiletext.split('\n')
		if not any(lines): continue
		number = lines[0].split()[-1].replace(':', '')

		tile = np.asarray([[l for l in line] for line in lines[1:] if line]) == '#'

		tiles[int(number)] = tile

	# print(tiles)

	edges = {}

	for number, tile in tiles.items():
		edge = edges.setdefault(number, [])
		# left, right, top, bottom
		edge.append(tile[0,:])
		edge.append(tile[-1,:])
		edge.append(tile[:,0])
		edge.append(tile[:,-1])

	# print(edges)

	# each edge will have 2 (corner), 3 ( edge), or 4 (inside) matches
	matches = {}
	for number, edgelist in edges.items():
		for edge in edgelist:
			for n2, edges2 in edges.items():
				if number == n2: continue
				for e2 in edges2:
					if np.all(edge == e2) or np.all(edge[::-1] == e2):
						matches.setdefault(number, [])
						matches[number].append(n2)
						break

	print(matches, [len(m) for m in matches.values()])

	# mult edges
	m = 1
	for key, match in matches.items():
		if len(match) == 2:
			m *= key

	print('part 1:', m)

	# part 2

	# i have a list which identifies corners, edges, and interiors, and their neighbors
	corners = [k for k,v in matches.items() if len(v) == 2]
	# edges = [k for k,v in matches.items() if len(v) == 3]
	# insides = [k for k,v in matches.items() if len(v) == 4]

	# height = int(np.sqrt(len(tiles)))
	# imageorder = np.zeros((height, height))
	# print(image.shape)

	tiles2 = tiles.copy()
	tilenum = corners.pop(0)
	# imageorder[0,0] = tilenum

	# items = corners + edges + insides
	# while items:
	# 	possible_matches = matches[tilenum]
	# 	
	transformations = {
		'none': lambda m: m,
		'fliplr': np.fliplr,
		'flipud': np.flipud,
		'rot90': lambda m: np.rot90(m, k=1),
		'rot180': lambda m: np.rot90(m, k=2),
		'rot270': lambda m: np.rot90(m, k=3),
	}

	# positions = {tilenum: (0,0)}

	# possibletiles = list(tiles.keys())
	# possibletiles.remove(tilenum)
	
	# while possibletiles:
	# 	for i in range(len(possibletiles)):
	# 		print(i)
	# 		num = possibletiles.pop(0)

	# 		if num not in positions: 
	# 			possibletiles.insert(0, num)
	# 			continue

	# 		t1 = tiles[num]
	# 		t1y, t1x = positions[num]

	# 		for num2 in possibletiles:
	# 			for t, f in transformations.items():
	# 				t2 = f(tiles[num2])

	# 				if np.all(t1[0,:] == t2[-1,:]):
	# 					# t2 is to the right of t1
	# 					positions[num2] = (t1y, t1x+1)
	# 				elif np.all(t1[-1,:] == t2[0,:]):
	# 					# t2 is to the left of t1
	# 					positions[num2] = (t1y, t1x-1)
	# 				elif np.all(t1[:,-1] == t2[:,0]):
	# 					# t2 is below t1
	# 					positions[num2] = (t1y-1, t1x)
	# 				elif np.all(t1[:,0] == t2[:,-1]):
	# 					# t2 is above t1
	# 					positions[num2] = (t1y+1, t1x)

	# print(positions)

	


