
import itertools as it
import numpy as np

INPUT = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""
INPUT = open('input.txt').read()


def makemap(input):
    points = {}
    for line in filter(None, input.splitlines()):
        p1, p2 = line.split(' -> ')
        x1, y1 = map(int, p1.split(','))
        x2, y2 = map(int, p2.split(','))

        # print(x1, y1, x2, y2)

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                points.setdefault((x1, y), 0)
                # print(x1, y)
                points[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                # print(x, y1)
                points.setdefault((x, y1), 0)
                points[(x, y1)] += 1

    return sum(1 for v in points.values() if v >= 2)


def makemap_diag(input):
    points = {}
    for line in filter(None, input.splitlines()):
        p1, p2 = line.split(' -> ')
        x1, y1 = map(int, p1.split(','))
        x2, y2 = map(int, p2.split(','))

        # print(x1, y1, x2, y2)

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                points.setdefault((x1, y), 0)
                # print(x1, y)
                points[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                # print(x, y1)
                points.setdefault((x, y1), 0)
                points[(x, y1)] += 1
        else:
            xstep = int((x2 - x1) / abs(x2 - x1))
            ystep = int((y2 - y1) / abs(y2 - y1))
            for i, x in enumerate(range(x1, x2+xstep, xstep)):
                y = y1+(i*ystep)
                # print((x, y))
                points.setdefault((x, y), 0)
                points[(x, y)] += 1

    return sum(1 for v in points.values() if v >= 2)


if __name__ == '__main__':
    print('part 1: ', makemap(INPUT))
    print('part 2: ', makemap_diag(INPUT))
