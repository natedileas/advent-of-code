
import itertools as it
# import numpy as np

INPUT = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
INPUT = open('input.txt').read()


def gammarate(input):
    # most common bit
    def findcounts(lines):
        counts = {}
        for line in lines:
            for i, char in enumerate(line):
                counts.setdefault(i, {})
                counts[i].setdefault(char, 0)
                counts[i][char] += 1

        return counts

    lines = list(filter(None, input.splitlines()))
    counts = findcounts(lines)
    gamma = '0b'
    epsilon = '0b'
    for i in range(len(lines[0])):
        gamma += max(counts[i], key=lambda v: counts[i][v])
        epsilon += min(counts[i], key=lambda v: counts[i][v])

    print(int(gamma, 2))
    print(int(epsilon, 2))

    lines = list(filter(None, input.splitlines()))
    for i in range(len(lines[0])):
        counts = findcounts(lines)
        if counts[i].get('0', 0) > counts[i].get('1', 0):
            char = '0'
        elif counts[i].get('0', 0) < counts[i].get('1', 0):
            char = '1'
        else:
            char = '1'
        # char = max(counts[i], key=lambda v: counts[i][v])
        print(lines, i, char)
        lines = list(filter(lambda l: l[i] == char, lines))

        if len(lines) == 1:
            break
    print(lines[0])
    oxygen = int(lines[0], 2)

    lines = list(filter(None, input.splitlines()))
    for i in range(len(lines[0])):
        counts = findcounts(lines)
        if counts[i].get('0', 0) > counts[i].get('1', 0):
            char = '1'
        elif counts[i].get('0', 0) < counts[i].get('1', 0):
            char = '0'
        else:
            char = '0'
        # char = min(, key=lambda v: counts[i][v])
        print(lines, i, char)
        lines = list(filter(lambda l: l[i] == char, lines))

        if len(lines) == 1:
            break
    print(lines[0])
    co2 = int(lines[0], 2)

    print()

    return int(gamma, 2) * int(epsilon, 2), oxygen * co2


if __name__ == '__main__':
    print('part 1: ', gammarate(INPUT))
    print('part 2: ', )
