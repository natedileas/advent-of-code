from functools import reduce


def factors(n):
    return set(reduce(list.__add__, ([i, n//i]
                                     for i in range(1, int(n**0.5) + 1)
                                     if n % i == 0)))


print('part 1')
# n = 0
# n_p = 0
# while n_p < 29000000:
#     n += 1
#     n_p = 10 * sum(factors(n))
#     print('\r', n, n_p, end='')

# print()
# print(n, n_p)

print('part 2')
n = 0
n_p = 0
while n_p < 29000000:
    n += 1
    n_p = 11 * sum(filter(lambda f: f * 50 >= n, factors(n)))
    print('\r', n, n_p, end='')

print()
print(n, n_p)
