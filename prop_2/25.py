from fnmatch import *

arr = []
for i in range(10, 100):
    if fnmatch(str(i), '?4'):
        arr.append(i)

for i in range(124, 10**10, 124):
    count = 0
    for j in arr:
        if i % j == 0:
            count += 1

    if fnmatch(str(i), '1*28?64') and count == 5:
        print(i, i // 124)