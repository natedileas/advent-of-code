
import itertools as it
# import numpy as np

INPUT = """
forward 5
down 5
forward 8
up 3
down 8
forward 2"""
INPUT = open('input.txt').read()


def plot_pos(input):
    x = 0
    y = 0

    for line in input.splitlines():
        if not line:
            continue

        if line.startswith('forward'):
            x += int(line.replace('forward ', ''))
        elif line.startswith('down'):
            y -= int(line.replace('down ', ''))
        elif line.startswith('up'):
            y += int(line.replace('up ', ''))

    return x, y


def plot_posv2(input):
    x = 0
    y = 0
    aim = 0

    for line in input.splitlines():
        if not line:
            continue

        if line.startswith('forward'):
            w = int(line.replace('forward ', ''))
            x += w
            y += aim * w
        elif line.startswith('down'):
            aim += int(line.replace('down ', ''))
        elif line.startswith('up'):
            aim -= int(line.replace('up ', ''))

    return x, y


if __name__ == '__main__':
    print('part 1: ', plot_pos(INPUT))
    print('part 2: ', plot_posv2(INPUT))
