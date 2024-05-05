from itertools import *
arr = [x for x in product(sorted('МОДУЛЬ'), repeat = 6)]
arr_2 = []
for i in range(len(arr)):
    if i % 2 != 0 and arr[i][0] == 'М':
        arr_2.append(i)
print(arr_2)
print(arr_2[-1] - arr_2[0] - 1)