data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
data = """92916254-92945956,5454498003-5454580069,28-45,4615-7998,4747396917-4747534264,272993-389376,36290651-36423050,177-310,3246326-3418616,48-93,894714-949755,952007-1003147,3-16,632-1029,420-581,585519115-585673174,1041-1698,27443-39304,71589003-71823870,97-142,2790995-2837912,579556301-579617006,653443-674678,1515120817-1515176202,13504-20701,1896-3566,8359-13220,51924-98061,505196-638209,67070129-67263432,694648-751703,8892865662-8892912125"""

sum = 0
for r in data.split(","):
    r1, r2 = r.split("-")
    r1 = int(r1)
    r2 = int(r2)
    for n in range(r1, r2 + 1):
        ns = str(n)
        if len(ns) % 2 == 0 and ns[: len(ns) // 2] == ns[len(ns) // 2 :]:
            sum += n
            # print(r, n)
print(sum)

sum = 0
for r in data.split(","):
    r1, r2 = r.split("-")
    r1 = int(r1)
    r2 = int(r2)
    for n in range(r1, r2 + 1):
        ns = str(n)

        for patternlen in range(1, len(ns) // 2 + 1):
            npat, rem = divmod(len(ns), patternlen)
            if rem != 0:
                # not an even division of the pattern
                continue

            pats = set([ns[i * patternlen : (i + 1) * patternlen] for i in range(npat)])
            if len(pats) == 1:
                # print(r, n, pats)
                sum += n
                break
print(sum)
