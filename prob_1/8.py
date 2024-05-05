from itertools import *
count = 0
for a in list(permutations('0234567', 5)):
    a = ''.join(a)
    if a[0] != '0':
        a = a.replace('5', '3').replace('7', '3')
        a = a.replace('2', '0').replace('4', '0').replace('6', '0')
        if '00' not in a and '33' not in a:
            count += 1
print(count)