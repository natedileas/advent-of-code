from dataclasses import dataclass, field


data = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
data = open("input07").read()

currentbeams = set([data.splitlines()[0].index("S")])
nsplits = 0
for line in data.splitlines()[1:]:
    newbeams = set()
    for beam in currentbeams:
        if line[beam] == "^":
            nsplits += 1
            newbeams.add(beam - 1)
            newbeams.add(beam + 1)
        else:
            newbeams.add(beam)
    currentbeams = newbeams
    # print("".join(l if i not in currentbeams else "|" for i, l in enumerate(line)))
print(nsplits)


@dataclass
class node:
    loc: tuple[int, int]
    children: set = field(default_factory=set)
    parents:  set = field(default_factory=set)

    def __repr__(self) -> str:
        return str(self.loc) + "\n\t" + "".join(repr(c) for c in self.children)

    def __hash__(self) -> int:
        return hash(self.loc)


nodes: dict[tuple[int, int], node] = dict()
edges: set[tuple[tuple[int, int], tuple[int, int]]] = set()

s = data.splitlines()[0].index("S")
currentbeams = set([data.splitlines()[0].index("S")])
root = node((0, s))
nodes[(0, s)] = root
nsplits = 0
for i, line in enumerate(data.splitlines()[1:]):
    # if "^" not in line:
    #     continue
    newbeams = set()
    for beam in currentbeams:
        parentnode = nodes[(i, beam)]
        if line[beam] == "^":
            newa, newb = node((i + 1, beam - 1)), node((i + 1, beam + 1))
            nodes[newa.loc] = newa
            nodes[newb.loc] = newb
            newbeams.add(beam - 1)
            newbeams.add(beam + 1)
            edges.add((parentnode.loc, newa.loc))
            edges.add((parentnode.loc, newb.loc))
        else:
            newbeams.add(beam)
            newb = node((i + 1, beam))
            nodes[newb.loc] = newb
            edges.add((parentnode.loc, newb.loc))
    currentbeams = newbeams
    print("".join(l if i not in currentbeams else "|" for i, l in enumerate(line)))

for parent, child in edges:
    pnode = nodes[parent]
    cnode = nodes[child]
    pnode.children.add(cnode)
    cnode.parents.add(pnode)

def npaths(root: node):
    pathcounts = {}

    def simple_path(n: node):
        if not n.children:
            pathcounts[n] = 1
            return 1
        elif n in pathcounts:
            return pathcounts[n]
        else:
            path_count = 0
            for nn in n.children:
                path_count += simple_path(nn)
            pathcounts[n] = path_count
            return path_count

    return simple_path(root)


print(npaths(root))