INPUT = open('input13.txt').read()

TEST1 = """939
7,13,x,x,59,x,31,19
"""


# 3417
TEST2 = """
17,x,13,19
"""

# 754018
TEST3 = """
67,7,59,61
"""

# 779210
TEST4 = """
67,x,7,59,61
"""

TEST5 = """
67,7,x,59,61
"""

TEST6 = """
1789,37,47,1889
"""

import numpy as np
import math

def earliest_time_bus(data):
    starttime,busses, = data.splitlines()
    starttime = int(starttime)
    busses = [int(b) for b in busses.split(',') if b != 'x']
    times = [(starttime-((math.ceil(starttime//b)+1)*b),b) for b in busses]

    print(times)
    return max(times, key=lambda i:i[0])

def p1(data):
    t, b = earliest_time_bus(data)
    return abs(t) * b

def p2(data, start=0):
    starttime,busses, = data.splitlines()
    # busses = [(i, int(b)) for i, b in enumerate(busses.split(',')) if b != 'x']
    # busses = sorted(busses, key=lambda i:i[1], reverse=True)

    # print(busses)

    busses = [int(b) if b != 'x' else 'x' for i, b in enumerate(busses.split(','))]
    mods = {bus: -i % bus for i, bus in enumerate(busses) if bus != "x"}
    vals = list(reversed(sorted(mods)))
    val = mods[vals[0]]
    r = vals[0]
    for b in vals[1:]:
        while val % b != mods[b]:
            val += r
        r *= b
    return val
    


if __name__ == '__main__':
    print(p1(INPUT))
    print(p1(TEST1))
    print(p2(TEST1))
    print(p2(TEST2))
    print(p2(TEST3))
    print(p2(TEST4))
    print(p2(TEST5))
    print(p2(TEST6))   # 1202161486
    print(p2(INPUT))
