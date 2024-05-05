symbols = '0123456789ABCDEFGHIJKLMNO'
maxx = 0
for x in symbols:
    s = int(f'B7{x}35F1', 25) + int(f'16{x}K1', 25) + int(f'1{x}G', 25)
    if s % 24 == 0:
        maxx = max(maxx, s // 24)

print(maxx)