from itertools import *
arr = [x for x in product(sorted('АЕКПТЧ'), repeat = 7)]
arr_2 = []
for i in range(len(arr)):
    r = ''.join(arr[i])
    if r == 'АПТЕЧКА':
        arr_2.append(i)
    if r == 'ПЕЧАТКА':
        arr_2.append(i)
print(arr_2)
print(arr_2[1] - arr_2[0] - 1)