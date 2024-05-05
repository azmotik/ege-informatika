symbols = '0123456789ABCDEFGHI'
maxx = 0
for x in symbols:
    s1 = f'98897{x}21'
    s2 = f'2{x}923'
    result = int(s1, 19) + int(s2, 19)
    if result % 18 == 0:
        maxx = max(maxx, result // 18)
print(maxx)