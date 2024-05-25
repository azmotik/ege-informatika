#var1
'''s = '0123456789ABC'
min_x = 'C'
for x in s:
    sum = int(f'206{x}9', 13) + int(f'3{x}027', 13) - int(f'{x}52', 13)
    if sum % 11 == 0:
        min_x = min(min_x, x)

print((int(f'206{min_x}9', 13) + int(f'3{min_x}027', 13) - int(f'{min_x}52', 13)) // 11)

#var2
s = '0123456789A'
min_x = 'C'
for x in s:
    sum = int(f'1800{x}6', 11) + int(f'6{x}107', 11) - int(f'1{x}63', 11)
    if sum % 7 == 0:
        min_x = min(min_x, x)

print((int(f'1800{min_x}6', 11) + int(f'6{min_x}107', 11) - int(f'1{min_x}63', 11)) // 7)

#var3
s = '0123456789ABC'
min_x = 'C'
for x in s:
    sum = int(f'186{x}4', 13) + int(f'5{x}716', 13)
    if sum % 11 == 0:
        min_x = min(min_x, x)

print((int(f'186{min_x}4', 13) + int(f'5{min_x}716', 13)) // 11)

#var4
s = '0123456789ABCDEFG'
min_x = 'G'
for x in s:
    sum = int(f'26{x}34', 17) + int(f'3{x}597', 17)
    if sum % 13 == 0:
        min_x = min(min_x, x)
print((int(f'26{min_x}34', 17) + int(f'3{min_x}597', 17)) // 13)
'''


#var5
def f(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n = n // 3
    s = s[::-1]
    return s

#var6
for x in range(10000):
    summ = 243 ** 5 + 3 ** 7 - 2 - x
    if f(summ).count('2') == 20:
        print(x)
        break

#var7
def f5(n):
    s = ''
    while n > 0:
        s += str(n % 5)
        n = n // 5
    s = s[::-1]
    return s

summ = 125 ** 300 * 5 ** 300 - 25**70 - 100
print(f5(summ).count('4'))

#var8
def f4(n):
    s = ''
    while n > 0:
        s += str(n % 4)
        n = n // 4
    s = s[::-1]
    return s

summ = 256 ** 500 * 4 ** 100 - 64**30 - 8
print(f4(summ).count('3'))

summ = 5 ** 200 + 25 ** 1000 - 5**50
print(f5(summ).count('0'))


