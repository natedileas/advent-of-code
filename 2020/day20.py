import numpy as np
import math
INPUT = open('input20.txt').read()
TEST1 = open('test20.txt').read()


if __name__ == '__main__':
    INPUT = TEST1

    # turn into tiles
    tiles = {}
    for tiletext in INPUT.split('\n\n'):
        lines = tiletext.split('\n')
        if not any(lines):
            continue
        number = lines[0].split()[-1].replace(':', '')

        tile = np.asarray([[l for l in line]
                           for line in lines[1:] if line]) == '#'

        tiles[int(number)] = tile

    # print(tiles)

    edges = {}

    for number, tile in tiles.items():
        edge = edges.setdefault(number, [])
        # left, right, top, bottom
        edge.append(tile[0, :])
        edge.append(tile[-1, :])
        edge.append(tile[:, 0])
        edge.append(tile[:, -1])

    # print(edges)

    # each edge will have 2 (corner), 3 ( edge), or 4 (inside) matches
    matches = {}
    for number, edgelist in edges.items():
        for edge in edgelist:
            for n2, edges2 in edges.items():
                if number == n2:
                    continue
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

    # each tile pair has 8 possible arrangements
    # i know the connectivity but not the arangement

    # organize the tiles into an image
    # square image
    l = int(math.sqrt(len(tiles)))
    image_tiles = [[None for j in range(l)] for i in range(l)]
    tile_map = [[None for j in range(l)] for i in range(l)]

    for n, m in matches.items():
        if len(m) == 2:
            image_tiles[0][0] = tiles[n]
            tile_map[0][0] = n
            break

    last_tile_n = tile_map[0][0]
    last_tile = image_tiles[0][0]
    for i in range(l):
        for j in range(l):
            if image_tiles[i][j] is not None:
                continue

            match_edge = 

            tile_map[i][j] = 
