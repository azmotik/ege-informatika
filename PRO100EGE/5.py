def f(n):
    r = ''
    while n > 0:
        r += str(n % 3)
        n = n // 3
    r = r[::-1]
    return r

min_r = 100000
for n in range(1, 10000):
    r = f(n)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += f((n % 3) * 5)
    r = int(r, 3)
    if r > 133:
        min_r = min(min_r, r)

print(min_r)