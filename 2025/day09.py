data = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
data = open("input09").read()


from functools import lru_cache
import numpy as np
from scipy.spatial.distance import pdist, squareform

positions = np.array(
    [list(map(int, l.split(",")))[::-1] for l in data.splitlines()]
).astype(int)
redtiles = set((r, c) for r, c in positions)
print("pdist")

area = lambda a, b: abs(a[0] - b[0] + 1) * abs(a[1] - b[1] + 1)
pdists = pdist(positions, area)
s = squareform(pdists).astype(int)
# print(s.argmin())
s[np.tri(len(positions), dtype=np.bool)] = -1000
ss = np.argsort(s, axis=None)
r, c = np.unravel_index(np.argmax(s), s.shape)
print(r, c, positions[r], positions[c], np.max(s))

print("edges")
greentiles = []
# positions += [positions[0]]
horizontal_edges = set()
vertical_edges = set()
for i in range(len(positions)):
    r1, c1 = positions[i]
    if i + 1 == len(positions):
        r2, c2 = positions[0]
    else:
        r2, c2 = positions[i + 1]

    if r1 == r2:
        step = -1 if c1 > c2 else 1
        for c in range(c1, c2 + step, step):
            greentiles.append((r1, c))
            horizontal_edges.add((r1, c))
    elif c1 == c2:
        step = -1 if r1 > r2 else 1

        for r in range(r1, r2 + step, step):
            greentiles.append((r, c1))
            vertical_edges.add((r, c1))

        if step == 1:
            vertical_edges.remove((r2, c1))
        else:
            vertical_edges.remove(((r1, c1)))
    else:
        raise ValueError("should never happen")
rmin, rmax = min(positions[:, 0]), max(positions[:, 0]) + 1
cmin, cmax = min(positions[:, 1]), max(positions[:, 1]) + 1
print("centers", rmin, rmax, cmin, cmax)
# print(
#     "\n".join(
#         "".join(
#             "#" if (r, c) in redtiles else "X" if (r, c) in greentiles else "."
#             for c in range(cmin - 2, cmax + 2)
#         )
#         for r in range(rmin - 2, rmax + 2)
#     )
# )
# positions.pop()
# now interior points
alledges = set(greentiles).union(redtiles)
for pr, pc in positions:
    alledges.add((pr, pc))
edgesnohorz = alledges.difference(horizontal_edges)
# for r in range(rmin, rmax):
#     for c in range(cmin, cmax):
#         ray = [(r, _c) for _c in range(c, cmax)]
#         rayintersections = [1 for p in ray if p in edges]
#         if len(rayintersections) % 2 == 1:
#             greentiles.append((r, c))

greentiles = set(greentiles)


# @lru_cache(maxsize=None)
def test_is_green(r, c):
    return sum(1 for _c in range(c + 1, cmax) if (r, _c) in vertical_edges) % 2 == 1


# print(
#     "\n".join(
#         "".join(
#             "#" if (r, c) in redtiles else "X" if (r, c) in greentiles else "."
#             for c in range(cmin - 2, cmax + 2)
#         )
#         for r in range(rmin - 2, rmax + 2)
#     )
# )
print("rectangles")
for i in np.argsort(s, axis=None)[::-1]:
    p1, p2 = np.unravel_index(i, s.shape)
    r1, c1 = positions[p1]
    r2, c2 = positions[p2]
    print(i, abs(r2 - r1), abs(c2 - c1))
    stepr = -1 if r1 > r2 else 1
    stepc = -1 if c1 > c2 else 1
    if (
        all(
            (r, c1) in alledges or test_is_green(r, c1)
            for r in range(r1, r2 + stepr, stepr)
        )
        and all(
            (r, c2) in alledges or test_is_green(r, c2)
            for r in range(r1, r2 + stepr, stepr)
        )
        and all(
            (r1, c) in alledges or test_is_green(r1, c)
            for c in range(c1, c2 + stepc, stepc)
        )
        and all(
            (r2, c) in alledges or test_is_green(r2, c)
            for c in range(c1, c2 + stepc, stepc)
        )
    ):
        print((r1, c1), (r2, c2), area((r1, c1), (r2, c2)))
        break
