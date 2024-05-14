max_sum = 0
for n in range(3, 1000):
    s = '1' + n * '9'
    while '19' in s or '49' in s or '999' in s:
        if '19' in s:
            s = s.replace('19', '9', 1)
        if '49' in s:
            s = s.replace('49', '91', 1)
        if '999' in s:
            s = s.replace('999', '4', 1)
    sum_s = sum([int(x) for x in s])
    max_sum = max(max_sum, sum_s)
print(max_sum)