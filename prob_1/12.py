#сделал со второго раза
max_n = 0
for n in range(3, 1000):
    s = '5' + n * '2'
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)

    if sum([int(x) for x in s]) == 64:
        max_n = max(max_n, n)
print(max_n)