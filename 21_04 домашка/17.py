#12471
file = [int(x) for x in open('files/17_12471.txt')]
max_arr = max([int(x) for x in file if int(x) % 100 == 13])
sum_3 = 0
count = 0
for i in range(len(file) - 2):
    if file[i] % 2 == 0 and file[i + 1] % 2 == 0 and file[i + 2] % 2 == 0 or len(str(file[i])) == 2 or len(str(file[i + 1])) == 2 or len(str(file[i + 2])) == 2:
        sum1 = file[i] + file[i + 1] + file[i + 2]
        if sum1 <= max_arr:
            count += 1
            sum_3 += sum1
print(count, int(sum_3 / count))


#12735
file1 = [int(x) for x in open('files/17_12735.txt')]
max_arr = max([int(x) for x in open('files/17_12735.txt') if int(x) % 100 == 9])
min_sum = 10**10
count = 0
for i in range(len(file) - 2):
    crat7_count = 0
    sum1 = 0
    sum2 = 1
    for j in range(3):
        sum1 += file[i + j]
        sum2 *= file[i + j]
        if file[i + j] % 7 == 0:
            crat7_count += 1
    if crat7_count == 2 and sum1 < max_arr:
        count += 1
        min_sum = min(min_sum, sum2)
print(count, min_sum)




