from itertools import *
count = 0
for a in set(permutations('0123456789', 6)):
    a = ''.join(a)
    if a[0] != '0' and int(a) % 5 == 0:
        a = a.replace('2', '0').replace('4', '0').replace('6', '0').replace('8', '0')
        a = a.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
        if '00' not in a and '11' not in a:
            count += 1

print(count)