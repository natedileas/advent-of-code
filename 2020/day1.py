
with open('input1-a.txt', 'r') as f:
    lines = f.readlines()

data = [int(l) for l in lines]

# part 1
for i, ii in enumerate(data):
    for j, jj in enumerate(data):
        if ii + jj == 2020:
            print('Part 1 Answer:', ii * jj)

# 806656

# part 2
for i, ii in enumerate(data):
    for j, jj in enumerate(data):
        for k, kk in enumerate(data):
            if ii + jj + kk == 2020:
                print('Part 2 Answer:', ii * jj * kk)

# 230608320
