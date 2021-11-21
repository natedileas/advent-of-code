import itertools as it
TEST1 = """
20
15
10
5
5
"""

INPUT = open('input17.txt').read()


# def count_ways(containers, total=150):
#     ways = 0

#     containers = sorted(containers, reverse=True)

#     def count(containers, used, stack=0):
#         print(containers, used, stack)
#         for i in range(len(containers)):
#             c = containers.pop(0)
#             used.append(c)

#             if sum(used) == total:
#                 ways += 1
#                 used.pop()
#                 print(containers, used, stack)
#                 return
#             elif sum(used) < total:
#                 count(containers, used, stack=stack+1)
#             elif sum(used) > total:
#                 containers.append(used.pop())
#                 print(containers, used, stack)
#                 return

#     count(containers, [])
#     return ways


def count_ways(containers, volume):

    return sum((1 for c in range(2, len(containers)) for i in it.combinations(containers, c) if sum(i) == volume))


def find_min_ways(containers, volume):
    for c in range(2, len(containers)):
        ways = 0
        for i in it.combinations(containers, c):
            if sum(i) == volume:
                ways += 1

        if ways > 0:
            return c, ways


print(count_ways([int(l) for l in TEST1.splitlines() if l], 25), 25)
print(count_ways([int(l) for l in INPUT.splitlines() if l], 150), 150)
print(find_min_ways([int(l) for l in INPUT.splitlines() if l], 150), 150)
