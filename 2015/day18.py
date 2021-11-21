# game of life
import numpy as np

TEST1 = """
.#.#.#
...##.
#....#
..#...
#.#..#
####..
"""

INPUT = open('input18.txt').read()


def input2state(input):
    lines = input.splitlines()
    state = [[c == '#' for c in l.strip()] for l in lines if l]
    return np.asarray(state, dtype=bool)


def sum_neighbors(state, index):
    # return the sum of the 8-neighborhood, zeros beyond edges
    i, j = index
    return sum((state[i+oi, j+oj] for oi in range(0, 3) for oj in range(0, 3) if not oi == oj == 1))


def take_step(state):
    new_state = np.zeros(state.shape, dtype=bool)
    padded = np.pad(state, 1)
    for index, val in np.ndenumerate(state):
        n = sum_neighbors(padded, index)
        if val and (n == 2 or n == 3):
            new_state[index] = True
        elif not val and n == 3:
            new_state[index] = True

    return new_state


if __name__ == '__main__':
    state = input2state(INPUT)
    # state = input2state(TEST1)
    # print(state)

    n = 100
    # n = 5

    # part 2, uncomment these
    state[0, 0] = True
    state[-1, 0] = True
    state[0, -1] = True
    state[-1, -1] = True

    for i in range(n):
        print('\r', i, n, end='')
        state = take_step(state)
        # print(state)

        state[0, 0] = True
        state[-1, 0] = True
        state[0, -1] = True
        state[-1, -1] = True

    print()
    print(state.sum())
