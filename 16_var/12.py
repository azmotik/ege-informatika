#var1
'''def f(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True


min_n = 5000
for n in range(1000):
    s = '>' + 31 * '0' + n * '1' + 47 * '2'
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '21>', 1)
        if '>2' in s:
            s = s.replace('>2', '12>', 1)
        if '>0' in s:
            s = s.replace('>0', '2>', 1)

    s = s.replace('>', '')
    if f(sum([int(x) for x in s])):
        min_n = min(min_n, n)
print(min_n)


#var2
s = '>' + 15 * '2' + 20 * '3' + 25 * '5'
while '>3' in s or '>2' in s or '>5' in s:
    if '>2' in s:
        s = s.replace('>2', '333>', 1)
    if '>3' in s:
        s = s.replace('>3', '23>', 1)
    if '>5' in s:
        s = s.replace('>5', '35>', 1)

s = s.replace('>', '')
print(sum([int(x) for x in s]))

#var4
s = '>' + 12 * '2' + 22 * '3' + 15 * '5'
while '>3' in s or '>2' in s or '>5' in s:
    if '>2' in s:
        s = s.replace('>2', '55>', 1)
    if '>3' in s:
        s = s.replace('>3', '523>', 1)
    if '>5' in s:
        s = s.replace('>5', '52>', 1)

s = s.replace('>', '')
print(sum([int(x) for x in s]))

#var5
for i in range(300):
    for j in range(300):
        for z in range(300):
            s = '2' * i + '4' * j + '6' * z
            s1 = s
            while '02' in s or '04' in s or '06' in s:
                if '02' in s:
                    s1 = s1.replace('02', '6404', 1)
                if '04' in s:
                    s1 = s1.replace('04', '2206', 1)
                if '06' in s:
                    s1 = s1.replace('06', '440', 1)

            if s1.count('2') == 30 and s1.count('4') == 54 and s1.count('6') == 10:
                print(s.count('6'))
                break

#var6
for i in range(300):
    for j in range(300):
        for z in range(300):
            s = '2' * i + '4' * j + '6' * z
            s1 = s
            while '02' in s or '04' in s or '06' in s:
                if '02' in s:
                    s1 = s1.replace('02', '620', 1)
                if '04' in s:
                    s1 = s1.replace('04', '4206', 1)
                if '06' in s:
                    s1 = s1.replace('06', '402', 1)

            if s1.count('2') == 38 and s1.count('4') == 32 and s1.count('6') == 28:
                print(s.count('4'))
                break'''

#var7
s = '>' + 15 * '1' + 16 * '4' + 20 * '6'
while '>1' in s or '>4' in s or '>6' in s:
    if '>1' in s:
        s = s.replace('>1', '4161>', 1)
    if '>4' in s:
        s = s.replace('>4', '1611>', 1)
    if '>6' in s:
        s = s.replace('>6', '414>', 1)

s = s.replace('>', '')
print(sum([int(x) for x in s]))

#var8
s = '>' + 32 * '1' + 11 * '4' + 22 * '6'
while '>1' in s or '>4' in s or '>6' in s:
    if '>1' in s:
        s = s.replace('>1', '1661>', 1)
    if '>4' in s:
        s = s.replace('>4', '146141>', 1)
    if '>6' in s:
        s = s.replace('>6', '141>', 1)

s = s.replace('>', '')
print(sum([int(x) for x in s]))

#var9
s = '>' + 10 * '2' + 11 * '4' + 12 * '7'
while '>2' in s or '>4' in s or '>7' in s:
    if '>2' in s:
        s = s.replace('>2', '72>', 1)
    if '>4' in s:
        s = s.replace('>4', '4>22', 1)
    if '>7' in s:
        s = s.replace('>7', '24>2', 1)

s = s.replace('>', '')
print(sum([int(x) for x in s]))