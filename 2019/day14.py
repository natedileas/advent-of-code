import math

class Value:
    def __init__(self, s):
        self.value, self.unit = s.split()
        self.value = int(self.value)

    def __repr__(self):
        return f'{self.value} {self.unit}'

    def __str__(self):
        return repr(self)

def count_ore1(data):
    lines = data.splitlines()

    graph = {}
    # graph['ORE'] = 

    for line in lines:
        if line:
            ins, out = line.split('=>')
            inputs = [Value(i) for i in ins.split(',')]
            output = Value(out)
            graph[output] = inputs

    graph[Value('1 ORE')] = [Value('1 ORE')]
    import pprint, math
    # pprint.pprint(graph)

    out_vals = {}
    leftover_ore = {}
    keys = list(graph.keys())
    while len(keys) > 1:
        output = keys.pop(0)
        inputs = graph[output]

        # if it doesn't have any upstream deps
        if output.unit not in (v.unit for out, ins in graph.items() for v in ins ):
            # print(output, out_vals)
            # process the rule
            out_vals.setdefault(output.unit, output.value)
            leftover_ore.setdefault(output.unit, output.value)

            for v in inputs:
                out_vals.setdefault(v.unit, 0)
                leftover_ore.setdefault(v.unit, 0)
                out_vals[v.unit] += math.ceil(out_vals[output.unit] / output.value) * v.value
                leftover_ore[v.unit] += leftover_ore[output.unit] / output.value * v.value

            # del keys[output]
            del graph[output]
        else:
            keys.append(output)

    return out_vals['ORE'], out_vals['ORE'] - leftover_ore['ORE']


TEST1 = """
10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL
"""

TEST2 = """
9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL
"""

TEST3 = """
157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT
"""

TEST4 = """
2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF
"""

TEST5 = """
171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX
"""

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)

    print(count_ore1(TEST1), 31)
    print(count_ore1(TEST2), 165)
    print(count_ore1(TEST3), 13312)
    print(count_ore1(TEST4), 180697)
    print(count_ore1(TEST5), 2210736)
    print('Part 1:', count_ore1(open('input14.txt').read()))

    # The 13312 ORE-per-FUEL example could produce 82892753 FUEL.
    # The 180697 ORE-per-FUEL example could produce 5586022 FUEL.
    # The 2210736 ORE-per-FUEL example could produce 460664 FUEL.

    def count_fuel_for_n(data, n=1000000000000):
        # floor(1 trillion [ore] / n [ore / fuel]) = m [fuel]
        rounded, leftover = count_ore1(data)
        exact = rounded - leftover
        return int(n // exact)

    print(count_fuel_for_n(TEST3), 82892753)
    print(count_fuel_for_n(TEST4), 5586022)
    print(count_fuel_for_n(TEST5), 460664)

    print('Part 2:', count_fuel_for_n(open('input14.txt').read()))  # 1896689 is "too high"
