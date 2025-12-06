data = """3-5
10-14
10-14
16-20
12-18
11-12
10-14

1
5
8
11
17
32"""
data = open("input05").read()

freshrangesstr, available = data.split("\n\n")
freshranges = [
    range(int(rs[0]), int(rs[1]) + 1)
    for rr in freshrangesstr.splitlines()
    if (rs := rr.split("-"))
]
print(sum(any(int(i) in r for r in freshranges) for i in available.splitlines()))

# part 2
# ranges = set()
# for newrange in sranges:
#     overlapping_ranges = []
#     for oldrange in ranges:
#         if (
#             newrange.start in oldrange
#             or newrange.stop in oldrange
#             or oldrange.start in newrange
#             or oldrange.stop in newrange
#         ):
#             # the ranges overlap, so combine them
#             overlapping_ranges.append(oldrange)

#     if overlapping_ranges:
#         all_overlapping_ranges = overlapping_ranges + [newrange]
#         combined_range = range(
#             min(_.start for _ in overlapping_ranges),
#             max(_.stop for _ in overlapping_ranges),
#         )
#         for old in overlapping_ranges:
#             ranges.remove(old)
#         ranges.add(combined_range)
#     else:
#         ranges.add(newrange)
#     # print(newrange, ranges)
freshranges = [
    range(int(rs[0]), int(rs[1]))
    for rr in freshrangesstr.splitlines()
    if (rs := rr.split("-"))
]
sranges = sorted(freshranges, key=lambda r: r.start)

ranges = []
latest = sranges[0]
for r in sranges[1:]:
    if r.start >= latest.start and r.start <= latest.stop:
        latest = range(latest.start, max(r.stop, latest.stop))
    else:
        ranges.append(latest)
        latest = r
    # print(r, ranges)
ranges.append(latest)

print(sum(len(r) + 1 for r in ranges))
print(
    [
        [(r, ra) for ra in ranges if r != ra and (r.start in ra or r.stop in ra)]
        for r in ranges
    ]
)
