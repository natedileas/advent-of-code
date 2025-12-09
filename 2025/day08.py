data = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
nconn = 10
data = open("input08").read()
nconn = 1000
from functools import reduce
import numpy as np
from scipy.spatial.distance import pdist, squareform

positions = np.array([list(map(int, l.split(","))) for l in data.splitlines()])
print("pdist")

pdists = pdist(positions, "euclidean")
s = squareform(pdists)
# print(s.argmin())
s[np.tri(len(positions), dtype=np.bool)] = np.inf
print("conn")
ss = np.argsort(s, axis=None)
connections: list[tuple[int, int]] = []
for i in range(nconn):
    r, c = np.unravel_index(ss[i], s.shape)
    connections.append((r, c))

print("strings")
sc = sorted(connections)
strings: list[set] = [set(sc[0])]
for i, j in sc[1:]:
    groupids = [ii for ii, s in enumerate(strings) if i in s or j in s]

    combined = set()
    for si in groupids:
        sr = strings[si]
        combined = combined.union(sr)
    combined.add(i)
    combined.add(j)
    strings = [combined] + [s for i, s in enumerate(strings) if i not in groupids]

print(reduce(lambda a, b: a * b, sorted((len(s) for s in strings), reverse=True)[:3]))

connections: list[tuple[int, int]] = []
strings: list[set] = [set(sc[0]), set(sc[0])]
i = 0
while i < len(ss) and (len(strings) != 1 or len(strings[0]) != len(positions)):
    if np.isinf(s.flat[ss[i]]):
        break
    r, c = np.unravel_index(ss[i], s.shape)

    groupids = [ii for ii, sr in enumerate(strings) if r in sr or c in sr]

    combined = set()
    for si in groupids:
        sr = strings[si]
        combined = combined.union(sr)
    combined.add(r)
    combined.add(c)
    strings = [combined] + [sr for i, sr in enumerate(strings) if i not in groupids]
    i += 1
    # print(positions[r][0] * positions[c][0])

# r, c = np.unravel_index(, s.shape)
print(positions[r][0] * positions[c][0])
# print(reduce(lambda a, b: a * b, sorted((len(s) for s in strings), reverse=True)[:3]))
