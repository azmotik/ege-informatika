max_n = 0
for n in range(3, 5000):
    s = '5' + n * '2'
    while '52' in s or '2222' in s or '1112' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
            s = s.replace('2222', '5', 1)
        else:
            s = s.replace('1112', '2', 1)

    if sum([int(x) for x in s]) == 1685:
        max_n = max(max_n, n)
print(max_n)