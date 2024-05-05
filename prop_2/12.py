for n in range(4, 1000):
    s = '2' + '5' * n
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '32', 1)
        if '355' in s:
            s = s.replace('355', '25', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)

    sum_s = sum([int(x) for x in s])
    if sum_s ** 0.5 == (int(sum_s ** 0.5)):
        print(n)
        break