# 27_1
file = open('27v01_A.txt').readlines()
K = int(file[0])
N = int(file[1])

min1 = 11000000000000000
min2 = 11000000000000000
min3 = 11000000000000000

for i in range(2, N + 2 - (K * 2)):
    min1 = min(min1, int(file[i]))
    min2 = min(min2, min1 + int(file[i + K]))
    min3 = min(min3, min2 + int(file[i + K * 2]))

print(min3)


# 27_17a
file = open('27/27v17_A.txt').readlines()
N = int(file[0])
arr = []

for i in range(1, N + 1):
    arr1 = file[i].split(' ')
    max_arr1 = max(int(arr1[0]), int(arr1[1]))
    arr.append(max_arr1)

print(sum(arr), sum(arr) % 39 != 0)

# 27_17a_b
file = open('27v17_B.txt').readlines()
N = int(file[0])
arr = []

for i in range(1, N + 1):
    arr1 = file[i].split(' ')
    max_arr1 = max(int(arr1[0]), int(arr1[1]))
    arr.append(max_arr1)


arr_sum = sum(arr)
for j in range(1, N + 1):
    min_razn = 600000

    for i in range(1, N + 1):
        arr1 = file[i].split(' ')
        razn = abs(int(arr1[0]) - int(arr1[1]))

        if razn != 0 and razn % 39 != 0:
            min_razn = min(min_razn, razn)

    #print(min_razn, arr_sum - min_razn, ( arr_sum - min_razn ) % 39 == 0)
    if arr_sum % 39 == 0:
        if (arr_sum - min_razn) % 39 != 0:
            print(min_razn, arr_sum - min_razn, (arr_sum - min_razn) % 39 == 0)
            break
    else:
        print(arr_sum, arr_sum % 39 == 0)
        break


