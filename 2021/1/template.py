
import itertools as it
# import numpy as np

# INPUT = ""
INPUT = open('input1.txt').read()

if __name__ == '__main__':
    values = [int(i) for i in INPUT.splitlines() if i]

    print('part 1: ', sum(values[i+1] > values[i]
                          for i in range(len(values)-1)))

    print('part 2: ', sum(sum(values[i+1:i+4]) > sum(values[i:i+3])
                          for i in range(len(values)-3)))
