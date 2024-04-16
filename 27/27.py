# 27_17
file = open('27/27v17_A.txt').readlines()
N = int(file[0])
arr = []

for i in range(1, N + 1):
    arr1 = file[i].split(' ')
    max_arr1 = max(int(arr1[0]), int(arr1[1]))
    arr.append(max_arr1)

print(sum(arr), sum(arr) % 39 != 0)

