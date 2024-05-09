def f(n):
    r = ''
    while n > 0:
        r += str(n % 5)
        n //= 5
    return r[::-1]


min_n = 10000
for n in range(11, 10000):
    r = f(n)
    if n % 5 == 0:
        r += r[-3:]
    else:
        r = f((n % 5 * 5)) + r
    r = int(r, 5)
    if r > 375:
        min_n = min(min_n, n)
print(min_n)
