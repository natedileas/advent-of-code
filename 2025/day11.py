data = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""
data = open("input11").read()

graph = {}
for line in data.splitlines():
    s, e = line.split(":")
    graph[s] = e.split()


def recursive_topological_sort(graph, node):
    result = []
    seen = set()

    def recursive_helper(node):
        for neighbor in graph.get(node, ()):
            if neighbor not in seen:
                seen.add(neighbor)
                recursive_helper(neighbor)
        result.insert(0, node)  # this line replaces the result.append line

    recursive_helper(node)
    return result


def npaths(graph, source, target):
    pathcounts = {target: 1}
    if target != "out":
        pathcounts["out"] = 0

    def simple_path(s, t):
        # print(source, target, s, t)
        if s == t:
            return 1
        elif s in pathcounts:
            return pathcounts[s]
        else:
            path_count = 0
            for w in graph[s]:
                path_count += simple_path(w, t)
            pathcounts[s] = path_count
            return path_count

    return simple_path(source, target)


print(npaths(graph, "you", "out"))


# data = """svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out"""

graph = {}
for line in data.splitlines():
    s, e = line.split(":")
    graph[s] = e.split()

sort = recursive_topological_sort(graph, "svr")
if sort.index("dac") < sort.index("fft"):
    print(
        npaths(graph, "svr", "dac")
        * npaths(graph, "dac", "fft")
        * npaths(graph, "fft", "out")
    )
else:
    print(
        npaths(graph, "svr", "fft")
        * npaths(graph, "fft", "dac")
        * npaths(graph, "dac", "out")
    )
