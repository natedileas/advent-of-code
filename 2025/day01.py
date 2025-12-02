data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
data = open("input01").read()
lines = data.splitlines()

positions = [50]
zerocount = 0
for l in lines:
    direction, distance = l[0], int(l[1:])
    sign = -1 if direction == "L" else 1

    unrolled = positions[-1] + sign * distance
    count, new = divmod(unrolled, 100)
    count = sum((p % 100) == 0 for p in range(positions[-1], unrolled, sign))
    zerocount += abs(count)
    print(positions[-1], l, count, new, zerocount)
    positions.append(new)

print(sum(p == 0 for p in positions))
print(zerocount)
