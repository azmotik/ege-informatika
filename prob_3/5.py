def f(n):
    r = ''
    while n > 0:
        r += str(n % 3)
        n //= 3
    return r[::-1]


min_r = 10000
for n in range(1, 10000):
    r = f(n)
    if len(r) % 2 != 0:
        r = '1' + r

    if sum([int(x) for x in r]) % 2 == 0:
        r += r[:2]
    else:
        r += f(n % 5)
    if r[0] == '2':
        r = r[1:]
    r1 = r

    for i in range(len(r1)):
        if r[i] == '0':
            r = r[1:]
        else:
            break
    if r[-1] == r[-2]:
        r = r[:-1]
    r = int(r, 3)
    if r > 150:
        min_r = min(min_r, r)
print(min_r)
