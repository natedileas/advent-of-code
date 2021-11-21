

def proc(program):
    instructions = list(filter(lambda line: line, program.splitlines()))
    pointer = 0
    reg = dict(a=1, b=0)

    while pointer < len(instructions):
        instr = instructions[pointer]
        # print(pointer, instr, reg)
        if instr.startswith('hlf'):
            reg[instr.replace('hlf ', '')] //= 2
        elif instr.startswith('tpl'):
            reg[instr.replace('tpl ', '')] *= 3
        elif instr.startswith('inc'):
            reg[instr.replace('inc ', '')] += 1
        elif instr.startswith('jmp'):
            offset = int(instr.replace('jmp ', ''))
            pointer += offset
            continue
        elif instr.startswith('jie'):
            jie, r, offset = instr.split()
            if reg[r.replace(',', '')] % 2 == 0:
                pointer += int(offset)
                continue
        elif instr.startswith('jio'):
            jio, r, offset = instr.split()
            if reg[r.replace(',', '')] == 1:
                pointer += int(offset)
                continue

        pointer += 1

    return reg


print(proc("""
inc a
jio a, +2
tpl a
inc a
"""))

print(proc("""
jio a, +19
inc a
tpl a
inc a
tpl a
inc a
tpl a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jmp +23
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7
"""))
