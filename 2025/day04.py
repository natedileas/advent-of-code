data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
data = open("input04").read()

# <4 in 8 neighborhood
papers = [[s == "@" for s in line] for line in data.splitlines()]
nrows, ncols = len(papers), len(papers[0])


def eightneighbood(row, col):
    indices = []

    indices = [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1),
    ]
    values = []
    for r, c in indices:
        if 0 <= r <= nrows - 1 and 0 <= c <= ncols - 1:
            values.append(papers[r][c])

    return indices, values


def setx(indices):
    p = papers[:]
    for r, c in indices:
        p[r][c] = "x"

    for line in p:
        for c in range(len(line)):
            line[c] = "@" if line[c] == True else "." if line[c] == False else line[c]

    print("\n".join("".join(l) for l in p))


valid = []
for r in range(nrows):
    for c in range(ncols):
        i, v = eightneighbood(r, c)
        if sum(v) < 4 and papers[r][c]:
            valid += [(r, c)]

print(len(valid))
# setx(valid)


def find_valid(p):
    valid = []
    for r in range(nrows):
        for c in range(ncols):
            i, v = eightneighbood(r, c)
            if sum(v) < 4 and p[r][c]:
                valid += [(r, c)]
    return valid


p = papers[:]
removed = 0
while True:
    v = find_valid(p)
    if not v:
        break
    removed += len(v)
    for r, c in v:
        p[r][c] = False

print(removed)
