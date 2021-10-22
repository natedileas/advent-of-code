import numpy as np
import re
TEST1 = """
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
"""

INPUT = open('input24.txt').read()


def line2tile(line):
    # using grid from here:
    #   https://www.redblobgames.com/grids/hexagons/#coordinates-cube
    direction2idxs = {
        #       x, y, z
        'e':  (+1, -1,  0),
        'w':  (-1, +1,  0),
        'se': (0, -1, +1),
        'nw': (0, +1, -1),
        'ne': (+1,  0, -1),
        'sw': (-1,  0, +1),
    }
    # nwwswee
    x, y, z = 0, 0, 0

    while True:
        # pull an instruction off the front of the line
        match = re.match(r'^(e|se|sw|w|nw|ne)', line)
        if match:
            instr = match.group(1)
        else:
            break

        line = line[len(instr):]

        dx, dy, dz = direction2idxs[instr]
        x += dx
        y += dy
        z += dz

    return x, y, z


def proc_instruct(data):
    tiles = {}
    # white == True
    for line in filter(None, data.splitlines()):
        idxs = line2tile(line)
        tiles.setdefault(idxs, True)
        tiles[idxs] = not tiles[idxs]

    return sum((t == False for t in tiles.values()))


def iterate(data, n=100):
    def neighbors(i=1):
        n = []
        for j in range(-i, i+1):
            for k in range(-i, i+1):
                for l in range(-i, i+1):
                    if abs(j) + abs(k) + abs(l) == i*2 and j + k + l == 0:
                        n.append((j, k, l))
        return n

    neighs = neighbors()

    def get_neighbor_count(tiles, x, y, z):
        count = 0
        for j, k, l in neighs:
            if tiles.get((x+j, y+k, z+l)) == False:
                count += 1
        return count

    tiles = {}
    for line in filter(None, data.splitlines()):
        idxs = line2tile(line)
        tiles.setdefault(idxs, True)
        tiles[idxs] = not tiles[idxs]
        # white == True

    # print(tiles)

    for i in range(n):
        print(i, sum((t == False for t in tiles.values())))

        newtiles = tiles.copy()
        # find the minimum and maximum x, y, z
        xs, ys, zs = zip(*tiles.keys())
        for x in range(min(xs)-2, max(xs)+2):
            for y in range(min(ys)-2, max(ys)+2):
                for z in range(min(zs)-2, max(zs)+2):
                    count = get_neighbor_count(tiles, x, y, z)
                    value = tiles.get((x, y, z), True)

                    if value == True and count == 2:
                        newtiles[(x, y, z)] = False
                    elif value == False and (count == 0 or count > 2):
                        newtiles[(x, y, z)] = True

        # strip out all the white tiles
        newtiles = {k: v for k, v in newtiles.items() if v == False}
        tiles = newtiles

    return sum((t == False for t in tiles.values()))


if __name__ == '__main__':
    from helpers import advent_assert

    advent_assert(line2tile, ('nwwswee',), ((0, 0, 0),))
    advent_assert(proc_instruct, (TEST1, INPUT), (10, 356))
    advent_assert(iterate, (TEST1, INPUT), (2208, 0))
