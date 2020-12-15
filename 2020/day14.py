INPUT = open('input14.txt').read()

TEST1 = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

TEST2 = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""

import re

def set_bit(value, n):
    return value | (1 << n)

def clear_bit(value, n):
    return value & ~(1 << n)

def run_program(program):


    def applymask(val, mask):
        # print(bin(val))
        # print(mask)
        for i, bit in enumerate(mask[::-1]):
            if bit == 'X': 
                continue
            elif bit == '0':
                val = clear_bit(val, i)
            elif bit == '1':
                val = set_bit(val, i)
            else:
                raise Exception('unexpected value in mask')

        # print(bin(val))
        return val

    mask = None
    mem = {}
    for line in program.splitlines():
        if line:
            lhs, rhs = line.split('=')
            
            if 'mask' in lhs:
                mask = rhs.strip()

            else:
                match = re.fullmatch(r'mem\[(\d+)\]', lhs.strip())
                mem[match.group(1)] = applymask(int(rhs), mask)

    print(mem)
    return sum(mem.values())

def run_program_v2(program):

    def applymask(val, mask):
        floating = []
        for i, bit in enumerate(mask[::-1]):
            if bit == 'X': 
                floating.append(i)
            elif bit == '1':
                val = set_bit(val, i)

        addresses = []
        def floatt(value, bits_to_float, depth=0):
            if not bits_to_float:
                addresses.append(value)
                return

            bit = bits_to_float.pop(0)
            floatt(set_bit(value, bit), bits_to_float[:], depth=depth+1)
            floatt(clear_bit(value, bit), bits_to_float[:], depth=depth+1)
            
        floatt(val, floating[:])

        addresses = list(set(addresses))
        # print(addresses)
        return addresses

    mask = None
    mem = {}
    for line in program.splitlines():
        if line:
            lhs, rhs = line.split('=')
            
            if 'mask' in lhs:
                mask = rhs.strip()

            else:
                match = re.fullmatch(r'mem\[(\d+)\]', lhs.strip())
                addresses = applymask(int(match.group(1)), mask)
                for addr in addresses:
                    mem[addr] = int(rhs.strip())

    # print(mem)
    return sum(mem.values())



if __name__ == '__main__':
    # print(run_program(TEST1))
    # print(run_program(INPUT))
    # print(run_program_v2(TEST2))
    print(run_program_v2(INPUT))
