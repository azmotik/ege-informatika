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

print(len(arr), max_len)'''

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
