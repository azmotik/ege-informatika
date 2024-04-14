#26_01
'''file = open('26 вар1.txt')
data = []
for line in file:
    start, duration = map(int, line.split())
    end = start + duration
    data.append([end, start])

data.sort()
arr = [data[0]]
for i in range(1, len(data)):
    if data[i][1] >= arr[-1][0]:
        arr.append([data[i][0], data[i][1], i])

time = 0
for i in range(arr[-2][2] + 1, len(data)):
    time = max(time, data[i][1] - arr[-2][0])
print(len(arr), time)

#26_02
file = open('26 вар2.txt')
data = []
for line in file:
    start, duration = map(int, line.split())
    end = start + duration
    data.append([end, start])

data.sort()
arr = [data[0]]
for i in range(1, len(data)):
    if data[i][1] >= arr[-1][0]:
        arr.append([data[i][0], data[i][1], i])

time = 0
for i in range(arr[-2][2] + 1, len(data)):
    time = max(time, data[i][1] - arr[-2][0])
print(len(arr), time)

#26_03

file = open('26 вар3.txt')
data = []
for line in file:
    left, duration = map(int, line.split()) 
    data.append([left + duration, left])

data.sort()
arr = [[data[0][0], data[0][1], 0]] 

for i in range(1, len(data)):
    if data[i][1] >= arr[-1][0]:
        arr.append([data[i][0], data[i][1], i])

max_len = 0
for i in range(arr[-2][2] + 1, len(data)):
    max_len = max(max_len, data[i][1] - arr[-2][1])

print(len(arr), max_len)

#26_04
file = open('26 вар4.txt')
data = []   
for line in file:
    left, duration = map(int, line.split()) 
    data.append([left + duration, left])

data.sort()
arr = [[data[0][0], data[0][1], 0]] 

for i in range(1, len(data)):
    if data[i][1] >= arr[-1][0]:
        arr.append([data[i][0], data[i][1], i])

max_len = 0
for i in range(arr[-2][2] + 1, len(data)):
    max_len = max(max_len, data[i][1] - arr[-2][1])

print(len(arr), max_len)

#26_05
file = open('26var05.txt') 
n = int(file.readline())
data = [int(line) for line in file] 
data.sort(reverse=True)
arr = [data[0]]
for i in data[1:]:
    if arr[-1] - i >= 7: 
        arr.append(i)
print(len(arr), arr[-1])



#TODO: на занятии решали

# 26var079
file = open('26var09.txt').readlines()
N = int(file[0])
tuples = []
for i in range(1, N + 1):
    arr = file[i].split(' ')
    tuples.append((int(arr[0]), int(arr[1])))

tuples = sorted(tuples, key=lambda item: (item[0], item[1]), reverse=True)

result_arr = []
for i in range(len(tuples)-1):
    if int(tuples[i][1]) - int(tuples[i+1][1]) == 3:
        result_arr.append(tuples[i+1])

max_arr = max(result_arr, key=lambda t: t[0])

rrr = filter(lambda item: item[0] == max_arr[0], result_arr)
min_arr = min(rrr, key=lambda t: t[1])

print(result_arr)
print(max_arr[0], min_arr[1] + 1)
print(N)

# 26var07
file = open('26var07.txt').readlines()

n = int(file[0].split('\t')[0])
m = int(file[0].split('\t')[1])
arr_n = []
arr_m = []
for i in range(n):
    arr_n.append(int(file[i].split('\t')[0]))

for i in range(m):
    arr_m.append(int(file[i].split('\t')[1]))

arr_n.sort()
arr_m.sort()

arr_sorted = []
for i in range(m):
    if arr_m[i] in arr_n:
        arr_sorted.append(arr_m[i])
        arr_n.remove(arr_m[i])

max_res = 0
max_len = 0
for j in range(0, 50):
    arr1 = [arr_sorted[j]]
    for i in range(len(arr_sorted)):
        if arr_sorted[i] - arr1[-1] >= 6:
            arr1.append(arr_sorted[i])
    max_res = max(max_res, len(arr1))
    if max_res == len(arr1):
        max_len = max(max_len, arr_sorted[j])


print(arr_n)
print(arr_m)
print(arr_sorted)

print(n, m)
print(max_res, max_len)


# 26var06
file = open('26var06.txt').readlines()
arr = [int(x) for x in file]
n = int(arr[0])
arr = arr[1:]

arr.sort()

max_res = 0
max_len = 0
for j in range(0, 50):
    arr1 = [arr[j]]
    for i in range(len(arr)):
        if arr[i] - arr1[-1] >= 6:
            arr1.append(arr[i])
    max_res = max(max_res, len(arr1))
    if max_res == len(arr1):
        max_len = max(max_len, arr[j])

print(max_res, max_len)
print(arr)


file = open('26.7_13397.txt').readlines()
N = int(file[0])
tuples = []
for i in range(1, N + 1):
    arr = file[i].split(' ')
    tuples.append((int(arr[0]), int(arr[1]), int(arr[0]) + int(arr[1])))

tuples = sorted(tuples, key=lambda item: item[0])

max_time=max(tuples, key=lambda t: t[0])

arr = []
first = min(tuples, key=lambda t: t[2])
arr.append(first)

for i in range(N):
    arr_sort = filter(lambda item: item[0] >= first[2], tuples)
    first = min(arr_sort, key=lambda t: t[2])
    arr.append(first)
    if first[2] > max_time[0]:
        break

tuples_6 = sorted(tuples, key=lambda item: item[2])

print(arr)
print(tuples)
print(tuples_6)

print(len(arr))

# 26var10
file = open('26var10.txt').readlines()
N = int(file[0])
tuples = []
for i in range(1, N + 1):
    arr = file[i].split(' ')
    tuples.append((int(arr[0]), int(arr[1])))

tuples = sorted(tuples, key=lambda item: (item[0], item[1]))

result_arr = []
for i in range(len(tuples)-1):
    if int(tuples[i+1][1]) - int(tuples[i][1]) == 3:
        result_arr.append(tuples[i+1])

max_arr = min(result_arr, key=lambda t: t[0])

rrr = filter(lambda item: item[0] == max_arr[0], result_arr)
min_arr = max(rrr, key=lambda t: t[1])
print(result_arr)
print(max_arr[0], min_arr[1] - 1)

# 26var11
file = open('26var11.txt').readlines()
N = int(file[0])
tuples = []
for i in range(1, N + 1):
    arr = file[i].split(' ')
    tuples.append((int(arr[0]), int(arr[1])))

tuples = sorted(tuples, key=lambda item: (item[0], item[1]), reverse=True)

result_arr = []
for i in range(len(tuples)-1):
    if int(tuples[i][1]) - int(tuples[i+1][1]) == 4:
        result_arr.append(tuples[i+1])

max_arr = max(result_arr, key=lambda t: t[0])

rrr = filter(lambda item: item[0] == max_arr[0], result_arr)
min_arr = min(rrr, key=lambda t: t[1])
print(result_arr)
print(max_arr[0], min_arr[1] + 2)

# 26var12
file = open('26var12.txt').readlines()
N = int(file[0])
tuples = []
for i in range(1, N + 1):
    arr = file[i].split(' ')
    tuples.append((int(arr[0]), int(arr[1])))

tuples = sorted(tuples, key=lambda item: (item[0], item[1]))

result_arr = []
for i in range(len(tuples)-1):
    if int(tuples[i+1][1]) - int(tuples[i][1]) == 4:
        result_arr.append(tuples[i+1])

max_arr = min(result_arr, key=lambda t: t[0])

rrr = filter(lambda item: item[0] == max_arr[0], result_arr)
min_arr = max(rrr, key=lambda t: t[1])
print(result_arr)
print(max_arr[0], min_arr[1] - 1)

#26_13
file = open('26var13.txt').readlines()
S = int((file[0].split(' '))[0])
N = int((file[0].split(' '))[1])
arr = []
for i in range(1, N + 1):
    arr.append(int(file[i]))

arr = sorted(arr)
arr1 = []
for i in range(N):
    if arr1 == [] or sum(arr1) + arr[i] <= S:
        arr1.append(arr[i])
print(len(arr1))
arr1 = arr1[:-1]
for j in range(N):
    if sum(arr1) + arr[j] > S:
        print(arr[j - 1])
        break

#26_14
file = open('26var14.txt').readlines()
S = int((file[0].split(' '))[0])
N = int((file[0].split(' '))[1])
arr = []
for i in range(1, N + 1):
    arr.append(int(file[i]))

arr = sorted(arr)
arr1 = []
for i in range(N):
    if arr1 == [] or sum(arr1) + arr[i] <= S:
        arr1.append(arr[i])
print(len(arr1))
arr1 = arr1[:-1]
for j in range(N):
    if sum(arr1) + arr[j] > S:
        print(arr[j - 1])
        break

#26_15
file = open('26var15.txt').readlines()
S = int((file[0].split(' '))[0])
N = int((file[0].split(' '))[1])
arr = []
for i in range(1, N + 1):
    arr.append(int(file[i]))

arr = sorted(arr)
arr1 = []
for i in range(N):
    if arr1 == [] or sum(arr1) + arr[i] <= S:
        arr1.append(arr[i])
print(len(arr1))
arr1 = arr1[:-1]
for j in range(N):
    if sum(arr1) + arr[j] > S:
        print(arr[j - 1])
        break

#26_16
file = open('26var16.txt').readlines()
S = int((file[0].split(' '))[0])
N = int((file[0].split(' '))[1])
arr = []
for i in range(1, N + 1):
    arr.append(int(file[i]))

arr = sorted(arr)
arr1 = []
for i in range(N):
    if arr1 == [] or sum(arr1) + arr[i] <= S:
        arr1.append(arr[i])
print(len(arr1))
arr1 = arr1[:-1]
for j in range(N):
    if sum(arr1) + arr[j] > S:
        print(arr[j - 1])
        break

#26_17
file = open('26var17.txt').readlines()
S = int((file[0].split(' '))[0])
N = int((file[0].split(' '))[1])
arr = []
for i in range(1, N + 1):
    arr.append(int(file[i]))

arr = sorted(arr)
arr1 = []
for i in range(N):
    if arr1 == [] or sum(arr1) + arr[i] <= S:
        arr1.append(arr[i])
print(len(arr1))
arr1 = arr1[:-1]
for j in range(N):
    if sum(arr1) + arr[j] > S:
        print(arr[j - 1])
        break

#26_18
file = open('26var18.txt').readlines()
S = int((file[0].split(' '))[0])
N = int((file[0].split(' '))[1])
arr = []
for i in range(1, N + 1):
    arr.append(int(file[i]))

arr = sorted(arr)
arr1 = []
for i in range(N):
    if arr1 == [] or sum(arr1) + arr[i] <= S:
        arr1.append(arr[i])
print(len(arr1))
arr1 = arr1[:-1]
for j in range(N):
    if sum(arr1) + arr[j] > S:
        print(arr[j - 1])
        break

#26_19
file = open('26var19.txt').readlines()
S = int((file[0].split(' '))[0])
N = int((file[0].split(' '))[1])
arr = []
for i in range(1, N + 1):
    arr.append(int(file[i]))

arr = sorted(arr)
arr1 = []
for i in range(N):
    if arr1 == [] or sum(arr1) + arr[i] <= S:
        arr1.append(arr[i])
print(len(arr1))
arr1 = arr1[:-1]
for j in range(N):
    if sum(arr1) + arr[j] > S:
        print(arr[j - 1])
        break'''

#26_20
file = open('26var20.txt').readlines()
S = int((file[0].split(' '))[0])
N = int((file[0].split(' '))[1])
arr = []
for i in range(1, N + 1):
    arr.append(int(file[i]))

arr = sorted(arr)
arr1 = []
for i in range(N):
    if arr1 == [] or sum(arr1) + arr[i] <= S:
        arr1.append(arr[i])
print(len(arr1))
arr1 = arr1[:-1]
for j in range(N):
    if sum(arr1) + arr[j] > S:
        print(arr[j - 1])
        break