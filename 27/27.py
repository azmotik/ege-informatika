# 27_1
file = open('27v01_A.txt').readlines()
K = int(file[0])
N = int(file[1])

# минимальный элемент
min_sum1 = 11000000000000000

# минимальная сумма первого элемента со второмы элементом который входит в диапазоне от i + K минимального до K * 2 элемента
min_sum2 = 11000000000000000

# минимальная сумма трех элементов(сумма двух + 3 элемент) от K * 2 до конца файла
min_sum3 = 11000000000000000

for i in range(2, N + 2 - (K * 2)):
    min_sum1 = min(min_sum1, int(file[i]))
    min_sum2 = min(min_sum2, min_sum1 + int(file[i + K]))
    min_sum3 = min(min_sum3, min_sum2 + int(file[i + K * 2]))

print(min_sum3)



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


