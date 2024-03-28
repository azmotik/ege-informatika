from fnmatch import *

'''for i in range(0, 10**10, 2024):
    if fnmatch(str(i), '1?2*4') and int(i**0.5)**2 == i:
        print(i, i//2024)


for i in range(98591, 10**7, 98591):
    if fnmatch(str(i), '12?3*456??9'):
        print(i, i//98591)

for i in range(3057, 10**9, 3057):
    if fnmatch(str(i), '1?58*5?9'):
        print(i, i//3057)

#12477
for i in range(1, 10**7):
    if fnmatch(str(i), '3?1111*'):
        if i == 1:
            continue
        for d in range(2, int(i**0.5)+1):
            if i % d == 0:
                continue
        print(i)

# TODO: не получилось        
#11814
for i in range(1777, 10**10+1, 1777):
    if fnmatch(str(i), '21*68?79'):
        if len(str(i)) == 10:
            print(i, i//1777)'''

sum = 0
count = 0
for i in range(596, 10**12, 596):
    if fnmatch(str(i), '1*28?64'):
        sum += i
        count += 1
print(count, int(count/i))