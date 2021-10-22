
INPUT = open('input10.txt').read()


TEST1 = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

TEST2 = """
16
10
15
5
1
11
7
19
6
12
4
"""

import math


def combs(blocklen): 
    # return blocklen
    if blocklen == 1:
        return 1

    if blocklen == 2:
        return 2
    if blocklen == 3:
        return 4

    if blocklen == 4:
        return 8

    return sum((math.comb(blocklen, k) for k in range(blocklen + 1)))


def countlist(random_list):
    retlist = []
    count = 1
    for i in range(len(random_list) - 1):
        if random_list[i] == random_list[i+1]:
            count += 1
        else:
            # If it is not append the count and restart counting
            retlist.append((count, random_list[i]))
            count = 1

    # Since we stopped the loop one early append the last count
    retlist.append((count, random_list[-1]))
    return retlist


def total_chances(arr):
    all_chances = []
    for count, item in countlist(arr):
        if item == 1:
            all_chances.append(combs(count))

    print(all_chances)

    return np.prod(np.asarray(all_chances))


def count_adapters(adapters, stack=0, set_options=set()):
    # print('\r', stack, end='')
    count = 0

    if (np.diff(adapters) > 3).any():
        return 0, set_options
    else:
        print(adapters, stack)
        set_options.add(','.join((str(i) for i in adapters)))
        # count += 1

    for i in range(1 , len(adapters) - 1):
        # if stack < 3: print(stack, i)
        adap = adapters.pop(i)
        c, s =  count_adapters(adapters, stack=stack+1, set_options=set())
        count += len(s)
        adapters.insert(i, adap)

    return count, set_options


def count_adapters(adapters, stack=0, set_options=set()):
    # print('\r', stack, end='')
    count = 0

    if (np.diff(adapters) > 3).any():
        return 0, set_options
    else:
        print(adapters, stack)
        set_options.add(','.join((str(i) for i in adapters)))
        # count += 1

    for i in range(1 , len(adapters) - 1):
        # if stack < 3: print(stack, i)
        adap = adapters.pop(i)
        c, s =  count_adapters(adapters, stack=stack+1, set_options=set())
        count += len(s)
        adapters.insert(i, adap)

    return count, set_options


# def count_adapters_big(adapters):
#   diff = np.diff(adapters)
#   indexs, = np.where(diff == 3)

#   indexs += 1
#   indexs = np.append(indexs,[len(adapters)])
#   indexs = np.append([0], indexs)

#   sublists = []
#   # p = 1
#   for i in range(len(indexs)-1):
#       sublists.append(adapters[indexs[i]:indexs[i+1]+1])
#       # p = i

#   print(adapters)
#   print(diff)
#   print(indexs)
#   print(sublists)

#   prod = 1
#   for sub in sublists:
#       c, s =  count_adapters(list(sub))
#       # print(sub, count_adapters(list(sub)))
#       prod *= len(s)

#   return prod


if __name__ == '__main__':
    # INPUT = TEST1
    import numpy as np
    lines = [int(i) for i in INPUT.splitlines() if i]
    arr = np.asarray(lines)
    arr = np.append(arr, [0, max(arr) + 3])
    arr.sort()


    df = np.diff(arr)

    print(arr, df)

    print(sum(df == 1), sum(df == 3))

    sol = {0:1}
    for line in sorted(lines):
        sol[line] = 0
        if line - 1 in sol:
            sol[line]+=sol[line-1]
        if line - 2 in sol:
            sol[line]+=sol[line-2]
        if line - 3 in sol:
            sol[line]+=sol[line-3]

    print(sol[max(lines)])