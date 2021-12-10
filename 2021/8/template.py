
import itertools as it
# import numpy as np

"""

Digit Map:

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

|     | a   | b   | c   | d   | e   | f   | g   | Sum |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| 0   | x   | x   | x   |     | x   | x   | x   | 6   |
| 1   |     |     | x   |     |     | x   |     | 2   |
| 2   | x   |     | x   | x   | x   |     | x   | 5   |
| 3   | x   |     | x   | x   |     | x   | x   | 5   |
| 4   |     | x   |     | x   |     | x   |     | 4   |
| 5   | x   | x   |     | x   |     | x   | x   | 5   |
| 6   | x   | x   |     | x   | x   | x   | x   | 6   |
| 7   | x   |     | x   |     |     | x   |     | 3   |
| 8   | x   | x   | x   | x   | x   | x   | x   | 7   |
| 9   | x   | x   | x   | x   |     | x   | x   | 6   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Sum | 8   | 6   | 8   | 7   | 4   | 9   | 7   |     |

"""


signal2digit = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9',
}

INPUT = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""
# INPUT = """
# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
# """
INPUT = open('input.txt').read()


def count_uniq_digited_outputs(input):
    words = [word for line in input.splitlines(
    ) if line for word in line.split('|')[-1].split()]
    matching_words = list(
        filter(lambda word: len(word) in (2, 4, 3, 7), words))
    return len(matching_words)


def analyse_digits(input):
    messages = []
    for line in input.splitlines():
        if not line:
            continue
        mapping = {}
        signals, outputs = line.split('|')
        signals = signals.split()
        outputs = outputs.split()

        one = next(filter(lambda s: len(s) == 2, signals))
        four = next(filter(lambda s: len(s) == 4, signals))
        seven = next(filter(lambda s: len(s) == 3, signals))
        eight = next(filter(lambda s: len(s) == 7, signals))

        counts = {}
        for word in signals:
            for c in word:
                counts.setdefault(c, 0)
                counts[c] += 1

        mapping[[k for k, v in counts.items() if v == 6][0]] = 'b'
        mapping[[k for k, v in counts.items() if v == 4][0]] = 'e'
        mapping[[k for k, v in counts.items() if v == 9][0]] = 'f'

        ac = [k for k, v in counts.items() if v == 8]
        dg = [k for k, v in counts.items() if v == 7]

        if ac[0] in seven and ac[0] not in one:
            mapping[ac[0]] = 'a'
            mapping[ac[1]] = 'c'
        else:
            mapping[ac[0]] = 'c'
            mapping[ac[1]] = 'a'

        if dg[0] in eight and dg[0] not in four:
            mapping[dg[0]] = 'g'
            mapping[dg[1]] = 'd'
        else:
            mapping[dg[0]] = 'd'
            mapping[dg[1]] = 'g'

        message = ''
        for word in outputs:
            message += signal2digit[''.join(sorted([mapping[char]
                                                    for char in word]))]
        # print(outputs, message)
        messages.append(int(message))
    return messages


if __name__ == '__main__':
    print('part 1: ', count_uniq_digited_outputs(INPUT))

    print('part 2: ', sum(analyse_digits(INPUT)))
