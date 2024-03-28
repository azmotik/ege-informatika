file = [int(x) for x in open('17_12926.txt')]
max_2 = max([int(x) for x in file if len(str(abs(x))) == 2])
a = 0
for i in range(len(file) - 3):
    if file[i] % 10 == file[i+1] % 10 == file[i+2] % 10 == file[i+3] % 10:
        a = max(a, file[i] + file[i+1] + file[i+2] + file[i+3])

count = 0
min_sum = 50000
for j in range(len(file)-4):
    count_a = 0
    sum_5 = 0
    for x in range(5):
        sum_5 += file[j+x]
        if file[j+x] < a:
            count_a += 1
    if count_a == 1 and sum_5 % a == 0:
        count += 1
    min_sum = min(min_sum, sum_5)
print(count, min_sum)



file = [int(x) for x in open('17_7848.txt')]
arr = []

for i in file:
    down_count = 0
    for j in range(len(str(i)) - 1):
        if str(i)[j] > str(i)[j+1]:
            down_count += 1
        if down_count == len(str(i)) - 1:
            arr.append(i)
min_arr = min(arr)
count = 0
min_sum = 200000
for s in range(len(file) - 1):
    par_count = 0
    up_count = 0
    for y in range(len(str(s)) - 1):
        if str(s)[y] < str(s)[y+1]:
            up_count+=1
        if up_count == len(str(s)) - 1:
            par_count+=1
    if par_count == 1 and (file[s] * file[s+1]) % sum([int(x) for x in str(min_arr)]) == 0:
        count+=1
        min_sum = min(min_sum, file[s] + file[s+1])
print(count, min_sum)

        
        
        