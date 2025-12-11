from itertools import combinations

data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
data = open("input10").read()


def combine(buttoncombinations):
    all = [b for btns in buttoncombinations for b in btns]
    indices = []
    for i in set(all):
        if sum(i == j for j in all) % 2 == 1:
            indices.append(i)
    return sorted(indices)


s = 0
for line in data.splitlines():
    indic, *buttons, joltagess = line.split()
    indiceson = [i for i, c in enumerate(indic[1:-1]) if c == "#"]

    buttonidxs = tuple(tuple(int(c) for c in b[1:-1].split(",")) for b in buttons)
    for n in range(1, len(buttonidxs)):
        if any(combine(bcs) == indiceson for bcs in combinations(buttonidxs, n)):
            # print(line, n)
            s += n
            break

print(s)


from ortools.sat.python import cp_model

s = 0
for line in data.splitlines():
    indic, *buttons, joltagess = line.split()
    indiceson = [i for i, c in enumerate(indic[1:-1]) if c == "#"]

    jolts = tuple(int(c) for c in joltagess[1:-1].split(","))
    buttonidxs = tuple(tuple(int(c) for c in b[1:-1].split(",")) for b in buttons)
    model = cp_model.CpModel()

    button_vars = []
    # only variable is how many times we're pressing the buttons
    for b, idxs in enumerate(buttonidxs):
        bvar = model.new_int_var(0, max(jolts), f"button_presses_{b}")
        button_vars.append(bvar)

    for i, j in enumerate(jolts):
        # constrain what the buttons do; when pressed, they add one to the appropriate outputs
        # strike above. the constaint is that the total number of buttons presses (for buttons which affect a particular output) has equal the output joltage.
        model.add(
            sum(b for b, bidxs in zip(button_vars, buttonidxs) if i in bidxs) == j
        )

    model.minimize(sum(button_vars))  # find the minimum number of presses
    solver = cp_model.CpSolver()
    status = solver.solve(model)
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        # print(status)
        # print(",".join(str(solver.value(b)) for b in button_vars))
        s += sum(solver.value(b) for b in button_vars)
    else:
        raise ValueError("no solution")
print(f"{s=}")
