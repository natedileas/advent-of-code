
import itertools as it
import numpy as np

INPUT = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""
INPUT = open('input.txt').read()


def make_boards(lines):
    boards = []
    for i in lines:
        board = np.zeros((5, 5), dtype=int)
        called = np.zeros((5, 5), dtype=bool)
        for ii, line in enumerate(i.splitlines()):
            for j, val in enumerate(line.split()):
                board[ii][j] = int(val)

        boards.append((board, called))

    return boards


def marknumber(board, number):
    #  reference or value?
    board, called = board
    called[np.where(board == number)] = True


def checkwin(board):
    board, called = board
    return np.any(np.all(called, axis=0)) or np.any(np.all(called, axis=1))


def get_sum_unmarked(board):
    board, called = board
    return np.sum(board[called == False])


def play_bingo(input):
    stuff = input.split('\n\n')
    numbers = stuff[0]
    boards = make_boards(stuff[1:])

    for n in map(int, numbers.strip().split(',')):
        for board in boards:
            marknumber(board, n)
            haswon = checkwin(board)

            if haswon:
                s = get_sum_unmarked(board)
                return s * n


def play_bingov2(input):
    stuff = input.split('\n\n')
    numbers = stuff[0]
    boards = make_boards(stuff[1:])

    winningscores = []
    skipboards = []
    for n in map(int, numbers.strip().split(',')):
        for i, board in enumerate(boards):
            marknumber(board, n)
            haswon = checkwin(board)

            if haswon and not i in skipboards:
                s = get_sum_unmarked(board)
                winningscores.append(s * n)
                skipboards.append(i)

    return winningscores[-1]


if __name__ == '__main__':
    print('part 1: ', play_bingo(INPUT))
    print('part 2: ', play_bingov2(INPUT))
