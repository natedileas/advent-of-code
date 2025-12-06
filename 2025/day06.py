from functools import reduce

data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
data = open("input06").read()

numbers = []
ops = []
add = lambda a, b: a + b
mul = lambda a, b: a * b
for line in data.splitlines():
    if "+" in line:
        ops = [add if o == "+" else mul for o in line.split()]
    else:
        operands = [int(i) for i in line.split()]
        numbers.append(operands)

s = 0
for i, op in enumerate(ops):
    s += reduce(op, [j[i] for j in numbers])
print(s)

lines = data.splitlines()
ops = []
cols = []
n = 0
for c in lines[-1]:
    if c != " ":
        ops.append(add if c == "+" else mul)
        cols.append(n)
    n += 1
cols.append(n)

s = 0
for i, (c, o) in enumerate(zip(cols, ops)):
    length = cols[i + 1] - c
    ns = []
    for j in range(length):
        digits = "".join(line[c + j] for line in lines[:-1])
        if digits.replace(" ", ""):
            ns.append(int(digits))
    # print(reduce(o, ns), o, ns, c, length)
    s += reduce(o, ns)
print(s)
