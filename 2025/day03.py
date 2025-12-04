data = """987654321111111
811111111111119
234234234234278
818181911112111"""
data = open("input03").read()

sum = 0
banks = data.splitlines()
for bank in banks:
    first = max(bank[:-1])
    second = max(bank[bank.index(first) + 1 :])
    # print(bank, first, second)
    sum += int(first + second)
print(sum)

sum = 0
banks = data.splitlines()
for _bank in banks:
    bank = list(_bank)
    s, e = 0, -11
    digits = []
    used = []
    for i in range(12):
        if e == 0:
            digit = max(bank[s:])
        else:
            digit = max(bank[s:e])
        digits.append(digit)
        used.append(bank.index(digit))
        for i in range(int(used[-1]) + 1):
            bank[i] = "0"
        s = max(used) + 1
        e += 1
    print(_bank, "".join(bank), "".join(digits))
    sum += int("".join(digits))
print(sum)
