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


# print(root)
paths = set()


def traverse(r, path=None):
    if path is None:
        path = []

    path.append(r.loc)
    if not r.children:
        paths.add(tuple(path))

    for c in r.children:
        traverse(c, path[:])


def traverse_and_count(r):
    npaths = 0

    def _traverse(n):
        if not n.children:
            nonlocal npaths
            npaths += 1

        for c in n.children:
            _traverse(c)

    _traverse(r)
    return npaths

def topoback(n):
    leafs = [_ for _ in nodes.values() if not _.children]

    def _scan_back(node, target, npaths=0):
        if node == target:
            return 1
        
        for p in node.parent:
            npaths += 
        

    for l in leafs:
        npaths += _scan_back(l, n)

# print(traverse_and_count(root))
print(topoback(root))