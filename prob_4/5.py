def f(n):
    r = ''
    while n > 0:
        r += str(n % 5)
        n //= 5
    return r[::-1]


min_n = 100000
for n in range(1, 10000):
    r = f(n)
    if n % 25 == 0:
        r = r[-3:] + r
    else:
        r += f((n % 25))
    r = int(r, 5)
    if r > 10000:
        min_n = min(min_n, n)
print(min_n)
